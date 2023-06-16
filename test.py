import unittest

from src.scanner import TokenType, Scanner

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

    # def test_operators(self):
    #     scanner = Scanner("! != = == > >= < <=")
    #     scanner.scan_tokens()
    #     for token in scanner.tokens:
    #       print(token)

        # expected_tokens = [TokenType.BANG, TokenType.BANG_EQUAL, TokenType.EQUAL, 
        #                    TokenType.EQUAL_EQUAL, TokenType.GREATER, TokenType.GREATER_EQUAL, 
        #                    TokenType.LESS, TokenType.LESS_EQUAL]
        # self.assertEqual(len(scanner.tokens), len(expected_tokens))
        # for token, expected_token in zip(scanner.tokens, expected_tokens):
        #     self.assertEqual(token.type, expected_token)

    # @note the text of the comment is ignored and the contents of the comment are not scanned
    def test_ignore_comments(self):
        scanner = Scanner("++// this is a comment&&\n++")
        scanner.scan_tokens()
        self.assertEqual(len(scanner.tokens), 4)
        for token in scanner.tokens:
          self.assertEqual(token.type, TokenType.PLUS)

    # def test_string_literal(self):
    #     scanner = Scanner('"this is a string"')
    #     scanner.scan_tokens()
    #     self.assertEqual(len(scanner.tokens), 1)
    #     self.assertEqual(scanner.tokens[0].type, TokenType.STRING)
    #     self.assertEqual(scanner.tokens[0].literal, "this is a string")

    # def test_number_literal(self):
    #     scanner = Scanner("1234 12.34")
    #     scanner.scan_tokens()
    #     self.assertEqual(len(scanner.tokens), 2)
    #     self.assertEqual(scanner.tokens[0].type, TokenType.NUMBER)
    #     self.assertEqual(scanner.tokens[0].literal, 1234)
    #     self.assertEqual(scanner.tokens[1].type, TokenType.NUMBER)
    #     self.assertEqual(scanner.tokens[1].literal, 12.34)

    # def test_identifiers(self):
    #     scanner = Scanner("abc abc123 _abc")
    #     scanner.scan_tokens()
    #     self.assertEqual(len(scanner.tokens), 3)
    #     for token in scanner.tokens:
    #         self.assertEqual(token.type, TokenType.IDENTIFIER)

    # def test_keywords(self):
    #     scanner = Scanner("auto break case char const continue default do double else enum extern")
    #     scanner.scan_tokens()
    #     expected_tokens = [TokenType.KEYWORDS["auto"], TokenType.KEYWORDS["break"], 
    #                        TokenType.KEYWORDS["case"], TokenType.KEYWORDS["char"], 
    #                        TokenType.KEYWORDS["const"], TokenType.KEYWORDS["continue"], 
    #                        TokenType.KEYWORDS["default"], TokenType.KEYWORDS["do"], 
    #                        TokenType.KEYWORDS["double"], TokenType.KEYWORDS["else"], 
    #                        TokenType.KEYWORDS["enum"], TokenType.KEYWORDS["extern"]]
    #     self.assertEqual(len(scanner.tokens), len(expected_tokens))
    #     for token, expected_token in zip(scanner.tokens, expected_tokens):
    #         self.assertEqual(token.type, expected_token)

if __name__ == "__main__":
    unittest.main()
