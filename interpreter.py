# CWDE615
# Interpreter for the parser in parser.py. Check the README for the limit Mixtec Grammar interpreted into text.

import tree_node

class Interpreter():
    
    def interpret(self, root : tree_node.Start) -> str:
        return root.interpret()

    def __call__(self, root : tree_node.Start) -> str:
        return self.interpret(root)
    
    
def run_interpreter(tree):
    # Fallback placeholder — returns raw tree string
    return tree.toStringTree()