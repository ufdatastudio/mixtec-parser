# Curated scenes for the Streamlit demo.
"""Attested and constructed scenes that showcase the grammar and interpreter.

The first preset is the paper's running example, the marriage statement from
page 26 of the Codex Zouche-Nuttall (obverse). The rest exercise the
interpreter's iconographic conventions one at a time.
"""

import scenes

PRESETS = [
    {
        "key": "wedding",
        "title": "A royal wedding — Lady 9 Eagle marries Lord 6 Alligator",
        "source": "Codex Zouche-Nuttall, page 26 (obverse). The paper's running example, Figures 2 and 3.",
        "facsimile": "assets/czn-p26-marriage.jpg",
        "facsimile_caption": (
            "The scene on page 26 of the Codex Zouche-Nuttall (obverse). "
            "Image courtesy of the British Museum."
        ),
        "blurb": (
            "Two seated figures face one another across a house glyph, the classic "
            "marriage statement of the genealogical sections. The year and day glyphs "
            "that open the scene date the ceremony. Try removing the house: without it "
            "the couple merely communes."
        ),
        "specs": [
            scenes.year_spec("Flint", 6),
            scenes.name_date_spec("Eagle", 7),
            scenes.human_spec("Lady", "sitting", "right"),
            scenes.name_date_spec("Eagle", 9),
            scenes.object_spec("house"),
            scenes.human_spec("Lord", "sitting", "left"),
            scenes.name_date_spec("Alligator", 6),
        ],
    },
    {
        "key": "consultation",
        "title": "An audience — Lord 4 Wind consults Lady 10 Serpent",
        "source": "Constructed example from the repository's test suite.",
        "blurb": (
            "A standing figure faces a seated one, which the interpreter reads as a "
            "consultation. The seated figure holds the authority in the exchange."
        ),
        "specs": [
            scenes.year_spec("House", 5),
            scenes.human_spec("Lord", "standing", "right"),
            scenes.name_date_spec("Wind", 4),
            scenes.human_spec("Lady", "sitting", "left"),
            scenes.name_date_spec("Serpent", 10),
        ],
    },
    {
        "key": "throne",
        "title": "An audience with the ruler on his throne",
        "source": "Constructed example.",
        "blurb": (
            "A near-object belongs to the figure it accompanies. Here the throne "
            "attaches to Lord 4 Wind, so the narration seats him on it while "
            "Lady 10 Serpent consults him."
        ),
        "specs": [
            scenes.human_spec("Lady", "standing", "right"),
            scenes.name_date_spec("Serpent", 10),
            scenes.human_spec("Lord", "sitting", "left"),
            scenes.near_object_spec("throne"),
            scenes.name_date_spec("Wind", 4),
        ],
    },
    {
        "key": "sacrifice",
        "title": "A ritual sacrifice in Year 5 House",
        "source": "Constructed example from the repository's test suite.",
        "blurb": (
            "A sacrificed animal near either standing figure marks the pair as "
            "participants in a ritual sacrifice rather than a meeting."
        ),
        "specs": [
            scenes.year_spec("House", 5),
            scenes.human_spec("Lord", "standing", "right"),
            scenes.near_object_spec("sacrificed_animal"),
            scenes.name_date_spec("Wind", 4),
            scenes.human_spec("Lord", "standing", "left"),
            scenes.name_date_spec("Death", 6),
        ],
    },
    {
        "key": "combat",
        "title": "Combat — Lord 4 Wind fights Lord 6 Death",
        "source": "Constructed example from the repository's test suite.",
        "blurb": (
            "Weapons and shields near two standing figures who face one another turn "
            "the scene into combat. Take the weapons away and the two simply meet."
        ),
        "specs": [
            scenes.year_spec("House", 5),
            scenes.human_spec("Lord", "standing", "right"),
            scenes.near_object_spec("weapon"),
            scenes.name_date_spec("Wind", 4),
            scenes.human_spec("Lord", "standing", "left"),
            scenes.near_object_spec("shield"),
            scenes.name_date_spec("Death", 6),
        ],
    },
    {
        "key": "procession",
        "title": "A procession in Year 1 Reed",
        "source": "Constructed example.",
        "blurb": (
            "Three or more standing figures who share an orientation read as a "
            "procession or journey. Turn one of them around and the scene becomes "
            "a gathering instead."
        ),
        "specs": [
            scenes.year_spec("Reed", 1),
            scenes.human_spec("Lord", "standing", "right"),
            scenes.name_date_spec("Wind", 4),
            scenes.human_spec("Lord", "standing", "right"),
            scenes.name_date_spec("Death", 6),
            scenes.human_spec("Lady", "standing", "right"),
            scenes.name_date_spec("Serpent", 10),
        ],
    },
    {
        "key": "communion",
        "title": "Lady 9 Eagle communes with Lord 6 Alligator",
        "source": "Constructed example.",
        "blurb": (
            "The wedding couple again, but with no house glyph between them. Two "
            "seated figures facing one another commune on equal terms."
        ),
        "specs": [
            scenes.human_spec("Lady", "sitting", "right"),
            scenes.name_date_spec("Eagle", 9),
            scenes.human_spec("Lord", "sitting", "left"),
            scenes.name_date_spec("Alligator", 6),
        ],
    },
    {
        "key": "two_scenes",
        "title": "Two scenes — a wedding, then combat",
        "source": "Constructed example.",
        "blurb": (
            "The end meta-token closes a scene the way a scene boundary does on the "
            "codex page, so one document can narrate several sentences in sequence."
        ),
        "specs": [
            scenes.year_spec("Flint", 6),
            scenes.name_date_spec("Eagle", 7),
            scenes.human_spec("Lady", "sitting", "right"),
            scenes.name_date_spec("Eagle", 9),
            scenes.object_spec("house"),
            scenes.human_spec("Lord", "sitting", "left"),
            scenes.name_date_spec("Alligator", 6),
            scenes.end_spec(),
            scenes.year_spec("House", 5),
            scenes.human_spec("Lord", "standing", "right"),
            scenes.near_object_spec("weapon"),
            scenes.name_date_spec("Wind", 4),
            scenes.human_spec("Lord", "standing", "left"),
            scenes.near_object_spec("shield"),
            scenes.name_date_spec("Death", 6),
        ],
    },
]


def by_title(title: str) -> dict:
    """Return the preset whose title matches, raising KeyError if absent."""
    for preset in PRESETS:
        if preset["title"] == title:
            return preset
    raise KeyError(title)
