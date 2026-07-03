# Schematic scene sketches for the Streamlit demo.
"""Draw a token sequence the way its glyphs sit on a codex page, as inline SVG.

Figures face one another, personal objects ride with their figures, name
glyphs float beside their owners, and red bands divide scenes the way red
guide lines divide the codices. The sketch is a diagram, not a facsimile: it
shows the spatial reading that the tokenizer flattens into a sequence.
"""

import html

from ast_viz import (
    DATE_ACCENT,
    DATE_TINT,
    END_ACCENT,
    HUMAN_ACCENT,
    NEAR_OBJECT_ACCENT,
    NEAR_OBJECT_TINT,
    OBJECT_ACCENT,
    OBJECT_TINT,
)

SKIN = "#D9A05B"
INK = "#221D18"
LABEL_INK = "#4A4238"
BASELINE_COLOR = "#9E2B25"

BASE = 180  # y of the ground line the glyphs stand on
GAP = 16  # horizontal space between glyph slots


def _text(x: float, y: float, content: str, size: float = 10.5, fill: str = LABEL_INK, weight: str = "normal") -> str:
    return (
        f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="middle" font-size="{size}" '
        f'font-family="Helvetica, Arial, sans-serif" font-weight="{weight}" fill="{fill}">'
        f"{html.escape(content)}</text>"
    )


def _figure_body(gender: str, pose: str) -> str:
    """Body parts for a figure drawn facing right, feet at (0, BASE)."""
    parts: list[str] = []
    seated = pose == "sitting"
    head_y = BASE - (78 if seated else 108)

    if seated:
        # folded legs, torso, pointing arm
        parts.append(f'<rect x="-16" y="{BASE - 26}" width="36" height="26" rx="8" fill="{HUMAN_ACCENT}"/>')
        parts.append(f'<rect x="-13" y="{BASE - 66}" width="26" height="42" rx="6" fill="{HUMAN_ACCENT}"/>')
        parts.append(f'<rect x="8" y="{BASE - 56}" width="20" height="7" rx="3.5" fill="{SKIN}"/>')
        parts.append(f'<path d="M28,{BASE - 56} l9,3.5 l-9,3.5 z" fill="{SKIN}"/>')
    else:
        if gender == "Lady":
            # ankle-length dress over the legs
            parts.append(f'<path d="M-13,{BASE - 96} h26 l7,91 h-40 z" fill="{HUMAN_ACCENT}"/>')
        else:
            parts.append(f'<rect x="-8" y="{BASE - 46}" width="7" height="46" fill="{SKIN}"/>')
            parts.append(f'<rect x="3" y="{BASE - 46}" width="7" height="46" fill="{SKIN}"/>')
            parts.append(f'<rect x="-13" y="{BASE - 96}" width="26" height="52" rx="6" fill="{HUMAN_ACCENT}"/>')
        parts.append(f'<rect x="-11" y="{BASE - 5}" width="13" height="5" fill="{SKIN}"/>')
        parts.append(f'<rect x="2" y="{BASE - 5}" width="13" height="5" fill="{SKIN}"/>')
        parts.append(f'<path d="M15,{BASE - 5} l8,2.5 l-8,2.5 z" fill="{SKIN}"/>')
        parts.append(f'<rect x="10" y="{BASE - 88}" width="22" height="7" rx="3.5" fill="{SKIN}"/>')
        parts.append(f'<path d="M32,{BASE - 88} l9,3.5 l-9,3.5 z" fill="{SKIN}"/>')

    # head, nose, hair
    parts.append(f'<circle cx="4" cy="{head_y}" r="11" fill="{SKIN}"/>')
    parts.append(f'<path d="M14,{head_y - 3} l8,4 l-8,4 z" fill="{SKIN}"/>')
    parts.append(f'<ellipse cx="3" cy="{head_y - 8}" rx="12" ry="6" fill="{INK}"/>')
    if gender == "Lady":
        # long braid down the back
        parts.append(f'<rect x="-17" y="{head_y - 6}" width="6" height="20" rx="3" fill="{INK}"/>')
    else:
        # small feather crest
        parts.append(f'<path d="M-2,{head_y - 12} l5,-9 l5,9 z" fill="{DATE_ACCENT}"/>')

    return "".join(parts)


