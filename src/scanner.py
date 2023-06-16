from enum import Enum, auto

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
    COMMENT = "//"

    # operators
    PLUS = "+"
    MINUS = "-"
    STAR = "*"
    
    # literals.
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"
    
    
    EOF = "eof"
    
    AND = 23
    OR = 24
    FALSE = 25
    TRUE = 26
    FUNC = 27
    NIL = 28
    AUTO = 29
    BREAK = 30
    CASE = 31
    CHAR = 32
    CONST = 33
    CONTINUE = 34
    DEFAULT = 35
    DO = 36
    DOUBLE = 37
    ELSE = 38
    ENUM = 39
    EXTERN = 40
    FLOAT = 41
    FOR = 42
    GOTO = 43
    IF = 44
    INT = 45
    LONG = 46
    REGISTER = 47
    RETURN = 48
    SHORT = 49
    SIGNED = 50
    SIZEOF = 51
    STATIC = 52
    STRUCT = 53
    SWITCH = 54
    TYPEDEF = 55
    UNION = 56
    UNSIGNED = 57
    VOID = 58
    VOLATILE = 59
    WHILE = 60
    
    INCLUDE = auto()
    DEFINE = auto()
    UNDEF = auto()
    IFDEF = auto()
    IFNDEF = auto()
    ELIF = auto()
    ENDIF = auto()
    LINE = auto()
    ERROR = auto()
    PRAGMA = auto()
    
  
    BOOL = auto()
    COMPLEX = auto()
    IMAGINARY = auto()
    SIZE_T = auto()
    PTRDIFF_T = auto()
    WCHAR_T = auto()
    INT8_T = auto()
    UINT8_T = auto()
    INT16_T = auto()
    UINT16_T = auto()
    INT32_T = auto()
    UINT32_T = auto()
    INT64_T = auto()
    UINT64_T = auto()
    INTPTR_T = auto()
    UINTPTR_T = auto()
    INTMAX_T = auto()
    UINTMAX_T = auto()
   
# Types
# @note can also be treated as keywords or even Types, but we are treating them as Identifiers for now.
TYPES = {
    "void": TokenType.VOID,
    "char": TokenType.CHAR,
    "short": TokenType.SHORT,
    "int": TokenType.INT,
    "long": TokenType.LONG,
    "float": TokenType.FLOAT,
    "double": TokenType.DOUBLE,
    "signed": TokenType.SIGNED,
    "unsigned": TokenType.UNSIGNED,
    "bool": TokenType.BOOL,
    "complex": TokenType.COMPLEX,
    "imaginary": TokenType.IMAGINARY,
    "size_t": TokenType.SIZE_T,
    "ptrdiff_t": TokenType.PTRDIFF_T,
    "wchar_t": TokenType.WCHAR_T,
    "int8_t": TokenType.INT8_T,
    "uint8_t": TokenType.UINT8_T,
    "int16_t": TokenType.INT16_T,
    "uint16_t": TokenType.UINT16_T,
    "int32_t": TokenType.INT32_T,
    "uint32_t": TokenType.UINT32_T,
    "int64_t": TokenType.INT64_T,
    "uint64_t": TokenType.UINT64_T,
    "intptr_t": TokenType.INTPTR_T,
    "uintptr_t": TokenType.UINTPTR_T,
    "intmax_t": TokenType.INTMAX_T,
    "uintmax_t": TokenType.UINTMAX_T
}
    
# @note some of these are handled in before the lexer stage by a preprocessor. We are keeping it simple
PREPROCESSOR_DIRECTIVES = {
    "include": TokenType.INCLUDE,
    "define": TokenType.DEFINE,
    "undef": TokenType.UNDEF,
    "if": TokenType.IF,
    "ifdef": TokenType.IFDEF,
    "ifndef": TokenType.IFNDEF,
    "else": TokenType.ELSE,
    "elif": TokenType.ELIF,
    "endif": TokenType.ENDIF,
    "line": TokenType.LINE,
    "error": TokenType.ERROR,
    "pragma": TokenType.PRAGMA
}

KEYWORDS = {
    "&&": TokenType.AND,
    "||": TokenType.OR,
    "false": TokenType.FALSE,
    "true": TokenType.TRUE,
    "func": TokenType.FUNC,
    "null": TokenType.NIL,
    "auto": TokenType.AUTO,
    "break": TokenType.BREAK,
    "case": TokenType.CASE,
    "char": TokenType.CHAR,
    "const": TokenType.CONST,
    "continue": TokenType.CONTINUE,
    "default": TokenType.DEFAULT,
    "do": TokenType.DO,
    "double": TokenType.DOUBLE,
    "else": TokenType.ELSE,
    "enum": TokenType.ENUM,
    "extern": TokenType.EXTERN,
    "float": TokenType.FLOAT,
    "for": TokenType.FOR,
    "goto": TokenType.GOTO,
    "if": TokenType.IF,
    "int": TokenType.INT,
    "long": TokenType.LONG,
    "register": TokenType.REGISTER,
    "return": TokenType.RETURN,
    "short": TokenType.SHORT,
    "signed": TokenType.SIGNED,
    "sizeof": TokenType.SIZEOF,
    "static": TokenType.STATIC,
    "struct": TokenType.STRUCT,
    "switch": TokenType.SWITCH,
    "typedef": TokenType.TYPEDEF,
    "union": TokenType.UNION,
    "unsigned": TokenType.UNSIGNED,
    "void": TokenType.VOID,
    "volatile": TokenType.VOLATILE,
    "while": TokenType.WHILE,
}



