# CWDE615
# file for a hierarchy of token types
from tree_node import TreeNode

# ABC for the token classes, which act more like structs, since they have no methods in the current design.
class Token(TreeNode):
    def __init__(self, x, y):
        super().__init__(None, None) # sets first_token to None and children to []
        self.x = x
        self.y = y
        self.children = None # overwrite children to None, signaling that this is a leaf in the AST.
        self.first_token = self
        
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
        

class Year(Token):
    def __init__(self, x, y, symbol, number):
        super().__init__(x, y)
        self.symbol = symbol
        self.number = number

    def interpret(self) -> str:
        return f'{self.number} {self.symbol}' # # Symbol

# TODO: Consider adding am additional level to the hierarchy from which Year and NameDate both inherit.
# Currently no advantage, so not implemented despite the fact they have the same set of attributes
class NameDate(Token):
    def __init__(self, x, y, symbol, number):
        super().__init__(x, y)
        self.symbol = symbol
        self.number = number
    
    def interpret(self) -> str:
        return f'{self.number} {self.symbol}' # # Symbol

# TODO: Consider adding specialized classes for different types of objects and relationships of near_obj tokens
class Obj(Token):
    def __init__(self, x, y, identity):
        super().__init__(x, y)
        self.identity = identity
    
    def interpret(self) -> str:
        return f"{self.identity}" # ObjIdentity

class NearObj(Token):
    def __init__(self, x, y, identity):
        super().__init__(x, y)
        self.identity = identity
    
    def interpret(self) -> str:
        return f'{self.identity}' # NearObjIdentity
    
class End(Token):
    def __init__(self, x, y, sent_id):
        super().__init__(x, y) # set x and y of ABC to -1.
        self.sent_id = sent_id
        self.verbose = True
    
    def interpret(self) -> str:
        if self.verbose:
            return f" |{self.sent_id}| "
        else:
            return ""