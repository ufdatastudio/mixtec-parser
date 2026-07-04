"""Tests for the interaction run records."""

import json

import run_log
import scenes


def test_build_record_is_json_serializable():
    specs = [scenes.human_spec("Lord", "standing", "right")]
    record = run_log.build_record(
        "abc123", "compose", specs, sentences=["There was a Lord."]
    )
    assert record["session"] == "abc123"
    assert record["source"] == "compose"
    assert record["token_count"] == 1
    assert record["narration"] == ["There was a Lord."]
    assert record["error"] is None
    assert record["time"].endswith("+00:00")
    assert json.loads(json.dumps(record)) == record


def test_build_record_captures_errors():
    record = run_log.build_record("abc123", "xml", [], error="unexpected end of input")
    assert record["error"] == "unexpected end of input"
    assert record["narration"] is None
