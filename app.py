"""Streamlit demo for the Mixtec scene parser and interpreter.

Interactive companion to Driggers-Ellis, Ayoubi, Salunke, and Grant, "Formal
Machine Interpretation for the Semasiographic Mixtec Codices of Precolonial
and Early Colonial Mesoamerica" (ALVR 2026, pages 230-238).

Run with: uv run streamlit run app.py
"""

import base64
import copy
import functools
import html
import os

import streamlit as st
from loguru import logger

import ast_viz
import interpreter
import parser
import presets
import scenes
import sketch

APP_DIR = os.path.dirname(os.path.abspath(__file__))

PAPER_URL = "https://aclanthology.org/2026.alvr-main.20/"
PAPER_PDF_URL = "https://aclanthology.org/2026.alvr-main.20.pdf"
POSTER_URL = "https://ufdatastudio.com/papers/driggers-ellis2026formal-poster.pdf"
LAB_URL = "https://ufdatastudio.com"
VIT_DEMO_URL = "https://mixtec.streamlit.app"
SCENES_DATASET_URL = "https://huggingface.co/datasets/ufdatastudio/mixtec-zouche-nuttall-british-museum"
FIGURES_DATASET_URL = "https://huggingface.co/datasets/ufdatastudio/mixtec-figures"

BIBTEX = """@inproceedings{driggers-ellis-etal-2026-formal,
    title = "Formal Machine Interpretation for the Semasiographic {M}ixtec Codices of Precolonial and Early Colonial Mesoamerica",
    author = "Driggers-Ellis, Christopher and Ayoubi, Gabriel and Salunke, Girish and Grant, Christan",
    booktitle = "Proceedings of the 4th Workshop on Advances in Language and Vision Research ({ALVR})",
    month = jul,
    year = "2026",
    address = "San Diego, California, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.alvr-main.20/",
    pages = "230--238",
    doi = "10.18653/v1/2026.alvr-main.20"
}"""

ABSTRACT = (
    "The precolonial and early colonial Mixtec codices describe the history and "
    "stories of the region in a semasiographic medium that is full of symbolic "
    "representations and meant to be narrated. Recently, the community has "
    "investigated hierarchical representation of related media, including Aztec "
    "codices and Mayan hieroglyphic script, in a step towards symbolic machine "
    "interpretation of these historic Mesoamerican artifacts. In this work, we "
    "propose formal symbolic machine interpretation of XML encodings representing "
    "facsimile images from the Mixtec Codex Zouche-Nuttall. We demonstrate the "
    "efficacy of symbolic machine interpretation from XML step-by-step, showing "
    "how our parser and interpreter process text capturing a scene from the "
    "Mixtec Codex Zouche-Nuttall. We hope our contribution and the example we "
    "provide motivate collaboration among the archaeological, historical, "
    "linguistic, and natural language processing research communities to apply "
    "machine interpretation to Mixtec codices and similar manuscripts."
)

GRAMMAR_TEXT = """S         = (Sent end)+
Sent      = Clause | obj (Date Clause | Clause) | Date (obj Clause | Clause)
Clause    = Clause_f+ (Date_tail | Obj_tail | ε)
Date_tail = Date (obj Clause_f+ | Clause_f+ | ε)
Obj_tail  = obj (Date Clause_f+ | Clause_f+ | ε)
Date      = y (nd | ε)
Clause_f  = h (nd | Near_date | ε)
Near_date = near_obj (nd | ε)"""

NONE_OPTION = "(none)"

CHIP_COLORS = {
    "human": (ast_viz.HUMAN_TINT, ast_viz.HUMAN_ACCENT),
    "year": (ast_viz.DATE_TINT, ast_viz.DATE_ACCENT),
    "name_date": (ast_viz.DATE_TINT, ast_viz.DATE_ACCENT),
    "object": (ast_viz.OBJECT_TINT, ast_viz.OBJECT_ACCENT),
    "near_object": (ast_viz.NEAR_OBJECT_TINT, ast_viz.NEAR_OBJECT_ACCENT),
    "end": (ast_viz.END_TINT, ast_viz.END_ACCENT),
}

