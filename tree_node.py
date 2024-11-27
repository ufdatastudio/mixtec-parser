# CWDE615
# a file for parse tree nodes
from tokens import Token
from abc import ABC, abstractmethod

class TreeNode(ABC):
    def __init__(self, first_token, children : list[object] = None):
        self.children : list[object] = children if children != None else []
        self.first_token : Token = first_token

    def add_children(self, chs):
        for ch in chs:
            self.children.append(ch)
    
    def get_children(self):
        return self.children
    
    def get_token(self):
        return self.first_token
    
    @abstractmethod
    def interpret(self):
        pass
    
class Start(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)

    def interpret(self):
        return None
        
class Sent(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        return None

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
    
