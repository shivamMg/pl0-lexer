import unittest

from pygments.token import Token

from lexer import PL0Lexer


class TestPL0Lexer(unittest.TestCase):
    def test_program_one(self):
        code = """
VAR x, squ;

PROCEDURE square;
BEGIN
   squ:= x * x
END;

BEGIN
   x := 1;
   WHILE x <= 10 DO
   BEGIN
      CALL square;
      ! squ;
      x := x + 1
   END
END.
"""
        result = [
            (Token.Keyword.Declaration, 'VAR'),
            (Token.Text, ' '),
            (Token.Name.Identifier, 'x'),
            (Token.Punctuation, ','),
            (Token.Text, ' '),
            (Token.Name.Identifier, 'squ'),
            (Token.Punctuation, ';'),
            (Token.Text, '\n'),
            (Token.Text, '\n'),
            (Token.Keyword.Declaration, 'PROCEDURE'),
            (Token.Text, ' '),
            (Token.Name.Identifier, 'square'),
            (Token.Punctuation, ';'),
            (Token.Text, '\n'),
            (Token.Keyword, 'BEGIN'),
            (Token.Text, '\n'),
            (Token.Text, '   '),
            (Token.Name.Identifier, 'squ'),
            (Token.Operator, ':='),
            (Token.Text, ' '),
            (Token.Name.Identifier, 'x'),
            (Token.Text, ' '),
            (Token.Operator, '*'),
            (Token.Text, ' '),
            (Token.Name.Identifier, 'x'),
            (Token.Text, '\n'),
            (Token.Keyword, 'END'),
            (Token.Punctuation, ';'),
            (Token.Text, '\n'),
            (Token.Text, '\n'),
            (Token.Keyword, 'BEGIN'),
            (Token.Text, '\n'),
            (Token.Text, '   '),
            (Token.Name.Identifier, 'x'),
            (Token.Text, ' '),
            (Token.Operator, ':='),
            (Token.Text, ' '),
            (Token.Literal.Number, '1'),
            (Token.Punctuation, ';'),
            (Token.Text, '\n'),
            (Token.Text, '   '),
            (Token.Keyword, 'WHILE'),
            (Token.Text, ' '),
            (Token.Name.Identifier, 'x'),
            (Token.Text, ' '),
            (Token.Operator, '<'),
            (Token.Operator, '='),
            (Token.Text, ' '),
            (Token.Literal.Number, '10'),
            (Token.Text, ' '),
            (Token.Keyword, 'DO'),
            (Token.Text, '\n'),
            (Token.Text, '   '),
            (Token.Keyword, 'BEGIN'),
            (Token.Text, '\n'),
            (Token.Text, '      '),
            (Token.Keyword, 'CALL'),
            (Token.Text, ' '),
            (Token.Name.Identifier, 'square'),
            (Token.Punctuation, ';'),
            (Token.Text, '\n'),
            (Token.Text, '      '),
            (Token.Operator, '!'),
            (Token.Text, ' '),
            (Token.Name.Identifier, 'squ'),
            (Token.Punctuation, ';'),
            (Token.Text, '\n'),
            (Token.Text, '      '),
            (Token.Name.Identifier, 'x'),
            (Token.Text, ' '),
            (Token.Operator, ':='),
            (Token.Text, ' '),
            (Token.Name.Identifier, 'x'),
            (Token.Text, ' '),
            (Token.Operator, '+'),
            (Token.Text, ' '),
            (Token.Literal.Number, '1'),
            (Token.Text, '\n'),
            (Token.Text, '   '),
            (Token.Keyword, 'END'),
            (Token.Text, '\n'),
            (Token.Keyword, 'END'),
            (Token.Punctuation, '.'),
            (Token.Text, '\n'),
        ]
        parser = PL0Lexer()
        self.assertEqual(result, list(parser.get_tokens(code)))


if __name__ == '__main__':
    unittest.main()

