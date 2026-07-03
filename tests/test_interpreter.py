"""Golden interpretation tests for the parser and interpreter."""

import interpreter
import parser
import tokens

LORD = 0
LADY = 1
SITTING = 0
STANDING = 1
LEFT = 0
RIGHT = 1


def interpret_tokens(token_list: list[tokens.Token]) -> str:
    """Parse a token list and interpret the resulting AST."""
    root = parser.Parser()(token_list)
    return interpreter.Interpreter()(root)


def test_consultation_between_standing_and_seated_nobles():
    result = interpret_tokens([
        tokens.Year(0, 0, "House", 5),
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Human(0, 0, LADY, SITTING, LEFT),
        tokens.NameDate(0, 0, "Serpent", 10),
        tokens.End(0, 0, 0),
    ])
    assert result == "in Year 5 House Lord 4 Wind consulted Lady 10 Serpent"


def test_consultation_near_a_house():
    result = interpret_tokens([
        tokens.Year(0, 0, "House", 5),
        tokens.Human(0, 0, LORD, SITTING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Obj(0, 0, "house"),
        tokens.Human(0, 0, LORD, STANDING, LEFT),
        tokens.NearObj(0, 0, "shield"),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.End(0, 0, 0),
    ])
    assert result == "in Year 5 House Lord 6 Death consulted Lord 4 Wind near a house"


def test_ritual_sacrifice():
    result = interpret_tokens([
        tokens.Year(0, 0, "House", 5),
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NearObj(0, 0, "sacrificed_animal"),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Human(0, 0, LORD, STANDING, LEFT),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.End(0, 0, 0),
    ])
    assert result == "in Year 5 House Lord 4 Wind and Lord 6 Death participated in a ritual sacrifice"


def test_combat_with_weapons():
    result = interpret_tokens([
        tokens.Year(0, 0, "House", 5),
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NearObj(0, 0, "weapon"),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Human(0, 0, LORD, STANDING, LEFT),
        tokens.NearObj(0, 0, "shield"),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.End(0, 0, 0),
    ])
    assert result == "in Year 5 House Lord 4 Wind fought Lord 6 Death"


def test_marriage_scene_from_the_paper():
    """Page 26 of the Codex Zouche-Nuttall (obverse), Figures 2 and 3 of the paper."""
    result = interpret_tokens([
        tokens.Year(0, 0, "Flint", 6),
        tokens.NameDate(0, 0, "Eagle", 7),
        tokens.Human(0, 0, LADY, SITTING, RIGHT),
        tokens.NameDate(0, 0, "Eagle", 9),
        tokens.Obj(0, 0, "house"),
        tokens.Human(0, 0, LORD, SITTING, LEFT),
        tokens.NameDate(0, 0, "Alligator", 6),
        tokens.End(0, 0, 0),
    ])
    assert result == "in Year 6 Flint Day 7 Eagle Lady 9 Eagle married Lord 6 Alligator"


def test_throne_consultation_names_the_seat():
    result = interpret_tokens([
        tokens.Human(0, 0, LADY, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Serpent", 10),
        tokens.Human(0, 0, LORD, SITTING, LEFT),
        tokens.NearObj(0, 0, "throne"),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.End(0, 0, 0),
    ])
    assert result == "Lady 10 Serpent consulted Lord 4 Wind sitting on his throne"


def test_communion_between_seated_nobles():
    result = interpret_tokens([
        tokens.Human(0, 0, LADY, SITTING, RIGHT),
        tokens.NameDate(0, 0, "Eagle", 9),
        tokens.Human(0, 0, LORD, SITTING, LEFT),
        tokens.NameDate(0, 0, "Alligator", 6),
        tokens.End(0, 0, 0),
    ])
    assert result == "Lady 9 Eagle communed with Lord 6 Alligator"


def test_meeting_without_weapons():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Human(0, 0, LORD, STANDING, LEFT),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.End(0, 0, 0),
    ])
    assert result == "Lord 4 Wind met Lord 6 Death"


def test_procession_of_standing_figures_facing_the_same_way():
    result = interpret_tokens([
        tokens.Year(0, 0, "Reed", 1),
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.Human(0, 0, LADY, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Serpent", 10),
        tokens.End(0, 0, 0),
    ])
    assert result == (
        "in Year 1 Reed there was a procession or journey including "
        "Lord 4 Wind, Lord 6 Death, and Lady 10 Serpent"
    )


def test_gathering_of_standing_figures_facing_different_ways():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Human(0, 0, LORD, STANDING, LEFT),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.Human(0, 0, LADY, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Serpent", 10),
        tokens.End(0, 0, 0),
    ])
    assert result == "there was a gathering including Lord 4 Wind, Lord 6 Death, and Lady 10 Serpent"


def test_group_with_seated_figures_is_listed_plainly():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Human(0, 0, LORD, SITTING, RIGHT),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.Human(0, 0, LADY, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Serpent", 10),
        tokens.End(0, 0, 0),
    ])
    assert result == "there were Lord 4 Wind, Lord 6 Death, and Lady 10 Serpent"


def test_pair_facing_the_same_direction():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.End(0, 0, 0),
    ])
    assert result == "there was Lord 4 Wind and Lord 6 Death"


def test_pair_facing_the_same_direction_near_an_object():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.Obj(0, 0, "temple"),
        tokens.End(0, 0, 0),
    ])
    assert result == "there was Lord 4 Wind and Lord 6 Death near a temple"


def test_pair_facing_away_from_each_other():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, LEFT),
        tokens.NearObj(0, 0, "shield"),
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.End(0, 0, 0),
    ])
    assert result == "there was a Lord with a shield and Lord 6 Death"


def test_date_tail_with_an_object():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Year(0, 0, "House", 5),
        tokens.Obj(0, 0, "house"),
        tokens.Human(0, 0, LORD, STANDING, LEFT),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.End(0, 0, 0),
    ])
    assert result == "in Year 5 House Lord 4 Wind met Lord 6 Death near a house"


def test_obj_tail_with_a_date():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.Obj(0, 0, "temple"),
        tokens.Year(0, 0, "Reed", 1),
        tokens.Human(0, 0, LORD, STANDING, LEFT),
        tokens.NameDate(0, 0, "Death", 6),
        tokens.End(0, 0, 0),
    ])
    assert result == "in Year 1 Reed Lord 4 Wind met Lord 6 Death near a temple"


def test_single_named_figure():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.End(0, 0, 0),
    ])
    assert result == "there was Lord 4 Wind"


def test_single_anonymous_figure():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.End(0, 0, 0),
    ])
    assert result == "there was a Lord"


def test_single_figure_near_an_object():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.Obj(0, 0, "house"),
        tokens.End(0, 0, 0),
    ])
    assert result == "there was a Lord near a house"


def test_two_scenes_interpret_in_sequence():
    result = interpret_tokens([
        tokens.Human(0, 0, LORD, STANDING, RIGHT),
        tokens.NameDate(0, 0, "Wind", 4),
        tokens.End(0, 0, 0),
        tokens.Human(0, 0, LADY, STANDING, LEFT),
        tokens.NameDate(0, 0, "Serpent", 10),
        tokens.End(0, 0, 1),
    ])
    assert result == "there was Lord 4 Windthere was Lady 10 Serpent"
