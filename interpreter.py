# CWDE615
import tree_node
#TODO: Add a new interpreter that interprets the XML into natural language. We are currently just transcribing the XML from the tokens.

class Interpreter():
    """
        Interpreter for the parser in parser.py. 
        Check the README for the limited Mixtec Grammar interpreted into text.

        An interpreter walks the parse tree and translates it into a human-readable sentence 
        that expresses the meaning of the scene.
    """

    def interpret(self, root : tree_node.Start) -> str:
        return root.interpret()

    def __call__(self, root : tree_node.Start) -> str:
        return self.interpret(root)
    
    
def run_interpreter(tree):
    # Fallback placeholder — returns raw tree string
    return tree.toStringTree()