CSS = """
<style>
h1, h2, h3 { font-family: Georgia, 'Times New Roman', serif; }
.mixtec-hero h1 { margin-bottom: 0.1rem; }
.mixtec-hero .subtitle { font-size: 1.05rem; color: #5C544A; margin-bottom: 0.35rem; }
.mixtec-hero .authors { font-size: 0.92rem; color: #5C544A; margin-bottom: 0.6rem; }
.linkrow a {
    display: inline-block; margin: 0 0.45rem 0.35rem 0; padding: 0.16rem 0.7rem;
    border: 1.5px solid #9E2B25; border-radius: 999px; color: #9E2B25;
    text-decoration: none; font-size: 0.88rem; background: #FFFFFF;
}
.linkrow a:hover { background: #9E2B25; color: #FAF6EE; }
.chipbox { margin: 0.3rem 0 0.6rem 0; }
.chip {
    display: inline-block; padding: 0.14rem 0.68rem; margin: 0.16rem 0.32rem 0.16rem 0;
    border-radius: 999px; border: 1.6px solid; font-size: 0.92rem; color: #221D18;
}
.chip .sym { font-family: monospace; font-size: 0.8rem; opacity: 0.72; margin-right: 0.4rem; }
.chip.ghost { border-style: dashed; opacity: 0.68; }
.narration {
    background: #FFFDF6; border: 1px solid #E6DCC8; border-left: 6px solid #9E2B25;
    border-radius: 8px; padding: 1.05rem 1.35rem; margin: 0.4rem 0 0.9rem 0;
    font-family: Georgia, 'Times New Roman', serif; font-size: 1.32rem;
    line-height: 1.55; color: #221D18;
}
.narration .scene-number { color: #9E2B25; font-size: 0.95rem; margin-right: 0.5rem; }
.vbar { width: 0; border-left: 1.5px solid #D9CDB2; height: 170px; margin: 0.5rem auto 0 auto; }
.vbar-results { width: 0; border-left: 1.5px solid #D9CDB2; height: 520px; margin: 0.4rem auto 0 auto; }
.scene-strip { display: flex; gap: 8px; overflow-x: auto; padding: 4px 2px 8px 2px; }
.scene-strip a, .scene-strip span { flex: 0 0 auto; display: block; }
.scene-strip img {
    height: 96px; width: auto; display: block; border-radius: 6px;
    border: 1.5px solid #D9CDB2; background: #FFF;
}
.scene-strip a:hover img { border-color: #9E2B25; box-shadow: 0 0 0 1px #9E2B25; }
.scene-strip a.encoded img { border: 2.5px solid #9E2B25; }
</style>
"""


def default_xml() -> str:
    """XML for the paper's running example, used to seed the XML tab."""
    wedding = presets.PRESETS[0]
    return scenes.specs_to_xml(scenes.ensure_end(wedding["specs"]))


def _apply_preset(preset: dict) -> None:
    """Load a preset and keep the dropdown selection in sync with it."""
    st.session_state.specs = copy.deepcopy(preset["specs"])
    st.session_state.active_preset = preset["title"]
    st.session_state.preset_choice = preset["title"]


def _mark_scene_edited() -> None:
    """The scene diverged from any preset, so clear the dropdown selection."""
    st.session_state.active_preset = None
    st.session_state.preset_choice = None


def init_state() -> None:
    # thumbnails in the scene strip select a scene through the scene query param
    requested = st.query_params.get("scene")
    if requested:
        try:
            _apply_preset(presets.by_key(requested))
            logger.info("Loaded scene from query param: {}", requested)
        except KeyError:
            logger.warning("Unknown scene in query param: {}", requested)
        st.query_params.clear()

    if "specs" not in st.session_state:
        _apply_preset(presets.PRESETS[0])
    if "xml_text" not in st.session_state:
        st.session_state.xml_text = default_xml()