class Error(Exception):
    
    @staticmethod
    def error(line, message):
        Error.report(line, "", message)
        Error.had_error = True

    @staticmethod
    def report(line, where, message):
        print("[line {}] Error {}: {}".format(line, where, message))
        Error.had_error = True

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
            # we move with each token
            self.start = self.current
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
        elif c == ';':
            self.add_token(TokenType.SEMICOLON)
        # operators
        elif c == '-':
            self.add_token(TokenType.MINUS)
        elif c == '+':
            self.add_token(TokenType.PLUS)
        elif c == '*':
            self.add_token(TokenType.STAR)
        elif c.isdigit():
            self.handle_number_literal(c)
        # matches the bang, if the next character is an equal sign, then it is a bang equal else it is just a bang
        elif c == '!':
            if self.match('='):
                self.add_token(TokenType.BANG_EQUAL)
            else:
                self.add_token(TokenType.BANG)
                
        elif c == '=':
            if self.match('='):
                self.add_token(TokenType.EQUAL_EQUAL)
            else:
              self.add_token(TokenType.EQUAL)
        elif c == '<':
            if self.match('='):
                self.add_token(TokenType.LESS_EQUAL)
            else:
                self.add_token(TokenType.LESS)
        elif c == '>':
            if self.match('='):
                self.add_token(TokenType.GREATER_EQUAL)
            else:
                self.add_token(TokenType.GREATER)
        elif c == '/':
            if self.peek() != '/':
                # then it is a division operator
                self.add_token(TokenType.SLASH)
            elif self.peek() == '/':
                # then it is a comment
                self.handle_comment()
        # handle whitespaces
        elif c == ' ' or c == '\r' or c == '\t':
            pass # ignore whitespace
        elif c == '\n':
            # we are at a new line, so we increment the line counter
            self.line += 1
            self.advance()        
        elif c.isalpha():
            # @audit is this method satisfactory? or should we use a hashmap with find()?
            self.handle_identifier()

        elif c == '"':
            self.handle_string_literal()
        # @todo there should be a main function handler
        # @todo there should be a function handler
        else:
            Error.error(self.line, "Unexpected character.")

    # check if next character is the expected one
    def match(self, expected):
        # if we are at the end of the source code, return false
        if self.is_at_end():
            return False
        # if the next character is not the expected one, return false
        if self.source[self.current]  != expected:
            return False
        # otherwise, advance and return true
        self.current += 1
        return True
    
    def handle_comment(self):
        while self.peek() != '\n' and not self.is_at_end():
            self.advance()
        if self.peek() == '\n':
            self.advance()

    # peek looks at the next character without consuming it
    def peek(self):
        if self.is_at_end():
            return '\0'
        return self.source[self.current]
     # move to the next character and return the current one
    def advance(self):
        # @todo rewrite
        self.current += 1
        return self.source[self.current - 1]
    
    # handlers for literals and keywords
    def handle_string_literal(self):
        value = ""
        # find the end of the string double quote or single quote        
        while self.peek() != '"' and not self.is_at_end():

            # we keep advancing until we find the end of the string
            # @note in C language, strings can span multiple lines using double quotes
            # so \n should not really be a problem. will have to fix this later
            if self.peek() == '\n':
                self.line += 1
            value += self.advance()
        
        # unterminated string
        if self.is_at_end():
            Error.error(self, self.line, "Unterminated string.")
            return
        
        self.advance()
        value = self.source[self.start + 1:self.current - 1]
        self.add_token(TokenType.STRING, value)
        
    # @todo error handling
    def handle_number_literal(self, first_digit):
        number = first_digit
        while self.peek().isdigit():
            number += self.advance()

        if self.peek() == '.':
            number += self.advance()
            while self.peek().isdigit():
                number += self.advance()

        self.add_token(TokenType.NUMBER, float(number) if '.' in number else int(number))



    
    def handle_identifier(self):
        while self.peek().isalnum() or self.peek() == '_':
            self.advance()

        text = self.source[self.start:self.current]
        token_type = TokenType.IDENTIFIER
        # Check if the identifier is a keyword
        if text in KEYWORDS:
            token_type = KEYWORDS[text]
        elif text in TYPES:
            token_type = TYPES[text]
        elif text in PREPROCESSOR_DIRECTIVES:
            token_type = PREPROCESSOR_DIRECTIVES[text]
        
        self.add_token(token_type)
    
        
        
# a sample C source code
# @todo fix problems with comment parsing
src ="32 1234"

# create a scanner object
scanner = Scanner(src)

# scan the source code
scanner.scan_tokens()

# for token in scanner.tokens:
#     print(token);
    