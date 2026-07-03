# Mixtec Parser

This repo contains a parser and interpreter for a limited grammar intended for Mixtec codices, together with a Streamlit demo that narrates encoded scenes in English.
It is the companion code for the ALVR 2026 paper [Formal Machine Interpretation for the Semasiographic Mixtec Codices of Precolonial and Early Colonial Mesoamerica](https://aclanthology.org/2026.alvr-main.20/).

## Streamlit demo

The demo composes a scene as a sequence of glyph tokens, parses it with the grammar below, renders the abstract syntax tree, and interprets it into English.
It also reads and writes the XML scene encoding used in the paper (Figure 2), and ships with attested and constructed example scenes, starting with the marriage of Lady 9 Eagle and Lord 6 Alligator from page 26 of the Codex Zouche-Nuttall.

Run it with [uv](https://docs.astral.sh/uv/):

    uv sync
    uv run streamlit run app.py

The demo code lives in `app.py` (interface), `scenes.py` (token specs and the XML encoding), `ast_viz.py` (syntax tree rendering), `sketch.py` (schematic scene drawings), and `presets.py` (example scenes).
The paper's pipeline is `parser.py` (recursive descent parser over `tokens.py`) and `tree_node.py` plus `interpreter.py` (AST nodes that interpret themselves).
The codex imagery behind the scenes lives in the lab's [Zouche-Nuttall labeled dataset](https://huggingface.co/datasets/ufdatastudio/mixtec-zouche-nuttall-british-museum) on Hugging Face, which the demo links and displays; images appear courtesy of the British Museum.

## Tests

    uv run python -m pytest

## Context Free Grammar (CFG):

    S = (Sent end)+
    Sent = Clause | obj (Date Clause | Clause) | Date (obj Clause | Clause)
    Clause = Clause_f+ (Date_tail | Obj_tail | ɛ)
    Date_tail = Date (obj Clause_f+ | Clause_f+ | ɛ)
    Obj_tail = obj (Date Clause_f+ | Clause_f+ | ɛ)
    Date = y (nd | ɛ)
    Clause_f = h ( nd | Near_date | ɛ )
    Near_date = near_obj (nd | ɛ)

## Terminal Symbols (Tokens)

    h = human figures

    y = year symbol

    nd = name-date symbol. Represents a name when associated with a human figure and a date when associated with a year

    obj = a drawn object that is not a person, year, or name-date and that is not associated with an h token (see near_obj). Examples include typonyms, tables, incense, ballcourts, temples, cities, etc.

    near_obj = Object that is note a year/name-date but still associated with a specific person, such as a weapon, head dress, torch, throne, epithet, umbilical cord, etc. A near_obj has a possessive or prepositional relationship with the associated h token. For example, a person's epithet belongs to them; a person sits on a throne; a person holds a torch. Saying that a person is "at" a place is an exception to the near_obj association because typonyms apply to everyone in the scene. More generally, objects that would have any sort of prepositional relationship to multiple human figures in a scene should be considered general objects and handled at interpretation time.

    end = end of sentence token

## Notes About the Tokenizer

    The parser in this repository expects the following additional functions to be completed at the tokenization step.

    - nd associated with years are always put after them in tokenized data regarless of how they are drawn. Ditto for nd associated with human figures, representing their names.

    - near_obj tokens are always placed after the h token they are associated with during tokenization but before any nd that might be associated with that person.

    - Tokenizer inserts the end of sentence token, which is purely a meta-token, at the end of each scene, which should correspond roughly to sentences.

## Citation

    @inproceedings{driggers-ellis-etal-2026-formal,
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
    }
