# CWDE615
# file containing the main function and entry point for the the Mixtec Parser and interpreter.
import parser
import tokens
import interpreter

def main():
    token_list : list[tokens.Token] = parser.construct_from_samples([
        'lord-standing-right',
        'year-5-house',
        'date-4-wind',
        'lady-sitting-left',
        'date-10-serpent', 
        'end'
    ])

    par = parser.Parser()
    ast = par(token_list)
    inter = interpreter.Interpreter()
    txt = inter(ast)

    print(txt)


if __name__ == "__main__":
    main()