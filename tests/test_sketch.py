"""Tests for the schematic scene sketch renderer."""

import pytest

import presets
import scenes
import sketch


@pytest.mark.parametrize("preset", presets.PRESETS, ids=lambda preset: preset["key"])
def test_every_preset_sketches(preset):
    svg = sketch.to_svg(scenes.ensure_end(preset["specs"]))
    assert svg.startswith("<svg")
    assert svg.endswith("</svg>")


def test_wedding_sketch_labels_the_scene():
    preset = presets.by_title("A royal wedding — Lady 9 Eagle marries Lord 6 Alligator")
    svg = sketch.to_svg(preset["specs"])
    assert "Year 6 Flint" in svg
    assert "Lady 9 Eagle" in svg
    assert "Lord 6 Alligator" in svg
    assert "house" in svg


def test_unnamed_figure_is_labeled_anonymously():
    svg = sketch.to_svg([scenes.human_spec("Lord", "standing", "right")])
    assert "a Lord" in svg


def test_trailing_end_is_not_drawn_but_breaks_are():
    single = sketch.to_svg(scenes.ensure_end([scenes.human_spec("Lord", "standing", "right")]))
    assert 'class="divider"' not in single

    two_scenes = sketch.to_svg([
        scenes.human_spec("Lord", "standing", "right"),
        scenes.end_spec(),
        scenes.human_spec("Lady", "sitting", "left"),
    ])
    assert two_scenes.count('class="divider"') == 1


def test_empty_specs_render_nothing():
    assert sketch.to_svg([]) == ""
    assert sketch.to_svg([scenes.end_spec()]) == ""


def test_identity_text_is_escaped():
    svg = sketch.to_svg([scenes.object_spec("<script>alert(1)</script>")])
    assert "<script>" not in svg
    assert "&lt;script&gt;" in svg


def test_long_identity_wraps_to_two_lines():
    svg = sketch.to_svg([
        scenes.human_spec("Lord", "standing", "right"),
        scenes.near_object_spec("sacrificed_animal"),
    ])
    assert "sacrific…" not in svg
    assert "animal" in svg
