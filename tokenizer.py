from enum import Enum

class TokenType(Enum):
    # single-character tokens.
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    COMMA = ","
    SEMICOLON = ";"
    DOT = "."
    SLASH = "/"

    # one or two character tokens.
    BANG = "!"
    BANG_EQUAL = "!="
    EQUAL = "="
    EQUAL_EQUAL = "=="
    GREATER = ">"
    GREATER_EQUAL = ">="
    LESS = "<"
    LESS_EQUAL = "<="

    #operators
    PLUS = "+"
    MINUS = "-"
    STAR = "*"
    
    # literals.
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"


    # keywords.
    AND = "&&"
    ELSE = "else"
    FALSE = "false"
    TRUE = "true"
    FUNC = "func"
    FOR = "for"
    IF = "if"
    # @audit probably error here
    NIL = "null"
    OR = "||"
    RETURN = "return"
    # there is no var in C language.
    WHILE = "while"

    EOF = "eof"

class Error(Exception):
    @staticmethod
    def error(self, line, message):
        self.report(line, "", message)

    @staticmethod
    def report(line, where, message):
        print("[line {}] Error {}: {}".format(line, where, message))
        had_error = True

class Token:
    # @todo see notes on what is a literal
    def __init__(self, typeof, lexeme, literal, line):
        self.type = typeof
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return "{} {} {}".format(self.type, self.lexeme, self.literal)

# the scanner class is used to scan the source code and generate tokens.
class Scanner:
    source = ""
    tokens = []
    start = 0
    # where the current token is
    current = 0
    line = 1
    

    def __init__(self, source):
        self.source = source
        self.tokens = []
    
    def scan_tokens(self):
        # print(len(self.source))
        while not self.is_at_end():
            print("scanning token")
            # we move with each token
            self.start = self.current
            print(self.start)
            print(self.current)
            self.scan_token()

    def is_at_end(self):
        # if current is greater than the length of the source code, then we are at the end of the source co
        return self.current >= len(self.source)
    
    def add_token(self, typeof, literal = None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(typeof, text, literal, self.line))

    # categorize the token and add it to the list of tokens
    def scan_token(self):
        c = self.advance()
        if c == '(':
            self.add_token(TokenType.LEFT_PAREN)
        elif c == ')':
            self.add_token(TokenType.RIGHT_PAREN)
        elif c == '{':
            self.add_token(TokenType.LEFT_BRACE)
        elif c == '}':
            self.add_token(TokenType.RIGHT_BRACE)
        elif c == ',':
            self.add_token(TokenType.COMMA)
        elif c == '.':
            self.add_token(TokenType.DOT)
        elif c == '-':
            self.add_token(TokenType.MINUS)
        elif c == '+':
            self.add_token(TokenType.PLUS)
        elif c == ';':
            self.add_token(TokenType.SEMICOLON)
        elif c == '*':
            self.add_token(TokenType.STAR)  
        else:
            print("error")
            

    # move to the next character and return the current one
    def advance(self):
        # @todo rewrite
        self.current += 1
        return self.source[self.current - 1]
    
    

# create a sample source code
src = "(){}+-"

# create a scanner object
scanner = Scanner(src)

# scan the source code
scanner.scan_tokens()
# print tokens as strings
for token in scanner.tokens:
    print(token)
    