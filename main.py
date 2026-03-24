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
from antlr.SceneInterpreterVisitor import SceneInterpreterVisitor
from antlr.SceneLexer import SceneLexer     # Tokenizes input stream based on lexer rules in Scene.g4
from antlr.SceneParser import SceneParser   # Parses token stream into a parse tree using Scene.g4
from antlr.TokenConvertor import TokenConvertor   

import tokens as tokens   
# pyright: reportShadowedImports=false
import recursive_descent.parser as p
import recursive_descent.interpreter as interpreter         

def parseScenes() -> str:
    # Setup command-line arguments
    parser = argparse.ArgumentParser(description="Scene parser and interpreter")
    
    # Accepts a single optional input argument (can be a file path or direct string)
    parser.add_argument("input", nargs="?", default=None, help="Input string or file")
    
    # Optional flag: use recursive descent parser
    parser.add_argument("-rd", "--recursiveDescent", action="store_true", help="Use recursive descent parser")
    
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
    token_stream.fill()                                   # Tokenize the full input now

    # DEBUG: Uncomment this code to debug lexer output
    """print("[DEBUG] Tokens:")
    for token in token_stream.tokens:
        print(f"Type: {token.type}, Text: {token.text}")"""

    # -------------
    # Interpretation
    # -------------
    if args.recursiveDescent:
        # If --recursiveDescent flag is passed, use the recursive descent parser
        token_list : list[tokens.Token] = []
        for token in token_stream.tokens[:-1]:
            if token.type == 11:
                 token_list.append(tokens.End(0,0,0))
            if token.type not in [6,7,9,10,11]:
                token_list.append(TokenConvertor.convert_token(token))
        par = p.Parser()
        ast = par(token_list)
        inter = interpreter.Interpreter()
        text = inter(ast)
        return text

    else:
        # Default: Use the Antlr Parser
        parser = SceneParser(token_stream)           # Parse tokens into a parse tree
        tree = parser.document()                     # Start parsing from the root rule `s`
        # print(tree.toStringTree(recog=parser))
        visitor = SceneInterpreterVisitor()
        text = visitor.visit(tree)                   # Recursively walk parse tree and interpret
        return text

if __name__ == '__main__':
    print(parseScenes())
