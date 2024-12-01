# CWDE615
# file containing the main function and entry point for the the Mixtec Parser and interpreter.
import parser
import tokens
import interpreter

def main():
    token_list : list[tokens.Token] = parser.construct_from_samples([
        'year-5-house', 
        'lord-standing-right',
        'date-4-wind',
        'lady-sitting-left',
        'date-10-serpent',
        'end'
    ])

    par = parser.Parser(token_list)
    ast = par()
    inter = interpreter.Interpreter(ast)
    txt = inter()

    print(txt)


if __name__ == "__main__":
    main()