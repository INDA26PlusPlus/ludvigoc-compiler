from lexer import convertToTokens
from parser import parse
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)

    args = parser.parse_args()

    #print("inputfile:",args.input)
    
    with open(args.input, "r") as file:
        source = file.read()

    #print("contents of file:\n", source)

    tokensList = convertToTokens(source)
    
    parse(tokensList)