def _glyph_disc(x: float, y: float, number: int) -> str:
    return (
        f'<circle cx="{x:.0f}" cy="{y:.0f}" r="11" fill="{DATE_TINT}" '
        f'stroke="{DATE_ACCENT}" stroke-width="2"/>'
        + _text(x, y + 4, str(number), size=11, fill=INK, weight="bold")
    )


def _wrap_identity(identity: str, limit: int = 10) -> list[str]:
    """Split an identity like sacrificed_animal into at most two short lines."""
    words = identity.replace("_", " ").split() or [identity]
    lines: list[str] = []
    for word in words:
        if lines and len(lines[-1]) + 1 + len(word) <= limit:
            lines[-1] = lines[-1] + " " + word
        else:
            lines.append(word if len(word) <= limit else word[: limit - 1] + "…")
    return lines[:2]


def _labeled_box(x: float, y: float, identity: str, tint: str, accent: str) -> str:
    """A rounded box centered at (x, y) with the identity text inside."""
    lines = _wrap_identity(identity)
    widest = max(len(line) for line in lines)
    width = max(42.0, widest * 5.6 + 14)
    height = 24.0 if len(lines) == 1 else 36.0
    parts = [
        f'<rect x="{x - width / 2:.0f}" y="{y - height / 2:.0f}" width="{width:.0f}" '
        f'height="{height:.0f}" rx="5" fill="{tint}" stroke="{accent}" stroke-width="1.5"/>'
    ]
    if len(lines) == 1:
        parts.append(_text(x, y + 3.5, lines[0], size=8.5, fill=INK))
    else:
        parts.append(_text(x, y - 2, lines[0], size=8.5, fill=INK))
        parts.append(_text(x, y + 9, lines[1], size=8.5, fill=INK))
    return "".join(parts)


def _object_pictogram(x: float, identity: str) -> str:
    """A pictogram for a scene object, centered at x on the ground line."""
    if identity == "house":
        return (
            f'<rect x="{x - 30:.0f}" y="{BASE - 14}" width="60" height="14" fill="#D8B98A" stroke="#B08D57"/>'
            f'<rect x="{x - 22:.0f}" y="{BASE - 40}" width="44" height="26" fill="{OBJECT_TINT}" stroke="{OBJECT_ACCENT}" stroke-width="1.5"/>'
            f'<path d="M{x - 34:.0f},{BASE - 40} L{x:.0f},{BASE - 64} L{x + 34:.0f},{BASE - 40} z" fill="{HUMAN_ACCENT}"/>'
        )
    if identity == "table":
        return (
            f'<rect x="{x - 27:.0f}" y="{BASE - 40}" width="54" height="9" rx="3" fill="{HUMAN_ACCENT}"/>'
            f'<rect x="{x - 22:.0f}" y="{BASE - 31}" width="7" height="31" fill="#B08D57"/>'
            f'<rect x="{x + 15:.0f}" y="{BASE - 31}" width="7" height="31" fill="#B08D57"/>'
        )
    return _labeled_box(x, BASE - 34, identity, OBJECT_TINT, OBJECT_ACCENT)


