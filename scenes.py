# Scene encodings shared by the Streamlit demo.
"""Bridge between the demo UI, the parser tokens, and the paper's XML encoding.

A scene is stored as a list of token specs, plain dictionaries that the
Streamlit session state can hold and edit. Specs convert to the Token objects
the parser consumes (specs_to_tokens), to the XML scene encoding shown in
Figure 2 of the paper (specs_to_xml), and back from XML (xml_to_specs).
"""

import xml.etree.ElementTree as ET

import tokens
import tree_node

# The twenty day signs of the 260-day Mesoamerican ritual calendar in
# canonical order. A number from 1 to 13 pairs with one of these signs to name
# both days and people, which is why the grammar's nd token can be a date or a
# personal name depending on what it attaches to.
DAY_SIGNS = [
    "Alligator", "Wind", "House", "Lizard", "Serpent",
    "Death", "Deer", "Rabbit", "Water", "Dog",
    "Monkey", "Grass", "Reed", "Jaguar", "Eagle",
    "Vulture", "Movement", "Flint", "Rain", "Flower",
]

# The four day signs that can name a year in the Mixtec calendar.
YEAR_BEARERS = ["House", "Rabbit", "Reed", "Flint"]

GENDERS = ["Lord", "Lady"]
POSES = ["sitting", "standing"]
ORIENTATIONS = ["left", "right"]

OBJECT_SUGGESTIONS = ["house", "table", "temple", "town", "river", "incense", "ballcourt"]
NEAR_OBJECT_SUGGESTIONS = ["weapon", "shield", "throne", "sacrificed_animal", "torch", "headdress"]

# Accepted spellings for human attributes. The Lord/male and Lady/female pairs
# let XML produced from the vision-model labels load without edits.
_GENDER_CODES = {"lord": 0, "male": 0, "lady": 1, "female": 1}
_POSE_CODES = {"sitting": 0, "seated": 0, "not_standing": 0, "standing": 1}
_ORIENTATION_CODES = {"left": 0, "right": 1}


def _normalize(value: str, codes: dict[str, int], canonical: list[str], attribute: str) -> str:
    key = str(value).strip().lower()
    if key not in codes:
        options = ", ".join(canonical)
        raise ValueError(f"Unknown {attribute} {value!r}. Expected one of: {options}.")
    return canonical[codes[key]]


# SPEC FACTORIES
def human_spec(gender: str, pose: str, orientation: str, x: int = 0, y: int = 0) -> dict:
    """Build a spec for an h token (a drawn human figure)."""
    return {
        "kind": "human",
        "gender": _normalize(gender, _GENDER_CODES, GENDERS, "gender"),
        "pose": _normalize(pose, _POSE_CODES, POSES, "pose"),
        "orientation": _normalize(orientation, _ORIENTATION_CODES, ORIENTATIONS, "orientation"),
        "x": x,
        "y": y,
    }


def year_spec(symbol: str, number: int, x: int = 0, y: int = 0) -> dict:
    """Build a spec for a y token (a year glyph)."""
    return {"kind": "year", "symbol": str(symbol), "number": int(number), "x": x, "y": y}


def name_date_spec(symbol: str, number: int, x: int = 0, y: int = 0) -> dict:
    """Build a spec for an nd token (a name-date glyph)."""
    return {"kind": "name_date", "symbol": str(symbol), "number": int(number), "x": x, "y": y}


def object_spec(identity: str, x: int = 0, y: int = 0) -> dict:
    """Build a spec for an obj token (a general drawn object)."""
    return {"kind": "object", "identity": str(identity), "x": x, "y": y}


def near_object_spec(identity: str, x: int = 0, y: int = 0) -> dict:
    """Build a spec for a near_obj token (an object tied to one figure)."""
    return {"kind": "near_object", "identity": str(identity), "x": x, "y": y}


def end_spec() -> dict:
    """Build a spec for the end meta-token that closes a scene."""
    return {"kind": "end"}


def ensure_end(specs: list[dict]) -> list[dict]:
    """Return a copy of specs with the closing end meta-token appended.

    The README notes that the tokenizer, not the artist, inserts the end of
    sentence token. The demo follows the same contract so users never have to
    place it by hand.
    """
    if specs and specs[-1]["kind"] == "end":
        return list(specs)
    return list(specs) + [end_spec()]


# SPEC -> TOKEN OBJECTS
def specs_to_tokens(specs: list[dict]) -> list[tokens.Token]:
    """Construct fresh Token objects for the parser from a list of specs."""
    result: list[tokens.Token] = []
    sent_id = 0

    for spec in specs:
        kind = spec.get("kind")
        x = int(spec.get("x", 0))
        y = int(spec.get("y", 0))

        if kind == "human":
            result.append(tokens.Human(
                x, y,
                _GENDER_CODES[spec["gender"].lower()],
                _POSE_CODES[spec["pose"].lower()],
                _ORIENTATION_CODES[spec["orientation"].lower()],
            ))
        elif kind == "year":
            result.append(tokens.Year(x, y, spec["symbol"], int(spec["number"])))
        elif kind == "name_date":
            result.append(tokens.NameDate(x, y, spec["symbol"], int(spec["number"])))
        elif kind == "object":
            result.append(tokens.Obj(x, y, spec["identity"]))
        elif kind == "near_object":
            result.append(tokens.NearObj(x, y, spec["identity"]))
        elif kind == "end":
            result.append(tokens.End(x, y, sent_id))
            sent_id += 1
        else:
            raise ValueError(f"Unknown token kind {kind!r}.")

    return result


