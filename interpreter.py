# CWDE615
# Interpreter for the parser in parser.py. Check the README for the limit Mixtec Grammar interpreted into text.

import tree_node

class Interpreter():
    def __init__(self, root : tree_node.Start):
        self.root : tree_node.Start = root
    
    def interpret(self) -> str:
        return self.root.interpret()

    def __call__(self) -> str:
        return self.interpret()