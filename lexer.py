import argparse
from enum import Enum

class TokenType(Enum):
    LET = 1
    IDENTIFIER = 2
    EQUALS = 3
    NUMBER = 4
    SEMICOLON = 5
    PRINT = 6
    ADD = 7

class Token():
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)

    args = parser.parse_args()

    print("inputfile:",args.input)
    
    with open(args.input, "r") as file:
        source = file.read()

    print("contents of file:\n", source)

    #convertToTokens(source)

def convertToTokens(source):
    currentWord = ""
    i = 0

    while i < len(source):
        char = source[i]
        currentWord += char