# SPEC LABELS FOR THE UI
def spec_symbol(spec: dict) -> str:
    """Return the grammar's terminal symbol for a spec (h, y, nd, obj, near_obj, end)."""
    symbols = {
        "human": "h",
        "year": "y",
        "name_date": "nd",
        "object": "obj",
        "near_object": "near_obj",
        "end": "end",
    }
    return symbols[spec["kind"]]


def spec_label(spec: dict) -> str:
    """Return a short human-readable label for a spec."""
    kind = spec["kind"]
    if kind == "human":
        return f'{spec["gender"]} · {spec["pose"]} · facing {spec["orientation"]}'
    if kind == "year":
        return f'Year {spec["number"]} {spec["symbol"]}'
    if kind == "name_date":
        return f'{spec["number"]} {spec["symbol"]}'
    if kind in ("object", "near_object"):
        return spec["identity"]
    return "scene break"


# SPEC <-> XML (the encoding from Figure 2 of the paper)
def specs_to_xml(specs: list[dict]) -> str:
    """Serialize specs into the XML scene encoding used by the paper."""
    document = ET.Element("document")
    scene = None

    for spec in specs:
        kind = spec["kind"]
        if kind == "end":
            scene = None
            continue
        if scene is None:
            scene = ET.SubElement(document, "scene")

        x = str(spec.get("x", 0))
        y = str(spec.get("y", 0))

        if kind == "human":
            ET.SubElement(scene, "human", {
                "x": x, "y": y,
                "gender": spec["gender"],
                "pose": spec["pose"],
                "orientation": spec["orientation"],
            })
        elif kind == "year":
            ET.SubElement(scene, "year", {
                "x": x, "y": y,
                "symbol": spec["symbol"],
                "number": str(spec["number"]),
            })
        elif kind == "name_date":
            ET.SubElement(scene, "name_date", {
                "x": x, "y": y,
                "symbol": spec["symbol"],
                "number": str(spec["number"]),
            })
        elif kind == "object":
            ET.SubElement(scene, "object", {"x": x, "y": y, "identity": spec["identity"]})
        elif kind == "near_object":
            ET.SubElement(scene, "near_object", {"x": x, "y": y, "identity": spec["identity"]})
        else:
            raise ValueError(f"Unknown token kind {kind!r}.")

    ET.indent(document, space="  ")
    return ET.tostring(document, encoding="unicode", xml_declaration=True)


def _require(element: ET.Element, attribute: str) -> str:
    value = element.get(attribute)
    if value is None:
        raise ValueError(f"<{element.tag}> is missing the {attribute!r} attribute.")
    return value


def _int_attr(element: ET.Element, attribute: str, default: int | None = None) -> int:
    value = element.get(attribute)
    if value is None:
        if default is None:
            raise ValueError(f"<{element.tag}> is missing the {attribute!r} attribute.")
        return default
    try:
        return int(float(value))
    except ValueError:
        raise ValueError(f"<{element.tag}> has a non-numeric {attribute!r} attribute: {value!r}.") from None


def xml_to_specs(xml_text: str) -> list[dict]:
    """Parse the paper's XML scene encoding into a list of token specs.

    A closing end spec is appended after each scene, mirroring the tokenizer
    contract described in the README.

    Raises:
        ValueError: If the XML is malformed or uses unknown elements or
            attribute values.
    """
    try:
        document = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        raise ValueError(f"The XML is not well formed: {exc}.") from None

    if document.tag != "document":
        raise ValueError(f"The root element must be <document>, found <{document.tag}>.")

    scenes = list(document)
    if not scenes:
        raise ValueError("The document contains no <scene> elements.")

    specs: list[dict] = []
    for scene in scenes:
        if scene.tag != "scene":
            raise ValueError(f"Expected <scene> elements inside <document>, found <{scene.tag}>.")
        for element in scene:
            specs.append(_element_to_spec(element))
        specs.append(end_spec())

    return specs


def _element_to_spec(element: ET.Element) -> dict:
    x = _int_attr(element, "x", 0)
    y = _int_attr(element, "y", 0)
    tag = element.tag

    if tag == "human":
        return human_spec(
            _require(element, "gender"),
            _require(element, "pose"),
            _require(element, "orientation"),
            x, y,
        )
    if tag == "year":
        return year_spec(_require(element, "symbol"), _int_attr(element, "number"), x, y)
    if tag == "name_date":
        return name_date_spec(_require(element, "symbol"), _int_attr(element, "number"), x, y)
    if tag == "object":
        return object_spec(_require(element, "identity"), x, y)
    if tag in ("near_object", "near_obj"):
        return near_object_spec(_require(element, "identity"), x, y)

    raise ValueError(
        f"Unknown element <{tag}>. Expected human, year, name_date, object, or near_object."
    )


# NARRATION
def narrate(root: tree_node.Start) -> list[str]:
    """Interpret each sentence under the Start node as a polished English line.

    The interpreter itself returns lowercase clauses joined end to end. For
    display, each Sent child is interpreted on its own, capitalized, and
    given a final period.
    """
    sentences: list[str] = []
    for child in root.get_children():
        if isinstance(child, tree_node.Sent):
            text = child.interpret().strip()
            if text:
                sentences.append(text[0].upper() + text[1:] + ".")
    return sentences
