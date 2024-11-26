# CWDE615
# a file for parse tree nodes
from tokens import Token
from abc import ABC, abstractmethod

class TreeNode(ABC):
    def __init__(self, first_token : Token, children : list[object] = None):
        self.t : Token = first_token
        self.children : list[object] = children if children != None else []

    def add_children(self, chs):
        for ch in chs:
            self.children.append(ch)

    def get_token_type(self):
        type(self.t)
    
    def get_children(self):
        return self.children
    
    def get_token(self):
        return self.t
    
    @abstractmethod
    def interpret(self):
        pass
    
class Start(TreeNode):
    def __init__(self, token, children = None):
        super().__init__(token, children)

    def interpret(self):
        for sent in self.children:
            return self.children.interpret()
        
class Sent(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        None

class Clause(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        return None

class DateTail(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        return None

class ObjTail(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        return None

class Date(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        return None

class ClauseF(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        return None

class NearDate(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        return None
    
