"""Every demo preset must parse, interpret, and render as an AST."""

import os

import pytest

import ast_viz
import parser
import presets
import scenes

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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


def test_attested_titles_mark_presets_with_scenes():
    assert presets.ATTESTED_TITLES == {
        "A royal wedding — Lady 9 Eagle marries Lord 6 Alligator"
    }
    assert presets.ATTESTED_TITLES <= {preset["title"] for preset in presets.PRESETS}


def test_attested_scenes_reference_real_presets_and_thumbnails():
    for scene in presets.ATTESTED_SCENES:
        preset = presets.by_key(scene["preset_key"])
        assert preset["specs"]
        assert os.path.exists(os.path.join(REPO_DIR, scene["thumb"]))
        assert scene["label"]
        assert scene["link"].startswith("https://huggingface.co/datasets/")


def test_illustrative_scenes_reference_real_presets_and_thumbnails():
    for key, scene in presets.ILLUSTRATIVE_SCENES.items():
        assert presets.by_key(key)
        assert os.path.exists(os.path.join(REPO_DIR, scene["thumb"]))
        assert scene["label"]
        assert scene["link"].startswith("https://huggingface.co/datasets/")
    # attested and illustrative sets never overlap
    attested = {scene["preset_key"] for scene in presets.ATTESTED_SCENES}
    assert not attested & set(presets.ILLUSTRATIVE_SCENES)


def test_browse_scenes_have_thumbnails_and_links():
    for scene in presets.BROWSE_SCENES:
        assert os.path.exists(os.path.join(REPO_DIR, scene["thumb"]))
        assert scene["label"]
        assert scene["link"].startswith("https://huggingface.co/datasets/")
        assert scene["link"].endswith(scene["file"])


def test_main_branch_test2_scene_is_a_preset():
    preset = presets.by_key("consult_house")
    token_list = scenes.specs_to_tokens(scenes.ensure_end(preset["specs"]))
    root = parser.Parser()(token_list)
    assert scenes.narrate(root) == [
        "In Year 5 House Lord 6 Death consulted Lord 4 Wind near a house."
    ]


def test_two_scene_preset_narrates_two_sentences():
    preset = presets.by_title("Two scenes — a wedding, then combat")
    token_list = scenes.specs_to_tokens(scenes.ensure_end(preset["specs"]))
    root = parser.Parser()(token_list)
    assert scenes.narrate(root) == [
        "In Year 6 Flint Day 7 Eagle Lady 9 Eagle married Lord 6 Alligator.",
        "In Year 5 House Lord 4 Wind fought Lord 6 Death.",
    ]
