"""Tests for the scene spec, XML, and narration bridge used by the demo."""

import pytest

import interpreter
import parser
import scenes

# The XML scene encoding from Figure 2 of the paper.
PAPER_XML = """<?xml version="1.0" encoding="UTF-8"?>
<document>
  <scene>
    <year x="0" y="0" symbol="Flint" number="6" />
    <name_date x="0" y="0" symbol="Eagle" number="7" />
    <human x="0" y="0" gender="Lady" pose="sitting" orientation="right" />
    <name_date x="0" y="0" symbol="Eagle" number="9" />
    <object x="0" y="0" identity="house" />
    <human x="0" y="0" gender="Lord" pose="sitting" orientation="left" />
    <name_date x="0" y="0" symbol="Alligator" number="6" />
  </scene>
</document>
"""


def test_paper_xml_interprets_to_the_marriage_sentence():
    specs = scenes.xml_to_specs(PAPER_XML)
    root = parser.Parser()(scenes.specs_to_tokens(specs))
    result = interpreter.Interpreter()(root)
    assert result == "in Year 6 Flint Day 7 Eagle Lady 9 Eagle married Lord 6 Alligator"


def test_xml_to_specs_appends_an_end_after_each_scene():
    specs = scenes.xml_to_specs(PAPER_XML)
    assert len(specs) == 8
    assert specs[-1] == scenes.end_spec()


def test_xml_round_trip_preserves_specs():
    specs = scenes.xml_to_specs(PAPER_XML)
    assert scenes.xml_to_specs(scenes.specs_to_xml(specs)) == specs


def test_specs_to_xml_splits_scenes_on_end():
    specs = [
        scenes.human_spec("Lord", "standing", "right"),
        scenes.end_spec(),
        scenes.human_spec("Lady", "sitting", "left"),
    ]
    xml_text = scenes.specs_to_xml(specs)
    assert xml_text.count("<scene>") == 2

    round_tripped = scenes.xml_to_specs(xml_text)
    assert [spec["kind"] for spec in round_tripped] == ["human", "end", "human", "end"]


def test_vision_model_labels_are_accepted():
    spec = scenes.human_spec("female", "not_standing", "left")
    assert spec["gender"] == "Lady"
    assert spec["pose"] == "sitting"


def test_malformed_xml_raises_value_error():
    with pytest.raises(ValueError):
        scenes.xml_to_specs("<document><scene>")


def test_unknown_element_raises_value_error():
    xml_text = '<document><scene><temple x="0" y="0" /></scene></document>'
    with pytest.raises(ValueError):
        scenes.xml_to_specs(xml_text)


def test_missing_attribute_raises_value_error():
    xml_text = '<document><scene><human x="0" y="0" gender="Lady" pose="sitting" /></scene></document>'
    with pytest.raises(ValueError):
        scenes.xml_to_specs(xml_text)


def test_unknown_gender_raises_value_error():
    with pytest.raises(ValueError):
        scenes.human_spec("duke", "sitting", "left")


def test_ensure_end_appends_exactly_one_end():
    specs = [scenes.human_spec("Lord", "standing", "right")]
    ended = scenes.ensure_end(specs)
    assert [spec["kind"] for spec in ended] == ["human", "end"]
    assert scenes.ensure_end(ended) == ended
    assert [spec["kind"] for spec in specs] == ["human"]


def test_narrate_capitalizes_and_punctuates_each_sentence():
    specs = scenes.xml_to_specs(PAPER_XML)
    root = parser.Parser()(scenes.specs_to_tokens(specs))
    assert scenes.narrate(root) == [
        "In Year 6 Flint Day 7 Eagle Lady 9 Eagle married Lord 6 Alligator."
    ]


def test_narrate_returns_one_line_per_scene():
    specs = [
        scenes.human_spec("Lord", "standing", "right"),
        scenes.name_date_spec("Wind", 4),
        scenes.end_spec(),
        scenes.human_spec("Lady", "standing", "left"),
        scenes.name_date_spec("Serpent", 10),
        scenes.end_spec(),
    ]
    root = parser.Parser()(scenes.specs_to_tokens(specs))
    assert scenes.narrate(root) == [
        "There was Lord 4 Wind.",
        "There was Lady 10 Serpent.",
    ]


def test_spec_labels_and_symbols():
    assert scenes.spec_symbol(scenes.human_spec("Lady", "sitting", "right")) == "h"
    assert scenes.spec_label(scenes.human_spec("Lady", "sitting", "right")) == "Lady · sitting · facing right"
    assert scenes.spec_label(scenes.year_spec("Flint", 6)) == "Year 6 Flint"
    assert scenes.spec_label(scenes.name_date_spec("Eagle", 7)) == "7 Eagle"
    assert scenes.spec_label(scenes.near_object_spec("throne")) == "throne"
    assert scenes.spec_symbol(scenes.end_spec()) == "end"


def test_specs_to_tokens_rejects_unknown_kind():
    with pytest.raises(ValueError):
        scenes.specs_to_tokens([{"kind": "temple"}])
