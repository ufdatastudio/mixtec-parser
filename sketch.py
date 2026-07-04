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


BONE = "#EDE6D6"
GREEN = NEAR_OBJECT_ACCENT
TEAL = OBJECT_ACCENT
RED = "#9E2B25"


def _sign_icon(sign: str) -> str:
    """A simplified pictogram of a day sign, drawn in a box from -12 to 12."""
    key = str(sign).strip().lower()

    if key == "alligator":
        return (
            f'<path d="M-10,6 L-10,-1 L-2,-5 L11,-2 L0,1 Z" fill="{GREEN}" stroke="{INK}" stroke-width="0.8"/>'
            f'<path d="M-10,6 L6,4 L0,8 Z" fill="{GREEN}" stroke="{INK}" stroke-width="0.8"/>'
            f'<path d="M0,1 L3,3 L5,1 L7,3 L9,0" stroke="#FFF" stroke-width="1.2" fill="none"/>'
            f'<circle cx="-5" cy="-1.5" r="1.5" fill="{INK}"/>'
        )
    if key == "wind":
        return (
            f'<circle cx="-3" cy="0" r="7" fill="{SKIN}" stroke="{INK}" stroke-width="0.8"/>'
            f'<path d="M3,-3 L12,1 L3,5 Q6,1 3,-3 Z" fill="{RED}" stroke="{INK}" stroke-width="0.8"/>'
            f'<circle cx="-5" cy="-2" r="1.5" fill="{INK}"/>'
        )
    if key == "house":
        return (
            f'<path d="M-11,-1 L0,-9 L11,-1 Z" fill="{RED}" stroke="{INK}" stroke-width="0.8"/>'
            f'<rect x="-8" y="-1" width="16" height="9" fill="{BONE}" stroke="{INK}" stroke-width="0.8"/>'
            f'<rect x="-2.5" y="2" width="5" height="6" fill="{INK}"/>'
        )
    if key == "lizard":
        return (
            f'<path d="M-10,9 Q-6,2 -1,0 Q6,-3 8,-8" stroke="{GREEN}" stroke-width="3" fill="none" stroke-linecap="round"/>'
            f'<circle cx="8.5" cy="-8.5" r="2.4" fill="{GREEN}"/>'
            f'<path d="M-4,2 l-3,3 M2,-1 l3,2.5" stroke="{GREEN}" stroke-width="2" stroke-linecap="round"/>'
        )
    if key == "serpent":
        return (
            f'<path d="M-9,7 Q-12,0 -5,-2 Q2,-4 1,1 Q0,5 5,4" fill="none" stroke="{GREEN}" stroke-width="3" stroke-linecap="round"/>'
            f'<circle cx="7" cy="3" r="2.6" fill="{GREEN}"/>'
            f'<path d="M9,3 l3.5,1.5 M9,3 l3,-2" stroke="{RED}" stroke-width="1.2"/>'
        )
    if key == "death":
        return (
            f'<circle cx="0" cy="-2" r="7.5" fill="{BONE}" stroke="{INK}" stroke-width="0.8"/>'
            f'<circle cx="-3" cy="-4" r="1.8" fill="{INK}"/><circle cx="3" cy="-4" r="1.8" fill="{INK}"/>'
            f'<path d="M0,-1.5 l-1.5,2.6 h3 Z" fill="{INK}"/>'
            f'<rect x="-4.5" y="4.5" width="9" height="4" fill="{BONE}" stroke="{INK}" stroke-width="0.8"/>'
            f'<path d="M-1.5,4.5 v4 M1.5,4.5 v4" stroke="{INK}" stroke-width="0.9"/>'
        )
    if key == "deer":
        return (
            f'<ellipse cx="0" cy="2" rx="6" ry="5.5" fill="{SKIN}" stroke="{INK}" stroke-width="0.8"/>'
            f'<path d="M-2,-3 L-5,-11 M-2.5,-5 L-8,-8 M2,-3 L5,-11 M2.5,-5 L8,-8" stroke="{INK}" stroke-width="1.5"/>'
            f'<circle cx="-2" cy="0.5" r="1.4" fill="{INK}"/><circle cx="4.5" cy="4" r="1.3" fill="{INK}"/>'
        )
    if key == "rabbit":
        return (
            f'<ellipse cx="-3" cy="-6" rx="2.2" ry="6" fill="{SKIN}" stroke="{INK}" stroke-width="0.8"/>'
            f'<ellipse cx="3.5" cy="-6" rx="2.2" ry="6" fill="{SKIN}" stroke="{INK}" stroke-width="0.8"/>'
            f'<circle cx="0" cy="4" r="6" fill="{SKIN}" stroke="{INK}" stroke-width="0.8"/>'
            f'<circle cx="-2" cy="2.5" r="1.4" fill="{INK}"/><circle cx="4.5" cy="5" r="1.2" fill="{INK}"/>'
        )
    if key == "water":
        return (
            f'<path d="M-11,3 Q-6,-2 0,3 Q6,8 11,3" stroke="{TEAL}" stroke-width="2.6" fill="none"/>'
            f'<path d="M-11,8 Q-6,3 0,8 Q6,13 11,8" stroke="{TEAL}" stroke-width="2.6" fill="none"/>'
            f'<circle cx="-4" cy="-6" r="2" fill="{TEAL}"/><circle cx="4" cy="-8" r="2" fill="{TEAL}"/>'
        )
    if key == "dog":
        return (
            f'<circle cx="0.5" cy="0" r="6.5" fill="{SKIN}" stroke="{INK}" stroke-width="0.8"/>'
            f'<path d="M-5.5,-5 Q-9.5,1 -5,4 Z" fill="{INK}"/>'
            f'<circle cx="-1" cy="-1.5" r="1.5" fill="{INK}"/><circle cx="6" cy="1" r="1.7" fill="{INK}"/>'
        )
    if key == "monkey":
        return (
            f'<circle cx="-7.5" cy="0" r="2.8" fill="{SKIN}" stroke="{INK}" stroke-width="0.8"/>'
            f'<circle cx="7.5" cy="0" r="2.8" fill="{SKIN}" stroke="{INK}" stroke-width="0.8"/>'
            f'<circle cx="0" cy="0" r="6" fill="{SKIN}" stroke="{INK}" stroke-width="0.8"/>'
            f'<path d="M1,-6 Q2,-11 6,-9" stroke="{INK}" stroke-width="1.5" fill="none"/>'
            f'<circle cx="-2" cy="-1.5" r="1.3" fill="{INK}"/><circle cx="2.5" cy="-1.5" r="1.3" fill="{INK}"/>'
        )
    if key == "grass":
        return (
            f'<path d="M0,9 C0,1 -1,-3 -3,-9 M0,9 C1,2 3,-2 6,-8 M0,9 C-2,3 -6,0 -10,-3 '
            f'M0,9 C2,4 7,1 10,-1" stroke="{GREEN}" stroke-width="1.8" fill="none" stroke-linecap="round"/>'
            f'<ellipse cx="0" cy="9.5" rx="5" ry="2" fill="{SKIN}" stroke="{INK}" stroke-width="0.7"/>'
        )
    if key == "reed":
        return (
            f'<rect x="-8" y="-8" width="3" height="17" fill="{DATE_ACCENT}" stroke="{INK}" stroke-width="0.6"/>'
            f'<rect x="-1.5" y="-11" width="3" height="20" fill="{DATE_ACCENT}" stroke="{INK}" stroke-width="0.6"/>'
            f'<rect x="5" y="-8" width="3" height="17" fill="{DATE_ACCENT}" stroke="{INK}" stroke-width="0.6"/>'
            f'<path d="M-6.5,-8 l1.5,-4 l1.5,4 Z M0,-11 l1.5,-4 l1.5,4 Z M6.5,-8 l1.5,-4 l1.5,4 Z" fill="{GREEN}"/>'
        )
    if key == "jaguar":
        return (
            f'<path d="M-6,-4 l-2.5,-4.5 l4.5,1.5 Z M6,-4 l2.5,-4.5 l-4.5,1.5 Z" fill="{DATE_ACCENT}" stroke="{INK}" stroke-width="0.7"/>'
            f'<circle cx="0" cy="0" r="7" fill="{DATE_ACCENT}" stroke="{INK}" stroke-width="0.8"/>'
            f'<circle cx="-3" cy="-1" r="1.2" fill="{INK}"/><circle cx="2.5" cy="-3" r="1.2" fill="{INK}"/>'
            f'<circle cx="1.5" cy="3.5" r="1.2" fill="{INK}"/><circle cx="-1" cy="6" r="1" fill="{INK}"/>'
        )
    if key == "eagle":
        return (
            f'<circle cx="-1" cy="0" r="6.5" fill="{BONE}" stroke="{INK}" stroke-width="0.8"/>'
            f'<path d="M4.5,-1.5 Q11.5,-0.5 9.5,4 Q6,4 3.5,1.5 Z" fill="{DATE_ACCENT}" stroke="{INK}" stroke-width="0.8"/>'
            f'<path d="M-6,-4 Q-8,-10 -3,-8 M-2,-6 Q-3,-11 2,-9" stroke="{INK}" stroke-width="1.4" fill="none"/>'
            f'<circle cx="-2.5" cy="-1.5" r="1.6" fill="{INK}"/>'
        )
    if key == "vulture":
        return (
            f'<circle cx="-1" cy="0" r="6.5" fill="{RED}" stroke="{INK}" stroke-width="0.8"/>'
            f'<path d="M4.5,-2.5 Q12,-1.5 10,3 Q6,3 3.5,0.5 Z" fill="{BONE}" stroke="{INK}" stroke-width="0.8"/>'
            f'<circle cx="-2.5" cy="-2" r="2" fill="#FFF" stroke="{INK}" stroke-width="0.7"/>'
            f'<circle cx="-2.5" cy="-2" r="0.9" fill="{INK}"/>'
        )
    if key == "movement":
        return (
            f'<path d="M-8,-9 Q1,0 -8,9" stroke="{RED}" stroke-width="3.2" fill="none" stroke-linecap="round"/>'
            f'<path d="M8,-9 Q-1,0 8,9" stroke="{DATE_ACCENT}" stroke-width="3.2" fill="none" stroke-linecap="round"/>'
            f'<circle cx="0" cy="0" r="2.2" fill="{INK}"/>'
        )
    if key == "flint":
        return (
            f'<path d="M0,-11 C5.5,-7 5.5,7 0,11 C-5.5,7 -5.5,-7 0,-11 Z" fill="{BONE}" stroke="{INK}" stroke-width="0.9"/>'
            f'<path d="M0,-11 C5.5,-7 5.5,7 0,11 Z" fill="{RED}"/>'
        )
    if key == "rain":
        return (
            f'<path d="M-9,0 a4,4 0 0 1 4,-5 a5,5 0 0 1 9.5,0.5 a3.5,3.5 0 0 1 1.5,6.5 Z" '
            f'fill="{OBJECT_TINT}" stroke="{TEAL}" stroke-width="1.2"/>'
            f'<path d="M-6,4 l1.6,3.4 a1.7,1.7 0 1 1 -3.2,0 Z" fill="{TEAL}"/>'
            f'<path d="M0,4 l1.6,3.4 a1.7,1.7 0 1 1 -3.2,0 Z" fill="{TEAL}"/>'
            f'<path d="M6,4 l1.6,3.4 a1.7,1.7 0 1 1 -3.2,0 Z" fill="{TEAL}"/>'
        )
    if key == "flower":
        return (
            f'<circle cx="0" cy="-5.5" r="3.2" fill="{RED}" stroke="{INK}" stroke-width="0.7"/>'
            f'<circle cx="0" cy="5.5" r="3.2" fill="{RED}" stroke="{INK}" stroke-width="0.7"/>'
            f'<circle cx="-5.5" cy="0" r="3.2" fill="{RED}" stroke="{INK}" stroke-width="0.7"/>'
            f'<circle cx="5.5" cy="0" r="3.2" fill="{RED}" stroke="{INK}" stroke-width="0.7"/>'
            f'<circle cx="0" cy="0" r="2.8" fill="{DATE_ACCENT}" stroke="{INK}" stroke-width="0.7"/>'
        )

    # unknown sign: fall back to its initial so custom spellings still render
    initial = key[:1].upper() if key else "?"
    return _text(0, 4.5, initial, size=13, fill=INK, weight="bold")


