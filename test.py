import unittest

from src.scanner import TokenType, Scanner, KEYWORDS
from src.parser import Visitor, Binary, Grouping, Literal

class TestScanner(unittest.TestCase):

    def test_single_token(self):
        scanner = Scanner("+")
        scanner.scan_tokens()
        self.assertEqual(len(scanner.tokens), 1)
        self.assertEqual(scanner.tokens[0].type, TokenType.PLUS)

    def test_single_char_tokens(self):
        scanner = Scanner("(){},.;")
        scanner.scan_tokens()
        expected_tokens = [TokenType.LEFT_PAREN, TokenType.RIGHT_PAREN, 
                           TokenType.LEFT_BRACE, TokenType.RIGHT_BRACE, 
                           TokenType.COMMA, TokenType.DOT, TokenType.SEMICOLON,]
        self.assertEqual(len(scanner.tokens), len(expected_tokens))
        for token, expected_token in zip(scanner.tokens, expected_tokens):
            self.assertEqual(token.type, expected_token)

    def test_operators(self):
        scanner = Scanner("! != = == > >= < <=")
        scanner.scan_tokens()

        expected_tokens = [TokenType.BANG, TokenType.BANG_EQUAL, TokenType.EQUAL, 
                           TokenType.EQUAL_EQUAL, TokenType.GREATER, TokenType.GREATER_EQUAL, 
                           TokenType.LESS, TokenType.LESS_EQUAL]
        self.assertEqual(len(scanner.tokens), len(expected_tokens))
        for token, expected_token in zip(scanner.tokens, expected_tokens):
            self.assertEqual(token.type, expected_token)

    # @note the text of the comment is ignored and the contents of the comment are not scanned
    def test_ignore_comments(self):
        scanner = Scanner("++// this is a comment&&\n++")
        scanner.scan_tokens()
        self.assertEqual(len(scanner.tokens), 4)
        for token in scanner.tokens:
          self.assertEqual(token.type, TokenType.PLUS)

    def test_string_literal(self):
        scanner = Scanner('"this is a string"')
        scanner.scan_tokens()
        self.assertEqual(len(scanner.tokens), 1)
        self.assertEqual(scanner.tokens[0].type, TokenType.STRING)
        self.assertEqual(scanner.tokens[0].literal, "this is a string")

    def test_number_literal(self):
        scanner = Scanner("12 12.34")
        scanner.scan_tokens()
        
        self.assertEqual(len(scanner.tokens), 2)
        self.assertEqual(scanner.tokens[0].type, TokenType.NUMBER)
        self.assertEqual(scanner.tokens[0].literal, 12)
        self.assertEqual(scanner.tokens[1].type, TokenType.NUMBER)
        self.assertEqual(scanner.tokens[1].literal, 12.34)


    def test_identifiers_and_keywords(self):
        scanner = Scanner("auto break case char uint include define myVariable")
        scanner.scan_tokens()
        self.assertEqual(len(scanner.tokens), 8)
        # The first 4 tokens should be keywords
        for token in range(4):
            self.assertEqual(scanner.tokens[token].type, TokenType[scanner.tokens[token].lexeme.upper()])
        # # The last token should be an identifier
        self.assertEqual(scanner.tokens[4].type, TokenType.IDENTIFIER)


class TestVisitor(unittest.TestCase):
    def setUp(self):
        self.visitor = Visitor()

    def test_visit_binary_expression(self):
        # Test with literal expressions
        expr = Binary(Literal(1), '+', Literal(2))
        result = expr.accept(self.visitor)
        self.assertEqual(result, '(+ 1 2)')

        # Test with nested binary expressions
        expr = Binary(Binary(Literal(1), '+', Literal(2)), '*', Literal(3))
        result = expr.accept(self.visitor)
        self.assertEqual(result, '(* (+ 1 2) 3)')

    def test_visit_grouping_expression(self):
        expr = Grouping(Binary(Literal(1), '+', Literal(2)))
        result = expr.accept(self.visitor)
        self.assertEqual(result, '(group (+ 1 2))')

    def test_visit_literal_expression(self):
        expr = Literal(5)
        result = expr.accept(self.visitor)
        self.assertEqual(result, '5')

       

if __name__ == "__main__":
    unittest.main()
