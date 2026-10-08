from token import Token, TokenType
from enum import Enum

class Node:
    def __init__(self, t, children = []):
        self.type = t
        self.children = children

    def __repr__(self):
        return f"Type: {self.type} Children: {self.children}\n"

class statementTypes:
    DECLARATION = "declaration"
    ASSIGNMENT = "assignment"
    PRINTSTATEMENT = "print"
    ADDITION = "addition"
    LOOP = "loop"

def parseStatement(tokensList, t):
    match tokensList[t].type:
            case TokenType.LET:
                r = parseDeclaration(tokensList, t)
                t = t + 5
            case TokenType.IDENTIFIER:
                r = parseAssignment(tokensList, t)
                t = t + 4
            case TokenType.PRINT:
                r = parsePrint(tokensList, t)
                t = t + 5
            case TokenType.ADD:
                r = parseAdd(tokensList, t)
                t = t + 9
            case _:
                print("Unexpected token:", tokensList[t])
                fail()
    return r, t


def parse(tokensList):
    t = 0
    r = []
    statements = []

    while t < len(tokensList):

        if tokensList[t].type == TokenType.FOR:
            r, t = parseLoop(tokensList, t)
        else:
            r, t = parseStatement(tokensList, t)
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
        n = Node(statementTypes.DECLARATION, [tokensList[t+1], tokensList[t+3]])
        return n

def parseAssignment(tokensList, t):
    if (tokensList[t+1].type) != TokenType.EQUALS:
        fail()
    elif (tokensList[t+2].type) != TokenType.NUMBER and (tokensList[t+2].type) != TokenType.IDENTIFIER:
        fail()
    elif (tokensList[t+3].type) != TokenType.SEMICOLON:
        fail()
    else:
        n = Node(statementTypes.ASSIGNMENT, [tokensList[t], tokensList[t+2]])
        return n

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
        n = Node(statementTypes.PRINTSTATEMENT, [tokensList[t+2]])
        return n

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
        n = Node(statementTypes.ADDITION, [tokensList[t+2], tokensList[t+4], tokensList[t+6]])
        return n

def parseLoop(tokensList, t):
    if (tokensList[t+1].type) != TokenType.LPAREN:
        fail()
    elif (tokensList[t+2].type) != TokenType.NUMBER:
        fail()
    elif (tokensList[t+3].type) != TokenType.RPAREN:
        fail()
    elif (tokensList[t+4].type) != TokenType.LWING:
        fail()
    loopList = [Node(statementTypes.ADDITION, tokensList[t+2])]
    t = t+5

    statementsInLoop = []
    while tokensList[t].type != TokenType.RWING:
        r, t = parseStatement(tokensList, t)
        statementsInLoop.append(r)

    loopList.append(statementsInLoop)
    return Node(statementTypes.LOOP, loopList), t+1

def fail():
    raise Exception("Syntax error")