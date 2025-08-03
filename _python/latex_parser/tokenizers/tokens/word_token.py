"""
plain word or phrase
"""

import re
from re import Match

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase


class WordToken(LaTeXTokenBase):
    num_instances: int = 0
    TOKEN_SET: set[str] = set()

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        WordToken.num_instances += 1
        self.TOKEN_SET.add(string)

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(r"([\w:'!]+)", source_left)
        if match:
            return WordToken(match.group(1), line_num), match.span()[1]

        raise ParsingException()
