# CWDE615
# a file for parse tree nodes
import tokens
from abc import ABC, abstractmethod

class TreeNode(ABC):
    def __init__(self, first_token, children : list[object] = None):
        self.children : list[object] = children if children != None else []
        self.first_token : tokens.Token = first_token

    def add_children(self, chs):
        for ch in chs:
            self.children.append(ch)
    
    def get_children(self):
        return self.children
    
    def get_token(self):
        return self.first_token
    
    def is_first_token_type(self, exp : type):
        return type(self.first_token) == exp
     
    @abstractmethod
    def interpret(self) -> str:
        pass
    
class Start(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)

    def interpret(self) -> str:
        sentence_list : list[str] = []
        # the Start symbol should have an alternating sequence of Sent and end children.
        for sent_or_end in self.children():
            sentence_list.append(sent_or_end.interpret())

        return "".join(sentence_list)
        
class Sent(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        sentence_list : list[str] = []

        if self.is_first_token_type(tokens.Human):
            return self.children[0].interpret() # Clause
       
        if self.is_first_token_type(tokens.Obj) or self.is_first_token_type(tokens.Year):
            sentence_list.append(self.children[0].interpret()) # obj || Date
            
            if len(self.children) > 2:
                sentence_list.append(self.children[1].interpret()) # Date || obj
                sentence_list.append(self.children[2].interpret()) # Clause || Clause
            else:
                sentence_list.append(self.children[1].interpret()) # Clause || Clause
            
        return "".join(sentence_list)

class Clause(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        i = 0
        human_list = []

        while self.children[i].is_first_token_type(tokens.Human):
            human_list.append(self.children[i].interpret())
            i += 1

        obj_tail = None
        date_tail = None

        # get the possible Obj_tail and Date_tail. These may have their own human_list to consider. 
        if i < len(self.children) and self.children[i].is_first_token_type(tokens.Obj):
            obj_tail = self.children[i].interpret()
        elif i < len(self.children) and self.children[i].is_first_token_type(tokens.Year):
            date_tail = self.children[i].interpret()
        
        # do something with those data.
        return "PLACEHOLDER"
            

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
        
        year_string : str = self.first_token.interpret() # interpret the year

        if len(self.children) > 1:
            date_string : str = self.children[1].interpret() # nd

            return "".join(["in Year ", year_string, " Day ", date_string])
        else:
            return "".join(["in Year ", year_string])


class ClauseF(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        return None

class NearDate(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self) -> str:
        near_obj_string : str = self.first_token.interpret() # near_obj

        # somewhat bends the rules of the interpretation interface by inserting a meta-character '$'
        # to represent that the two pieces of information provided are not meant to be in sequence.
        if len(self.children) > 1:
            name_date_string : str = self.children[1].interpret() # nd
        
            return "$".join([near_obj_string, name_date_string])
        else:
            return near_obj_string
            
    
