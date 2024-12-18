# CWDE615
# file containing the main function and entry point for the the Mixtec Parser and interpreter.
import parser
import tokens
import interpreter

def run_list(token_list : list[tokens.Token]):
    par = parser.Parser()
    ast = par(token_list)
    inter = interpreter.Interpreter()
    txt = inter(ast)

    return txt

def test1():
    token_list : list[tokens.Token] = parser.construct_from_samples([
        
        'year-5-house',
        'lord-standing-right',
        'date-4-wind',
        'lady-sitting-left',
        'date-10-serpent', 
        'end',
    ])

    return run_list(token_list)

def test2():
    token_list : list[tokens.Token] = parser.construct_from_samples([
        
        'year-5-house',
        'lord-sitting-right',
        'date-4-wind',
        'house',
        'lord-standing-left',
        'shield',
        'date-6-death', 
        'end',
    ])

    return run_list(token_list)

def test3():
    token_list : list[tokens.Token] = parser.construct_from_samples([
        
        'year-5-house',
        'lord-standing-right',
        'sacrificed-animal',
        'date-4-wind',
        'lord-standing-left',
        'date-6-death', 
        'end',
    ])

    return run_list(token_list)

def test4():
    token_list : list[tokens.Token] = parser.construct_from_samples([
        
        'year-5-house',
        'lord-standing-right',
        'weapon',
        'date-4-wind',
        'lord-standing-left',
        'shield',
        'date-6-death', 
        'end',
    ])

    return run_list(token_list)


def main():
    print(f'test 1: {test1()}')
    print(f'test 2: {test2()}')
    print(f'test 3: {test3()}')
    print(f'test 4: {test4()}')




if __name__ == "__main__":
    main()