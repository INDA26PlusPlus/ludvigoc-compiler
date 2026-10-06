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