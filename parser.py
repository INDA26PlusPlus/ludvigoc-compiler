from token import Token, TokenType

def superLen(lst):
    length = 0

    for element in lst:
        if isinstance(element, list):
            length += superLen(element)
        else:
            length += 1

    return length

def parseStatement(tokensList, t):
    match tokensList[t].type:
            case TokenType.LET:
                r = parseDeclaration(tokensList, t)
            case TokenType.IDENTIFIER:
                r = parseAssignment(tokensList, t)
            case TokenType.PRINT:
                r = parsePrint(tokensList, t)
            case TokenType.ADD:
                r = parseAdd(tokensList, t)
            case _:
                print("Unexpected token:", tokensList[t])
                fail()
    return r


def parse(tokensList):
    t = 0
    r = []
    statements = []

    while t < len(tokensList):

        if tokensList[t].type == TokenType.FOR:
            r = parseLoop(tokensList, t)
        else:
            r = parseStatement(tokensList, t)
        t += superLen(r)
        statements.append(r)
    
    return statements

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

def parseAssignment(tokensList, t):
    if (tokensList[t+1].type) != TokenType.EQUALS:
        fail()
    elif (tokensList[t+2].type) != TokenType.NUMBER and (tokensList[t+2].type) != TokenType.IDENTIFIER:
        fail()
    elif (tokensList[t+3].type) != TokenType.SEMICOLON:
        fail()
    else:
        declarationList = [tokensList[t], tokensList[t+1], tokensList[t+2], tokensList[t+3]]
        return declarationList

def parsePrint(tokensList, t):
    if (tokensList[t+1].type) != TokenType.LPAREN:
        fail()
    elif (tokensList[t+2].type) != TokenType.IDENTIFIER:
        fail()
    elif (tokensList[t+3].type) != TokenType.RPAREN:
        fail()
    elif (tokensList[t+4].type) != TokenType.SEMICOLON:
        fail()
    else:
        declarationList = [tokensList[t], tokensList[t+1], tokensList[t+2], tokensList[t+3], tokensList[t+4]]
        return declarationList

def parseAdd(tokensList, t):
    if (tokensList[t+1].type) != TokenType.LPAREN:
        fail()
    elif (tokensList[t+2].type) != TokenType.IDENTIFIER and (tokensList[t+2].type) != TokenType.NUMBER:
        fail()
    elif (tokensList[t+3].type) != TokenType.COMMA:
        fail()
    elif (tokensList[t+4].type) != TokenType.IDENTIFIER and (tokensList[t+4].type) != TokenType.NUMBER:
        fail()
    elif (tokensList[t+5].type) != TokenType.COMMA:
        fail()
    elif (tokensList[t+6].type) != TokenType.IDENTIFIER:
        fail()
    elif (tokensList[t+7].type) != TokenType.RPAREN:
        fail()
    elif (tokensList[t+8].type) != TokenType.SEMICOLON:
        fail()
    else:
        declarationList = [tokensList[t], tokensList[t+1], tokensList[t+2], tokensList[t+3], tokensList[t+4], tokensList[t+5], tokensList[t+6], tokensList[t+7], tokensList[t+8]]
        return declarationList

def parseLoop(tokensList, t):
    if (tokensList[t+1].type) != TokenType.LPAREN:
        fail()
    elif (tokensList[t+2].type) != TokenType.NUMBER:
        fail()
    elif (tokensList[t+3].type) != TokenType.RPAREN:
        fail()
    elif (tokensList[t+4].type) != TokenType.LWING:
        fail()
    loopList = [tokensList[t], tokensList[t+1], tokensList[t+2], tokensList[t+3], tokensList[t+4]]
    finalList = []
    finalList.append(loopList)
    t = t+5

    statementsInLoop = []
    while tokensList[t].type != TokenType.RWING:
        r = parseStatement(tokensList, t)
        t += len(r)
        statementsInLoop.append(r)

    finalList.append(statementsInLoop)
    finalList.append(tokensList[t])
    return finalList

def fail():
    raise Exception("Syntax error")