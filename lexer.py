import re

from pygments.lexer import RegexLexer, words
from pygments.token import Text, Keyword, Punctuation, Operator, Name, Number

__all__ = ['PL0Lexer']


class PL0Lexer(RegexLexer):
    name = 'PL/0'
    filenames = ['*.pl0']
    aliases = ['pl0']
    mimetypes = ['text/x-pl0src']

    flags = re.IGNORECASE

    tokens = {
        'root': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'(var|procedure|const)\b', Keyword.Declaration),
            (words(('call', 'begin', 'end', 'if', 'then', 'while', 'do',
                    'odd'), suffix=r'\b'), Keyword),
            (r'[.,;()]', Punctuation),
            (r'(:=|#|<=|>=|<|>|=|[+\-*/]|[!?])', Operator),
            (r'(0|[1-9]\d*)', Number),
            (r'[^\W\d]\w*', Name.Identifier),
        ]
    }

