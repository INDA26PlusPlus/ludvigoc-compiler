from token import Token, TokenType

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