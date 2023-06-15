from enum import Enum

class TokenType(Enum):
    # single-character tokens.
    LEFT_PAREN,
    RIGHT_PAREN,
    LEFT_BRACE,
    RIGHT_BRACE,
    COMMA,
    SEMICOLON,

    # one or two character tokens.
    BANG,
    BANG_EQUAL,
    EQUAL,
    EQUAL_EQUAL,
    GREATER,
    GREATER_EQUAL,
    LESS,
    LESS_EQUAL,

    # literals.
    IDENTIFIER,
    STRING,
    NUMBER,

    # keywords.
    AND,
    ELSE,
    FALSE,
    TRUE,
    FUNC,
    FOR,
    IF,
    NIL,
    OR,
    RETURN,
    # there is no var in C language.
    WHILE,

    EOF

class Error(Exception):
    @staticmethod
    def error(line, message):
        report(line, "", message)

    @staticmethod
    def report(line, where, message):
        print("[line {}] Error {}: {}".format(line, where, message))
        had_error = True