def _glyph_medallion(x: float, y: float, number: int, sign: str) -> str:
    """A day-sign medallion: the sign pictogram with a number badge."""
    return (
        f'<g class="sign" data-sign="{html.escape(str(sign).strip().lower())}" '
        f'transform="translate({x:.0f},{y:.0f})">'
        f'<circle cx="0" cy="0" r="15" fill="{DATE_TINT}" stroke="{DATE_ACCENT}" stroke-width="2"/>'
        f'<g transform="scale(0.78)">{_sign_icon(sign)}</g>'
        f'<circle cx="-13" cy="-11" r="7" fill="#FFFDF6" stroke="{DATE_ACCENT}" stroke-width="1.4"/>'
        f'{_text(-13, -7.5, str(number), size=9, fill=INK, weight="bold")}'
        f"</g>"
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
            half = 46.0
            cx = cursor + half
            body.append(
                f'<g class="year">'
                f'<circle cx="{cx - 8:.0f}" cy="{BASE - 58}" r="16" fill="none" stroke="{HUMAN_ACCENT}" stroke-width="3"/>'
                f'<path d="M{cx - 25:.0f},{BASE - 46} L{cx - 8:.0f},{BASE - 88} L{cx + 9:.0f},{BASE - 46}" '
                f'fill="none" stroke="{DATE_ACCENT}" stroke-width="3" stroke-linejoin="round"/>'
                f"{_glyph_medallion(cx + 26, BASE - 84, int(spec['number']), str(spec['symbol']))}"
                f"{_text(cx, BASE + 16, 'Year ' + str(spec['number']) + ' ' + str(spec['symbol']))}"
                f"</g>"
            )
            cursor = cx + half + 10
            figure = None

        elif kind == "name_date":
            if figure is not None:
                # the figure's name floats behind its head
                x = figure["cx"] - figure["facing"] * 30
                y = BASE - (94 if figure["pose"] == "sitting" else 122)
                body.append(
                    f'<g class="name">'
                    f'{_glyph_medallion(x, y, int(spec["number"]), str(spec["symbol"]))}'
                    f"</g>"
                )
                body[figure["label_index"]] = _text(
                    figure["cx"], BASE + 16,
                    f'{figure["gender"]} {spec["number"]} {spec["symbol"]}',
                )
            else:
                # a day date beside the year
                half = 38.0
                cx = cursor + half
                body.append(
                    f'<g class="day">'
                    f'{_glyph_medallion(cx, BASE - 66, int(spec["number"]), str(spec["symbol"]))}'
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
