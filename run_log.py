# Interaction logging for the Streamlit demo.
"""Log every interpretation run so the team can review usage later.

Runs always go to the console through loguru. Streamlit Community Cloud
surfaces that stream in the app's Manage app console, but only as a live
tail that disappears on reboot. When the Streamlit secrets provide an
hf_token, each run is also appended as JSONL to a private Hugging Face
dataset through a background CommitScheduler, which gives the team a
durable, reviewable history.

Secrets:
    hf_token: A Hugging Face write token. Enables persistence.
    log_dataset: Optional dataset repo id; defaults to DEFAULT_LOG_DATASET.
"""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st
from loguru import logger

DEFAULT_LOG_DATASET = "ufdatastudio/mixtec-parser-logs"
LOG_FOLDER = Path("interaction_logs")


def _secret(name: str) -> str | None:
    try:
        return st.secrets.get(name)
    except Exception:
        return None


@st.cache_resource
def _scheduler():
    """A CommitScheduler pushing the log folder to a private dataset, or None."""
    token = _secret("hf_token")
    if not token:
        logger.info("No hf_token secret; interaction logs stay on the console.")
        return None
    try:
        from huggingface_hub import CommitScheduler

        repo_id = _secret("log_dataset") or DEFAULT_LOG_DATASET
        LOG_FOLDER.mkdir(exist_ok=True)
        scheduler = CommitScheduler(
            repo_id=repo_id,
            repo_type="dataset",
            folder_path=LOG_FOLDER,
            path_in_repo="logs",
            every=5,
            private=True,
            token=token,
        )
        logger.info("Interaction logs persist to {} every 5 minutes.", repo_id)
        return scheduler
    except Exception as exc:
        logger.warning("Could not start the log scheduler: {}", exc)
        return None


def _session_id() -> str:
    if "run_session_id" not in st.session_state:
        st.session_state.run_session_id = uuid.uuid4().hex[:12]
    return st.session_state.run_session_id


def build_record(
    session_id: str,
    source: str,
    specs: list[dict],
    sentences: list[str] | None = None,
    error: str | None = None,
) -> dict:
    """Assemble one JSON-serializable record of an interpretation run."""
    return {
        "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "session": session_id,
        "source": source,
        "token_count": len(specs),
        "specs": specs,
        "narration": sentences,
        "error": error,
    }


def log_run(
    source: str,
    specs: list[dict],
    sentences: list[str] | None = None,
    error: str | None = None,
) -> None:
    """Log one interpretation run, once per distinct scene per source.

    Streamlit reruns the script on every widget interaction, so identical
    consecutive runs are deduplicated per source through session state.
    """
    digest = json.dumps([source, specs, error], sort_keys=True, default=str)
    marker = f"_last_logged_{source}"
    if st.session_state.get(marker) == digest:
        return
    st.session_state[marker] = digest

    record = build_record(_session_id(), source, list(specs), sentences, error)
    logger.info("run {}", json.dumps(record, ensure_ascii=False))

    scheduler = _scheduler()
    if scheduler is not None:
        path = LOG_FOLDER / f"runs-{datetime.now(timezone.utc):%Y-%m-%d}.jsonl"
        with scheduler.lock, path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")