def to_svg(specs: list[dict]) -> str:
    """Render specs as a schematic SVG strip of the scene.

    A trailing end spec is not drawn; scene breaks between scenes appear as
    red divider bands.
    """
    drawn = list(specs)
    while drawn and drawn[-1]["kind"] == "end":
        drawn.pop()
    if not drawn:
        return ""

    body: list[str] = []
    cursor = 14.0
    figure: dict | None = None  # where the last figure stands, for attachments

    for spec in drawn:
        kind = spec["kind"]

        if kind == "human":
            facing = 1 if spec["orientation"] == "right" else -1
            half = 36.0
            cx = cursor + half
            transform = f'translate({cx:.0f},0)' if facing == 1 else f'translate({cx:.0f},0) scale(-1,1)'
            body.append(f'<g class="figure" transform="{transform}">{_figure_body(spec["gender"], spec["pose"])}</g>')
            # anonymous until a name-date attaches
            body.append(_text(cx, BASE + 16, f'a {spec["gender"]}'))
            figure = {
                "cx": cx,
                "facing": facing,
                "pose": spec["pose"],
                "gender": spec["gender"],
                "label_index": len(body) - 1,
            }
            cursor = cx + half

        elif kind == "year":
            half = 42.0
            cx = cursor + half
            body.append(
                f'<g class="year">'
                f'<circle cx="{cx:.0f}" cy="{BASE - 62}" r="16" fill="none" stroke="{HUMAN_ACCENT}" stroke-width="3"/>'
                f'<path d="M{cx - 17:.0f},{BASE - 50} L{cx:.0f},{BASE - 92} L{cx + 17:.0f},{BASE - 50}" '
                f'fill="none" stroke="{DATE_ACCENT}" stroke-width="3" stroke-linejoin="round"/>'
                f"{_glyph_disc(cx + 24, BASE - 88, int(spec['number']))}"
                f"{_text(cx, BASE + 16, 'Year ' + str(spec['number']) + ' ' + str(spec['symbol']))}"
                f"</g>"
            )
            cursor = cx + half + 12
            figure = None

        elif kind == "name_date":
            if figure is not None:
                # the figure's name floats behind its head
                x = figure["cx"] - figure["facing"] * 30
                y = BASE - (92 if figure["pose"] == "sitting" else 120)
                body.append(f'<g class="name">{_glyph_disc(x, y, int(spec["number"]))}</g>')
                body[figure["label_index"]] = _text(
                    figure["cx"], BASE + 16,
                    f'{figure["gender"]} {spec["number"]} {spec["symbol"]}',
                )
            else:
                # a day date beside the year
                half = 34.0
                cx = cursor + half
                body.append(
                    f'<g class="day">{_glyph_disc(cx, BASE - 64, int(spec["number"]))}'
                    f"{_text(cx, BASE + 16, str(spec['number']) + ' ' + str(spec['symbol']))}</g>"
                )
                cursor = cx + half

        elif kind == "near_object":
            if figure is not None:
                # held or worn on the side the figure faces
                x = figure["cx"] + figure["facing"] * 46
                y = BASE - (44 if figure["pose"] == "sitting" else 58)
                cursor = max(cursor, x + 30)
            else:
                # grammatically out of place, but sketch it anyway so users see it
                x = cursor + 30
                y = BASE - 28
                cursor = x + 30
            body.append(
                f'<g class="near-object">'
                f'{_labeled_box(x, y, str(spec["identity"]), NEAR_OBJECT_TINT, NEAR_OBJECT_ACCENT)}'
                f"</g>"
            )

        elif kind == "object":
            half = 44.0
            cx = cursor + half
            body.append(
                f'<g class="object">{_object_pictogram(cx, str(spec["identity"]))}'
                f"{_text(cx, BASE + 16, str(spec['identity']))}</g>"
            )
            cursor = cx + half
            figure = None

        elif kind == "end":
            cx = cursor + 16
            body.append(
                f'<g class="divider">'
                f'<rect x="{cx - 4:.0f}" y="30" width="8" height="{BASE - 22}" fill="{HUMAN_ACCENT}" opacity="0.75"/>'
                f"{_text(cx, BASE + 16, 'end', size=9, fill=END_ACCENT)}"
                f"</g>"
            )
            cursor = cx + 16
            figure = None

        cursor += GAP

    width = cursor + 6
    ground = (
        f'<line x1="8" y1="{BASE}" x2="{width - 8:.0f}" y2="{BASE}" '
        f'stroke="{BASELINE_COLOR}" stroke-width="2" opacity="0.35"/>'
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 26 {width:.0f} 178" '
        f'width="100%" style="max-width:{width * 1.6:.0f}px" role="img" '
        f'aria-label="Schematic sketch of the scene">'
        f"{ground}{''.join(body)}</svg>"
    )
