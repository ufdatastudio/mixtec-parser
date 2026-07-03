"""Every demo preset must parse, interpret, and render as an AST."""

import pytest

import ast_viz
import parser
import presets
import scenes


@pytest.mark.parametrize("preset", presets.PRESETS, ids=lambda preset: preset["key"])
def test_preset_parses_and_narrates(preset):
    token_list = scenes.specs_to_tokens(scenes.ensure_end(preset["specs"]))
    root = parser.Parser()(token_list)
    sentences = scenes.narrate(root)
    assert sentences
    assert all(sentence[0].isupper() and sentence.endswith(".") for sentence in sentences)


@pytest.mark.parametrize("preset", presets.PRESETS, ids=lambda preset: preset["key"])
def test_preset_renders_dot(preset):
    token_list = scenes.specs_to_tokens(scenes.ensure_end(preset["specs"]))
    root = parser.Parser()(token_list)
    dot = ast_viz.to_dot(root)
    assert dot.startswith("digraph AST {")
    assert dot.rstrip().endswith("}")


def test_wedding_preset_matches_the_paper_reading():
    preset = presets.by_title("A royal wedding — Lady 9 Eagle marries Lord 6 Alligator")
    token_list = scenes.specs_to_tokens(scenes.ensure_end(preset["specs"]))
    root = parser.Parser()(token_list)
    assert scenes.narrate(root) == [
        "In Year 6 Flint Day 7 Eagle Lady 9 Eagle married Lord 6 Alligator."
    ]


def test_two_scene_preset_narrates_two_sentences():
    preset = presets.by_title("Two scenes — a wedding, then combat")
    token_list = scenes.specs_to_tokens(scenes.ensure_end(preset["specs"]))
    root = parser.Parser()(token_list)
    assert scenes.narrate(root) == [
        "In Year 6 Flint Day 7 Eagle Lady 9 Eagle married Lord 6 Alligator.",
        "In Year 5 House Lord 4 Wind fought Lord 6 Death.",
    ]
