"""
LaTeX Tokenizer
"""

import re
from re import Match
from typing import Generator

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.algorithmic_clause import AlgorithmicEnv
from latex_parser.tokenizers.tokens.braced_clause import BracedClause
from latex_parser.tokenizers.tokens.bracketed_clause import BracketedClause
from latex_parser.tokenizers.tokens.command_token_base import CommandTokenBase
from latex_parser.tokenizers.tokens.keyword_base import KeywordBase
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.tokens.math_clause_base import MathClauseBase
from latex_parser.tokenizers.tokens.new_lines_token import NewLines
from latex_parser.tokenizers.tokens.punctuation_token import PunctuationToken
from latex_parser.tokenizers.tokens.refer import Refer
from latex_parser.tokenizers.tokens.special_character import SpecialCharacter
from latex_parser.tokenizers.tokens.special_number_string import SpecialNumberString
from latex_parser.tokenizers.tokens.special_string import SpecialString
from latex_parser.tokenizers.tokens.white_spaces import WhiteSpaces
from latex_parser.tokenizers.tokens.word_token import WordToken


class LaTeXTokenizer:
    def __init__(self, latex_source: str) -> None:
        self.string_left: str = re.sub(r"%[^\n]*\n", "\n", latex_source)
        self.line_num: int = 0

    def tokenize(self) -> Generator[LaTeXTokenBase, None, None]:
        self.line_num = 1
        while len(self.string_left) > 0:

            def update_string_left(length: int):
                self.line_num += self.string_left[:length].count("\n")
                self.string_left = self.string_left[length:]

            # new line
            match: Match | None = re.match(r"(\n+)", self.string_left)
            if match:
                yield NewLines(match.group(1), self.line_num)
                update_string_left(match.span()[1])
                continue

            # white spaces
            match = re.match(r"(\s+)", self.string_left)
            if match:
                yield WhiteSpaces(match.group(1), self.line_num)
                update_string_left(match.span()[1])
                continue
            #
            # try:
            #     token, match = LaTeXComment.parse_and_create(self.string_left)
            #     update_string_left()
            #     yield token
            #     continue
            # except ParsingException:
            #     pass

            token_parsed: bool = False
            for cls in [
                WordToken,  # ~ 24889
                MathClauseBase,  # ~ 5945
                KeywordBase,  # ~ 6402
                PunctuationToken,  # ~ 4760
                Refer,  # ~ 194
                AlgorithmicEnv,  # ~ 9
                CommandTokenBase,  # ~ 4462
                BracedClause,  # ~ 4373
                SpecialCharacter,  # ~ 979
                BracketedClause,  # ~ 45
                SpecialString,  # ~ 0
                SpecialNumberString,  # ~ 0
            ]:
                try:
                    token, length = cls.parse_and_create(  # type:ignore
                        self.string_left, self.line_num
                    )
                    yield token
                    update_string_left(length)
                    token_parsed = True
                    break
                except ParsingException:
                    pass

            if token_parsed:
                continue

            assert False, (self.line_num, self.string_left[:30])