# CALLBACKS
def load_preset() -> None:
    title = st.session_state.preset_choice
    if not title:
        return
    _apply_preset(presets.by_title(title))
    logger.info("Loaded preset: {}", title)


def add_figure() -> None:
    specs = st.session_state.specs
    specs.append(scenes.human_spec(
        st.session_state.fig_gender,
        st.session_state.fig_pose,
        st.session_state.fig_orientation,
    ))
    near = st.session_state.fig_near_custom.strip().replace(" ", "_")
    if not near and st.session_state.fig_near != NONE_OPTION:
        near = st.session_state.fig_near
    if near:
        specs.append(scenes.near_object_spec(near))
    if st.session_state.fig_named:
        specs.append(scenes.name_date_spec(st.session_state.fig_sign, int(st.session_state.fig_number)))
    _mark_scene_edited()


def add_date() -> None:
    specs = st.session_state.specs
    specs.append(scenes.year_spec(st.session_state.date_year_sign, int(st.session_state.date_year_number)))
    if st.session_state.date_has_day:
        specs.append(scenes.name_date_spec(st.session_state.date_day_sign, int(st.session_state.date_day_number)))
    _mark_scene_edited()


def add_object() -> None:
    identity = st.session_state.obj_custom.strip()
    if not identity:
        identity = st.session_state.obj_select
    st.session_state.specs.append(scenes.object_spec(identity))
    _mark_scene_edited()


def add_scene_break() -> None:
    st.session_state.specs.append(scenes.end_spec())
    _mark_scene_edited()


def undo_token() -> None:
    if st.session_state.specs:
        st.session_state.specs.pop()
    _mark_scene_edited()


def clear_scene() -> None:
    st.session_state.specs = []
    _mark_scene_edited()


def send_scene_to_xml() -> None:
    st.session_state.xml_text = scenes.specs_to_xml(scenes.ensure_end(st.session_state.specs))
    st.toast("Scene exported. Open the XML encoding tab to see it.", icon="📜")


def load_xml_into_builder() -> None:
    try:
        st.session_state.specs = scenes.xml_to_specs(st.session_state.xml_text)
        _mark_scene_edited()
        st.toast("XML loaded into the scene composer.", icon="📜")
    except ValueError as exc:
        logger.warning("Could not load XML into the builder: {}", exc)
        st.toast(f"Could not load the XML: {exc}", icon="⚠️")


def restore_paper_xml() -> None:
    st.session_state.xml_text = default_xml()


