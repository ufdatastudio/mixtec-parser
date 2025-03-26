
import sys
import argparse
from antlr4 import *
from SceneLexer import SceneLexer
from SceneParser import SceneParser
from scene_interpreter_visitor import SceneInterpreterVisitor
from interpreter import run_interpreter  # fallback to original interpreter

def main():
    parser = argparse.ArgumentParser(description="Scene parser and interpreter")
    parser.add_argument("input", nargs="?", default=None, help="Input string or file")
    parser.add_argument("-v", "--visitor", action="store_true", help="Use visitor-based interpreter")
    args = parser.parse_args()

    # Determine input source
    if args.input is None:
        input_stream = InputStream(sys.stdin.read())
    else:
        try:
            with open(args.input, 'r') as f:
                input_stream = InputStream(f.read())
        except FileNotFoundError:
            input_stream = InputStream(args.input)

    lexer = SceneLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SceneParser(token_stream)

    tree = parser.s()

    if args.visitor:
        visitor = SceneInterpreterVisitor()
        result = visitor.visit(tree)
        print("[Visitor Result]", result)
    else:
        result = run_interpreter(tree)
        print("[Interpreter Result]", result)

if __name__ == '__main__':
    main()
