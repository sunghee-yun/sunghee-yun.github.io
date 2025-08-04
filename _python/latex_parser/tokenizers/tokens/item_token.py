"""
- \\item
- \\vitem
- \\vvitem
- \\iitem
"""

import re
from re import Match

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.keyword_base import KeywordBase
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase


class ItemToken(KeywordBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        ItemToken.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(r"(\\(v+i?|i|b)?item\s*(\[.*])?)", source_left)
        if match:
            return ItemToken(match.group(1), line_num), match.span()[1]

        raise ParsingException()
