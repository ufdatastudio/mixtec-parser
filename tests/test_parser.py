"""Structural and error-handling tests for the recursive descent parser."""

import pytest

import parser
import tokens
import tree_node

LORD = 0
LADY = 1
SITTING = 0
STANDING = 1
LEFT = 0
RIGHT = 1


def test_ast_structure_of_the_marriage_scene():
    root = parser.Parser()([
        tokens.Year(0, 0, "Flint", 6),
        tokens.NameDate(0, 0, "Eagle", 7),
        tokens.Human(0, 0, LADY, SITTING, RIGHT),
        tokens.NameDate(0, 0, "Eagle", 9),
        tokens.Obj(0, 0, "house"),
        tokens.Human(0, 0, LORD, SITTING, LEFT),
        tokens.NameDate(0, 0, "Alligator", 6),
        tokens.End(0, 0, 0),
    ])

    assert isinstance(root, tree_node.Start)
    sent, end = root.get_children()
    assert isinstance(sent, tree_node.Sent)
    assert isinstance(end, tokens.End)

    date, clause = sent.get_children()
    assert isinstance(date, tree_node.Date)
    assert isinstance(clause, tree_node.Clause)
    assert [type(child) for child in date.get_children()] == [tokens.Year, tokens.NameDate]

    clause_f, obj_tail = clause.get_children()
    assert isinstance(clause_f, tree_node.ClauseF)
    assert isinstance(obj_tail, tree_node.ObjTail)


def test_multiple_scenes_number_their_end_tokens():
    root = parser.Parser()([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.End(0, 0, 0),
        tokens.Human(0, 0, LADY, STANDING, LEFT),
        tokens.End(0, 0, 0),
    ])

    ends = [child for child in root.get_children() if isinstance(child, tokens.End)]
    assert [end.sent_id for end in ends] == [0, 1]


def test_empty_input_raises_parse_error():
    with pytest.raises(parser.ParseError):
        parser.Parser()([])


def test_missing_end_token_raises_parse_error():
    with pytest.raises(parser.ParseError):
        parser.Parser()([
            tokens.Year(0, 0, "House", 5),
            tokens.Human(0, 0, LORD, STANDING, RIGHT),
        ])


def test_scene_cannot_start_with_a_name_date():
    with pytest.raises(parser.ParseError):
        parser.Parser()([
            tokens.NameDate(0, 0, "Wind", 4),
            tokens.End(0, 0, 0),
        ])


def test_object_alone_is_not_a_sentence():
    with pytest.raises(parser.ParseError):
        parser.Parser()([
            tokens.Obj(0, 0, "house"),
            tokens.End(0, 0, 0),
        ])


def test_year_alone_is_not_a_sentence():
    with pytest.raises(parser.ParseError):
        parser.Parser()([
            tokens.Year(0, 0, "House", 5),
            tokens.End(0, 0, 0),
        ])
