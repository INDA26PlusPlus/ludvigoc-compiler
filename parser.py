from token import Token, TokenType

def parse(tokensList):
    t = 0
    r = []
    statements = []
    while t < len(tokensList):
        match tokensList[t].type:
            case TokenType.LET:
                r = parseDeclaration(tokensList, t)
            case TokenType.IDENTIFIER:
                r = parseAssignment(tokensList, t)
            case TokenType.PRINT:
                r = parsePrint(tokensList, t)
            case TokenType.FOR:
                r = parseLoop(tokensList, t)
            case TokenType.ADD:
                r = parseAdd(tokensList, t)

        t += len(r)
        statements.append(r)

def parseDeclaration(tokensList, t):
    if (tokensList[t+1].type) != TokenType.IDENTIFIER:
        fail()
    elif (tokensList[t+2].type) != TokenType.EQUALS:
        fail()
    elif (tokensList[t+3].type) != TokenType.NUMBER:
        fail()
    elif (tokensList[t+4].type) != TokenType.SEMICOLON:
        fail()
    else:
        declarationList = [tokensList[t], tokensList[t+1], tokensList[t+2], tokensList[t+3], tokensList[t+4]]
        return declarationList

def fail():
    raise Exception("Syntax error")