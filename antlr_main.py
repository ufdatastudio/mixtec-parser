# --------------------------------------------
# Command-line tool for parsing and interpreting Mixtec codex scenes.
# Supports both visitor-based and legacy interpretation modes.
# Usage:
#   python antlr_main.py "<Year>...</Year> <Human>...</Human> <End/>"
#   python antlr_main.py input.txt
#   python antlr_main.py input.txt --visitor
# --------------------------------------------

import sys
import argparse

# Import ANTLR4 runtime and generated lexer/parser classes
from antlr4 import *
from SceneLexer import SceneLexer     # Tokenizes input stream based on lexer rules in Scene.g4
from SceneParser import SceneParser   # Parses token stream into a parse tree using Scene.g4

# Import visitor-based and fallback interpreters
from scene_interpreter_visitor import SceneInterpreterVisitor  # New visitor-style interpreter
from interpreter import run_interpreter                       

def main():
    # Setup command-line arguments
    parser = argparse.ArgumentParser(description="Scene parser and interpreter")
    
    # Accepts a single optional input argument (can be a file path or direct string)
    parser.add_argument("input", nargs="?", default=None, help="Input string or file")
    
    # Optional flag: use visitor-based interpretation
    parser.add_argument("-v", "--visitor", action="store_true", help="Use visitor-based interpreter")
    
    args = parser.parse_args()

    # -------------
    # Load input
    # -------------
    if args.input is None:
        # If no argument provided, read from standard input (e.g., via piping)
        input_stream = InputStream(sys.stdin.read())
    else:
        try:
            # Try to open the input as a file path
            with open(args.input, 'r') as f:
                input_stream = InputStream(f.read())
        except FileNotFoundError:
            # If the file doesn't exist, treat it as a raw string
            input_stream = InputStream(args.input)

    # -------------
    # Lexing and Parsing
    # -------------
    lexer = SceneLexer(input_stream)                      # Convert raw input to tokens
    token_stream = CommonTokenStream(lexer)               # Stream tokens for the parser
    parser = SceneParser(token_stream)                    # Parse tokens into a parse tree
    tree = parser.s()                                     # Start parsing from the root rule `s`

    # -------------
    # Interpretation
    # -------------
    if args.visitor:
        # If --visitor flag is passed, use the new visitor-style interpreter
        visitor = SceneInterpreterVisitor()
        result = visitor.visit(tree)                      # Recursively walk parse tree and interpret
        print("[Visitor Result]", result)
    else:
        # Use legacy interpreter fallback (manual interpret() methods on tree)
        result = run_interpreter(tree)
        print("[Interpreter Result]", result)

# -------------
# Script Entry Point
# -------------
if __name__ == '__main__':
    main()
