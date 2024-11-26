# CWDE615
# file for a hierarchy of token types
from abc import ABC

# ABC for the token classes, which act more like structs, since they have no methods in the current design.
class Token(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Human(Token):
    def __init__(self, x, y, gender, pose, orientation):
        super().__init__(x, y)
        self.gender = gender
        self.pose = pose
        self.orientation = orientation

class Year(Token):
    def __init__(self, x, y, symbol, number):
        super().__init__(x, y)
        self.symbol = symbol
        self.number = number

# TODO: Consider adding a second level to the hierarchy from which Year and NameDate both inherit.
# Currently no advantage, so not implemented despite the fact they have the same set of attributes
class NameDate(Token):
    def __init__(self, x, y, symbol, number):
        super().__init__(x, y)
        self.symbol = symbol
        self.number = number

# TODO: Consider adding specialized classes for different types of objects and relationships of near_obj tokens
class Obj(Token):
    def __init__(self, x, y, identity):
        super().__init__(x, y)
        self.identity = identity

class NearObj(Token):
    def __init__(self, x, y, identity):
        super().__init__(x, y)
        self.identity = identity
    
class End(Token):
    def __init__(self, x, y, sent_id):
        super().__init__(x, y) # set x and y of ABC to -1.
        self.sent_id = sent_id