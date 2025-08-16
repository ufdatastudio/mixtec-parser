# CWDE615
# file for a hierarchy of token types

from __future__ import annotations

# ABC for the token classes, which act more like structs, since they have no methods in the current design.
class Token:
    def __init__(self, x, y, *args, **kwargs):
        self.x = x
        self.y = y
        
class Human(Token):
    def __init__(self, x, y, gender, pose, orientation):
        super().__init__(x, y)
        self.gender = gender
        self.pose = pose
        self.orientation = orientation
        self.gender_dict = {0 : 'Lord', 1: 'Lady'}
        self.pose_dict = {0 : 'sitting', 1: 'standing'}
        self.orientation_dict = {0: 'left', 1: 'right'}

    # pose and orientation are used by the Human parent to infer what to say about the person.
    # Thus, they are not returned by interpret, which simply says Lord or Lady according to the
    # Humans gender.
    def interpret(self):
        return f'{self.gender_dict[self.gender]}' # Lord/Lady
        
    def to_xml(self) -> str:
        return (
            f'<human x="{self.x}" y="{self.y}" '
            f'gender="{self.gender_dict[self.gender]}" '
            f'pose="{self.pose_dict[self.pose]}" '
            f'orientation="{self.orientation_dict[self.orientation]}"/>'
        )

class Year(Token):
    def __init__(self, x, y, symbol, number):
        super().__init__(x, y)
        self.symbol = symbol
        self.number = number

    def interpret(self) -> str:
        return f'{self.number} {self.symbol}' # # Symbol
    
    def to_xml(self) -> str:
        return (
            f'<year x="{self.x}" y="{self.y}" '
            f'symbol="{self.symbol}" number="{self.number}"/>'
        )

# TODO: Consider adding an additional level to the hierarchy from which Year and NameDate both inherit.
# Currently no advantage, so not implemented despite the fact they have the same set of attributes
class NameDate(Token):
    def __init__(self, x, y, symbol, number):
        super().__init__(x, y)
        self.symbol = symbol
        self.number = number
    
    def interpret(self) -> str:
        return f'{self.number} {self.symbol}' # # Symbol
    
    def to_xml(self) -> str:
        return (
            f'<name_date x="{self.x}" y="{self.y}" '
            f'symbol="{self.symbol}" number="{self.number}"/>'
        )

# TODO: Consider adding specialized classes for different types of objects and relationships of near_obj tokens
class Obj(Token):
    def __init__(self, x, y, identity):
        super().__init__(x, y)
        self.identity = identity
    
    def interpret(self) -> str:
        return f"{self.identity}" # ObjIdentity
    
    def to_xml(self) -> str:
        return (
            f'<object x="{self.x}" y="{self.y}" identity="{self.identity}"/>'
        )

class NearObj(Token):
    def __init__(self, x, y, identity):
        super().__init__(x, y)
        self.identity = identity
    
    def interpret(self) -> str:
        return f'{self.identity}' # NearObjIdentity
    
    def to_xml(self) -> str:
        return (
            f'<near_object x="{self.x}" y="{self.y}" identity="{self.identity}"/>'
        )
    
class End(Token):
    def __init__(self, x, y, sent_id):
        super().__init__(x, y) # set x and y of ABC to -1.
        self.sent_id = sent_id
        self.verbose = False
    
    def interpret(self) -> str:
        if self.verbose:
            return f" |{self.sent_id}|\n"
        else:
            return ""
    
    def to_xml(self) -> str:
        return (
            f'<end x="{self.x}" y="{self.y}" sent_id="{self.sent_id}"/>'
        )