# RENDER HELPERS
@functools.lru_cache(maxsize=32)
def _image_data_uri(path: str) -> str:
    with open(path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"


def _preset_facsimile(preset: dict) -> dict | None:
    """Resolve a preset's codex facsimile for display, or None if absent."""
    image = preset.get("facsimile")
    if not image:
        return None
    if not image.startswith("http"):
        image = os.path.join(APP_DIR, image)
        if not os.path.exists(image):
            return None
    return {
        "image": image,
        "caption": preset.get("facsimile_caption"),
        "link": preset.get("facsimile_link"),
    }


def scene_strip_html() -> str:
    """A horizontally scrollable strip of codex scene thumbnails.

    Scenes with token encodings come first, framed in red; clicking one loads
    it for interpretation through the scene query param. The rest are shown
    for browsing only, with their dataset link surfaced in the results panel
    once a scene is selected.
    """
    cards = []
    for scene in presets.ATTESTED_SCENES:
        uri = _image_data_uri(os.path.join(APP_DIR, scene["thumb"]))
        label = html.escape(f'Click to interpret: {scene["label"]}')
        cards.append(
            f'<a class="encoded" href="?scene={scene["preset_key"]}" target="_self" '
            f'title="{label}"><img src="{uri}" alt="{label}"/></a>'
        )
    for scene in presets.BROWSE_SCENES:
        uri = _image_data_uri(os.path.join(APP_DIR, scene["thumb"]))
        label = html.escape(scene["label"])
        cards.append(
            f'<span title="{label}"><img src="{uri}" alt="{label}"/></span>'
        )
    return f'<div class="scene-strip">{"".join(cards)}</div>'


def graphviz_chart(dot: str) -> None:
    try:
        st.graphviz_chart(dot, width="stretch")
    except TypeError:
        st.graphviz_chart(dot, use_container_width=True)


def chip_html(spec: dict, ghost: bool = False) -> str:
    tint, accent = CHIP_COLORS[spec["kind"]]
    ghost_class = " ghost" if ghost else ""
    return (
        f'<span class="chip{ghost_class}" style="background:{tint}; border-color:{accent};">'
        f'<span class="sym">{scenes.spec_symbol(spec)}</span>'
        f"{html.escape(scenes.spec_label(spec))}</span>"
    )


def render_chips(specs: list[dict]) -> None:
    chips = [chip_html(spec) for spec in specs]
    if not specs or specs[-1]["kind"] != "end":
        chips.append(chip_html(scenes.end_spec(), ghost=True))
    st.markdown(f'<div class="chipbox">{"".join(chips)}</div>', unsafe_allow_html=True)


NOT_YET_COVERED = (
    "The grammar accepts this scene, but the interpreter does not yet cover "
    "this grouping of figures. One-to-many and many-to-many configurations "
    "are future work in the paper."
)


def render_narration(sentences: list[str]) -> None:
    shown = [
        NOT_YET_COVERED if "<ERROR" in sentence.upper() else sentence
        for sentence in sentences
    ]
    if len(shown) == 1:
        body = html.escape(shown[0])
    else:
        body = "<br>".join(
            f'<span class="scene-number">{i + 1}.</span>{html.escape(sentence)}'
            for i, sentence in enumerate(shown)
        )
    st.markdown(f'<div class="narration">{body}</div>', unsafe_allow_html=True)


def render_scene_outputs(specs: list[dict], show_xml: bool = True, facsimile: dict | None = None) -> None:
    """Parse the specs and show narration, the AST, and the XML encoding."""
    token_list = scenes.specs_to_tokens(scenes.ensure_end(specs))
    try:
        root = parser.Parser()(token_list)
    except parser.ParseError as exc:
        logger.info("Parse error: {}", exc)
        st.error(f"This token sequence is not in the grammar. {exc}")
        st.caption(
            "Every scene needs at least one human figure, a name-date must follow "
            "a year or a figure, and a near-object must follow its figure. The "
            "grammar tab spells out the full rules."
        )
        return

    st.markdown("###### Machine narration")
    render_narration(scenes.narrate(root))

    ast_col, results_bar_col, detail_col = st.columns([3, 0.14, 2], gap="small")
    with ast_col:
        st.markdown("###### Abstract syntax tree, as in Figure 3 of the paper")
        graphviz_chart(ast_viz.to_dot(root))
    with results_bar_col:
        st.markdown('<div class="vbar-results"></div>', unsafe_allow_html=True)
    with detail_col:
        if facsimile:
            st.markdown("###### The scene on the codex page")
            st.image(facsimile["image"], caption=facsimile.get("caption"))
            if facsimile.get("link"):
                st.markdown(f'[View this scene in the dataset]({facsimile["link"]})')
        st.markdown("###### Scene sketch")
        st.markdown(sketch.to_svg(specs), unsafe_allow_html=True)
        st.caption(
            "A schematic of how the glyphs sit on the page: names float by "
            "their figures, personal objects ride with their owners, and red "
            "bands divide scenes."
        )
        if show_xml:
            st.markdown("###### XML scene encoding, as in Figure 2 of the paper")
            st.code(scenes.specs_to_xml(scenes.ensure_end(specs)), language="xml")
        with st.expander("Raw interpreter output"):
            st.code(interpreter.Interpreter()(parser.Parser()(
                scenes.specs_to_tokens(scenes.ensure_end(specs))
            )))
            st.caption(
                "The interpreter emits lowercase clauses joined end to end. The "
                "narration above capitalizes each sentence and adds punctuation."
            )


# PAGE SECTIONS
def render_hero() -> None:
    st.markdown(
        f"""
        <div class="mixtec-hero">
        <h1>Reading Mixtec codices, formally</h1>
        <p class="subtitle">A context free grammar, parser, and interpreter that turn
        encoded scenes from the Codex Zouche-Nuttall into English narration.</p>
        <p class="authors">Christopher Driggers-Ellis · Gabriel Ayoubi · Girish Salunke ·
        Christan Grant — University of Florida Data Studio</p>
        <p class="linkrow">
        <a href="{PAPER_URL}">Paper · ALVR 2026</a>
        <a href="{PAPER_PDF_URL}">PDF</a>
        <a href="{POSTER_URL}">Poster</a>
        <a href="{VIT_DEMO_URL}">Glyph classifier demo</a>
        <a href="{LAB_URL}">UF Data Studio</a>
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown("### About this demo")
        st.markdown(
            "Mixtec codices narrate history through arrangements of glyphs rather "
            "than written sentences. This demo composes a scene as a sequence of "
            "glyph tokens, parses it with the paper's context free grammar, and "
            "interprets the syntax tree into English."
        )
        st.markdown("#### Token legend")
        legend = [
            (scenes.human_spec("Lord", "standing", "right"), "human figure"),
            (scenes.year_spec("Flint", 6), "year glyph"),
            (scenes.name_date_spec("Eagle", 7), "name-date glyph"),
            (scenes.object_spec("house"), "scene object"),
            (scenes.near_object_spec("throne"), "personal object"),
            (scenes.end_spec(), "scene boundary"),
        ]
        for spec, meaning in legend:
            st.markdown(
                f'{chip_html(spec)} <span style="font-size:0.85rem; color:#5C544A;">{meaning}</span>',
                unsafe_allow_html=True,
            )
        st.markdown("#### Links")
        st.markdown(
            f"- [Paper on the ACL Anthology]({PAPER_URL})\n"
            f"- [Poster]({POSTER_URL})\n"
            f"- [Scene and glyph cutouts]({SCENES_DATASET_URL}) from the codex, on Hugging Face\n"
            f"- [Vision-model demo]({VIT_DEMO_URL}) that classifies the glyphs\n"
            f"- [UF Data Studio]({LAB_URL})"
        )


def render_compose_tab() -> None:
    st.markdown(
        "Pick a scene from the codex, load a constructed example, or compose "
        "your own from glyph tokens. The parser and interpreter run on every "
        "change."
    )

    picker_col, bar_col, gallery_col = st.columns([2.4, 0.14, 2.6], gap="small")

    with gallery_col:
        st.markdown("###### Scenes from the codex")
        st.markdown(scene_strip_html(), unsafe_allow_html=True)
        st.caption(
            "Red-framed scenes have token encodings; click one to interpret "
            "it. The rest come from the "
            f"[Zouche-Nuttall dataset]({SCENES_DATASET_URL}) on Hugging Face "
            "and join the encoded set as their readings are curated."
        )

    with bar_col:
        st.markdown('<div class="vbar"></div>', unsafe_allow_html=True)

    with picker_col:
        st.markdown("###### Example scenes")
        st.selectbox(
            "Load an example scene",
            options=[preset["title"] for preset in presets.PRESETS],
            index=None,
            placeholder="Choose a scene…",
            key="preset_choice",
            on_change=load_preset,
            label_visibility="collapsed",
        )
        st.caption(
            "Attested and constructed scenes: weddings, audiences, "
            "sacrifices, combats, and processions. A chosen scene shows its "
            "codex facsimile below when one exists."
        )

    active_facsimile = None
    if st.session_state.active_preset:
        preset = presets.by_title(st.session_state.active_preset)
        st.caption(f'{preset["source"]}')
        st.markdown(preset["blurb"])
        active_facsimile = _preset_facsimile(preset)

    st.markdown("###### Scene tokens, in reading order")
    render_chips(st.session_state.specs)
    if not (st.session_state.specs and st.session_state.specs[-1]["kind"] == "end"):
        st.caption(
            "The dashed end token is the tokenizer's meta-token. It closes the "
            "scene automatically, as described in the README."
        )

    undo_col, clear_col, break_col, xml_col = st.columns([1, 1, 1.4, 1.8])
    undo_col.button("Undo last", on_click=undo_token, disabled=not st.session_state.specs)
    clear_col.button("Clear scene", on_click=clear_scene, disabled=not st.session_state.specs)
    break_col.button("Add scene break", on_click=add_scene_break, disabled=not st.session_state.specs)
    xml_col.button("Export to the XML tab", on_click=send_scene_to_xml, disabled=not st.session_state.specs)

    with st.expander("Add glyph tokens", expanded=False):
        figure_col, date_col, object_col = st.columns(3, gap="large")

        with figure_col:
            st.markdown("Human figure — h")
            st.selectbox("Gender", scenes.GENDERS, key="fig_gender")
            st.selectbox("Pose", scenes.POSES, index=1, key="fig_pose")
            st.selectbox("Facing", scenes.ORIENTATIONS, index=1, key="fig_orientation")
            st.checkbox("Named by a name-date glyph", value=True, key="fig_named")
            number_col, sign_col = st.columns(2)
            number_col.number_input("Number", min_value=1, max_value=13, value=4, key="fig_number")
            sign_col.selectbox("Day sign", scenes.DAY_SIGNS, index=1, key="fig_sign")
            st.selectbox(
                "Personal object nearby (near_obj)",
                [NONE_OPTION] + scenes.NEAR_OBJECT_SUGGESTIONS,
                key="fig_near",
            )
            st.text_input("or another personal object", key="fig_near_custom")
            st.button("Add figure", on_click=add_figure, type="primary")

        with date_col:
            st.markdown("Date — y and nd")
            year_number_col, year_sign_col = st.columns(2)
            year_number_col.number_input("Year number", min_value=1, max_value=13, value=6, key="date_year_number")
            year_sign_col.selectbox("Year bearer", scenes.YEAR_BEARERS, index=3, key="date_year_sign")
            st.caption(
                "Mixtec years take one of four bearer signs: House, Rabbit, Reed, "
                "or Flint."
            )
            st.checkbox("Include a day (a name-date after the year)", value=True, key="date_has_day")
            day_number_col, day_sign_col = st.columns(2)
            day_number_col.number_input("Day number", min_value=1, max_value=13, value=7, key="date_day_number")
            day_sign_col.selectbox("Sign", scenes.DAY_SIGNS, index=14, key="date_day_sign")
            st.button("Add date", on_click=add_date, type="primary")

        with object_col:
            st.markdown("Scene object — obj")
            st.selectbox("Object", scenes.OBJECT_SUGGESTIONS, key="obj_select")
            st.text_input("or another object", key="obj_custom")
            st.caption(
                "A house or table between a seated couple signals a marriage. "
                "Objects apply to the whole scene, unlike personal near-objects."
            )
            st.button("Add object", on_click=add_object, type="primary")

    st.divider()
    if st.session_state.specs:
        render_scene_outputs(st.session_state.specs, facsimile=active_facsimile)
    else:
        st.info("The scene is empty. Load an example above or add glyph tokens.")


def render_xml_tab() -> None:
    st.markdown(
        "The paper parses scenes from an XML encoding of the codex page "
        "(Figure 2). Paste or edit a document here; the same grammar parses it "
        "into an AST and narrates it."
    )
    st.text_area("XML scene encoding", key="xml_text", height=320)

    load_col, restore_col = st.columns([1.4, 1.6])
    load_col.button("Load into the scene composer", on_click=load_xml_into_builder)
    restore_col.button("Restore the paper's example", on_click=restore_paper_xml)

    st.divider()
    try:
        specs = scenes.xml_to_specs(st.session_state.xml_text)
    except ValueError as exc:
        logger.info("XML error: {}", exc)
        st.error(f"{exc}")
        st.caption(
            "The document wraps one or more scene elements. Each scene lists "
            "human, year, name_date, object, and near_object elements in reading "
            "order. Restore the paper's example to see the expected shape."
        )
        return

    render_chips(specs)
    render_scene_outputs(specs, show_xml=False)


def render_grammar_tab() -> None:
    grammar_col, gloss_col = st.columns([2, 3], gap="large")

    with grammar_col:
        st.markdown("#### The context free grammar")
        st.code(GRAMMAR_TEXT, language=None)
        st.markdown(
            "A recursive descent parser consumes the token stream and builds the "
            "abstract syntax tree; each node then interprets itself into English. "
            "The paper implements the same grammar over XML with ANTLR."
        )
        st.markdown("#### Why a name-date is two things")
        st.info(
            "People in the codices are named after their birthday in the 260-day "
            "ritual calendar, a number from 1 to 13 with one of 20 day signs. The "
            "same glyph therefore reads as a date beside a year glyph and as a "
            "personal name beside a human figure. The grammar resolves the "
            "ambiguity from position alone."
        )
        with st.expander("The 260-day calendar"):
            st.markdown(
                "Thirteen numbers cycle against twenty day signs, giving 260 "
                "named days: "
                + ", ".join(scenes.DAY_SIGNS)
                + ". Years take one of the four bearer signs House, Rabbit, "
                "Reed, and Flint, so a date like Year 6 Flint Day 7 Eagle pins a "
                "moment inside a 52-year round."
            )

    with gloss_col:
        st.markdown("#### The six terminal symbols")
        st.markdown(
            """
| Symbol | Glyph | Reading |
|---|---|---|
| h | Human figure | A Lord or Lady, drawn sitting or standing, facing left or right |
| y | Year glyph | The A-O year cartouche with a bearer sign and number |
| nd | Name-date | A calendar glyph: a date beside a year, a name beside a figure |
| obj | Scene object | Toponyms, temples, houses, rivers; property of the whole scene |
| near_obj | Personal object | A throne, weapon, or epithet bound to one figure |
| end | Scene boundary | Meta-token the tokenizer inserts at the end of each scene |
"""
        )
        st.markdown("#### From iconography to narration")
        st.markdown(
            """
| Scene configuration | Interpretation |
|---|---|
| Seated couple, opposite genders, facing, house or table between | X married Y |
| One standing, one seated, facing | Stander consulted the sitter, naming a throne when present |
| Both seated, facing, no object | X communed with Y |
| Both standing, facing, sacrificed animal nearby | X and Y participated in a ritual sacrifice |
| Both standing, facing, weapon or shield nearby | X fought Y |
| Both standing, facing, otherwise | X met Y |
| Three or more standing, one direction | A procession or journey |
| Three or more standing, mixed directions | A gathering |
| Figure without a name-date | A Lord, a Lady |
| Personal object | X with a throne, weapon, torch |
| Scene object elsewhere | The action happened near it |
"""
        )
        st.caption(
            "These conventions come from a century of scholarship on Mixtec "
            "pictorials, including Smith (1973), Pohl (1994), and Boone (2000)."
        )

    with st.expander("Tokenizer conventions the parser relies on"):
        st.markdown(
            "- A name-date follows the year or the human figure it belongs to, "
            "regardless of how the glyphs sit on the page.\n"
            "- A near-object follows its figure and precedes that figure's "
            "name-date.\n"
            "- The tokenizer inserts the end meta-token at each scene boundary, "
            "which corresponds roughly to a sentence.\n"
            "- Objects that relate to several figures at once, such as toponyms, "
            "are general objects rather than near-objects."
        )


def render_about_tab() -> None:
    left_col, right_col = st.columns([3, 2], gap="large")

    with left_col:
        st.markdown("#### Abstract")
        st.markdown(ABSTRACT)
        st.markdown("#### Where this fits")
        st.markdown(
            "The parser is the symbolic half of a larger pipeline. Vision models "
            "classify the glyphs of a facsimile page, the classifications become "
            "the XML scene encoding, and the grammar turns that encoding into "
            "narration."
        )
        graphviz_chart(
            """digraph pipeline {
  rankdir=LR;
  bgcolor="transparent";
  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11,
        fillcolor="#F2EBDC", color="#8A8378", fontcolor="#221D18", margin="0.22,0.12"];
  edge [color="#8A8378"];
  facsimile [label="Codex facsimile"];
  vit [label="Glyph classification\\n(fine-tuned ViTs)"];
  xml [label="XML scene encoding"];
  parse [label="CFG parser → AST", fillcolor="#F6DEDA", color="#9E2B25", penwidth=1.8];
  narrate [label="English narration", fillcolor="#F6DEDA", color="#9E2B25", penwidth=1.8];
  facsimile -> vit -> xml -> parse -> narrate;
}"""
        )
        st.caption(
            "Glyph classification builds on Webber et al. (AmericasNLP 2024) and "
            "Salunke et al. (CHR 2025); this paper contributes the highlighted "
            "symbolic stages. Try the classifiers in the "
            f"[vision-model demo]({VIT_DEMO_URL})."
        )
        st.markdown("#### The source imagery")
        st.markdown(
            "The lab publishes the codex imagery this pipeline reads on "
            "Hugging Face. The "
            f"[Zouche-Nuttall labeled dataset]({SCENES_DATASET_URL}) holds 270 "
            "scene cutouts alongside figure and name-date cutouts, segmented "
            "from British Museum scans; the wedding preset in this demo "
            "displays its scene directly from that dataset. A companion "
            f"[figures dataset]({FIGURES_DATASET_URL}) adds imagery from the "
            "Codices Selden and Vindobonensis."
        )
        st.markdown("#### Limitations the paper acknowledges")
        st.markdown(
            "Codex excerpts are not yet converted into the XML encoding "
            "automatically, so parsing currently requires curated XML. Toponym "
            "interpretation, which can hinge on archaeology and Mixtec-language "
            "wordplay, is left to future, specialized work."
        )

    with right_col:
        st.markdown("#### Cite the paper")
        st.code(BIBTEX, language="bibtex")
        st.markdown("#### Credits")
        st.markdown(
            "Built by the [UF Data Studio](https://ufdatastudio.com) at the "
            "University of Florida. Glyph examples in the paper and poster appear "
            "courtesy of the British Museum, which holds the Codex Zouche-Nuttall."
        )


def render_footer() -> None:
    st.divider()
    logo_paths = [
        os.path.join(APP_DIR, "logos/uflorida_logo.jpeg"),
        os.path.join(APP_DIR, "logos/ufdatastudio-logo.jpeg"),
    ]
    logos = [path for path in logo_paths if os.path.exists(path)]
    if logos:
        columns = st.columns([4, 1, 1, 4])
        for column, path in zip(columns[1:3], logos):
            column.image(path, width=110)
    st.caption(
        "Formal Machine Interpretation for the Semasiographic Mixtec Codices of "
        "Precolonial and Early Colonial Mesoamerica · ALVR 2026 · "
        "University of Florida Data Studio"
    )


def main() -> None:
    st.set_page_config(
        page_title="Mixtec Codex Interpretation Demo",
        page_icon="📜",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(CSS, unsafe_allow_html=True)
    init_state()
    render_hero()
    render_sidebar()

    compose_tab, xml_tab, grammar_tab, about_tab = st.tabs([
        "Interpret a scene",
        "XML encoding",
        "Grammar and semantics",
        "About the paper",
    ])
    with compose_tab:
        render_compose_tab()
    with xml_tab:
        render_xml_tab()
    with grammar_tab:
        render_grammar_tab()
    with about_tab:
        render_about_tab()

    render_footer()


main()
