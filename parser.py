# CWDE615
# Parser for a limited Mixtec Grammar. Check the README for this grammar.
import tokens
import tree_node

class Parser():
    def __init__(self, tks : list[tokens.Token]):
        self.tks = tks
        self.tks.reverse() # reverse tks to make it a stack and allow easy pop via List's pop method.

    # HELPERS
    @staticmethod
    def match(exp: tokens.Token, cand : tokens.Token):
        assert type(cand) == type(exp)

    def consume(self, exp : tokens.Token):
        top : tokens.Token = self.tks[-1]
        self.match(exp, top)
        self.tks.pop()
        return top

    def next_token_type(self, token_type):
        return type(self.tks[-1]) == token_type
    
    def next_token(self):
        return self.tks[-1]

    # RECURSIVE DESCENT FUNCTIONS
    def start(self):
        children : list[tree_node.TreeNode] = []

        first_token = self.next_token()

        while len(self.tks) > 0:
            children.append(self.sent())
            self.consume(tokens.End)
        
        return tree_node.Start(first_token, children)

    def sent(self):
        pass

    # PARSE FUNCTIONS
    def __call__(self) -> tree_node.Start:
        return self.start()
    
    def __call__(self, tks : list[tokens.Token]) -> tree_node.Start:
        self.tks = tks
        self.tks.reverse()
        return self.start()
            