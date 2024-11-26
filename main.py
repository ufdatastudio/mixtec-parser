# CWDE615
# file containing the main function and entry point for the the Mixtec Parser and interpreter.
import parser
import interpreter

def main(filename):
    print(f'Parsing file {filename}')
    
    print(f'Parsing passed. Interpreting...')

if __name__ == "__main__":
    main(filename='test_1.txt')