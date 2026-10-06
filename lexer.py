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
    LWING = 8
    RWING = 9
    LPAREN = 10
    RPAREN = 11
    FOR = 12
    COMMA = 13
    UNKNOWN = 14

class Token():
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def convertWord(word):

    if len(word) == 1 and "a" <= word <= "z":
        return Token(TokenType.IDENTIFIER, word)
    if word.isdigit():
        return Token(TokenType.NUMBER, word)

    
    match word:
        case "let": 
            t = TokenType.LET
        case "=": 
            t = TokenType.EQUALS
        case "printvar": 
            t = TokenType.PRINT
        case ";": 
            t = TokenType.SEMICOLON
        case "for": 
            t = TokenType.FOR
        case ",": 
            t = TokenType.COMMA
        case "add": 
            t = TokenType.ADD
        case "{": 
            t = TokenType.LWING
        case "}": 
            t = TokenType.RWING
        case "(": 
            t = TokenType.LPAREN
        case ")": 
            t = TokenType.RPAREN
        case _: 
            t = TokenType.UNKNOWN

    return Token(t, "")

def convertToTokens(source):
    currentWord = ""
    i = 0
    tokensList = []

    while i < len(source):
        char = source[i]
        if 'a' <= char <= 'z' or char.isdigit():
            currentWord += char
        else:
            if currentWord != "":
                tokensList.append(convertWord(currentWord))
                currentWord = ""
            if not char.isspace():
                tokensList.append(convertWord(char))
            
        i += 1

    return tokensList


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)

    args = parser.parse_args()

    print("inputfile:",args.input)
    
    with open(args.input, "r") as file:
        source = file.read()

    print("contents of file:\n", source)

    tokensList = convertToTokens(source)
    
    for t in tokensList:
        print(t)