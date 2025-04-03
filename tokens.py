
# CWDE615
# file for a hierarchy of token types

# ABC for the token classes, which act more like structs, since they have no methods in the current design.
class Token:
    def __init__(self, *args, **kwargs):
        from tree_node import TreeNode  # Lazy import to break circular import
        self.__class__ = type(self.__class__.__name__, (TreeNode,), dict(self.__class__.__dict__))
        super().__init__(*args, **kwargs)

        
class Human(Token):
    def __init__(self, x, y, gender, pose, orientation):
        super().__init__(x, y)
        self.gender = gender
        self.pose = pose
        self.orientation = orientation
        self.gender_dict = {0 : 'Lord', 1: 'Lady'}
        self.pose_dict = {0 : 'sitting', 1: 'standing'}
        self.orientation_dict = {0: 'left', 1: 'right'}

    def interpret(self):
        return f'{self.gender_dict[self.gender]}'

    def to_xml(self) -> str:
        return f"""<Human>
    <gender>{self.gender_dict[self.gender]}</gender>
    <pose>{self.pose_dict[self.pose]}</pose>
    <orientation>{self.orientation_dict[self.orientation]}</orientation>
</Human>"""

class Year(Token):
    def __init__(self, x, y, symbol, number):
        super().__init__(x, y)
        self.symbol = symbol
        self.number = number

    def interpret(self) -> str:
        return f'{self.number} {self.symbol}'

    def to_xml(self) -> str:
        return f"""<Year>
    <symbol>{self.symbol}</symbol>
    <number>{self.number}</number>
</Year>"""

class NameDate(Token):
    def __init__(self, x, y, symbol, number):
        super().__init__(x, y)
        self.symbol = symbol
        self.number = number
    
    def interpret(self) -> str:
        return f'{self.number} {self.symbol}'

    def to_xml(self) -> str:
        return f"""<NameDate>
    <symbol>{self.symbol}</symbol>
    <number>{self.number}</number>
</NameDate>"""

class Obj(Token):
    def __init__(self, x, y, identity):
        super().__init__(x, y)
        self.identity = identity
    
    def interpret(self) -> str:
        return f"{self.identity}"

    def to_xml(self) -> str:
        return f"<Obj>{self.identity}</Obj>"

class NearObj(Token):
    def __init__(self, x, y, identity):
        super().__init__(x, y)
        self.identity = identity
    
    def interpret(self) -> str:
        return f'{self.identity}'

    def to_xml(self) -> str:
        return f"<NearObj>{self.identity}</NearObj>"

class End(Token):
    def __init__(self, x, y, sent_id):
        super().__init__(x, y)
        self.sent_id = sent_id
        self.verbose = False
    
    def interpret(self) -> str:
        if self.verbose:
            return f" |{self.sent_id}|\n"
        else:
            return ""

    def to_xml(self) -> str:
        return "<End/>"
