"""
Number that is enclosed by brackets,
mostly to designate the number of arguments of a LaTeX command defined by \\newcommand
"""

import re
from re import Match

from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.parsing_exception import ParsingException


class BracketedClause(LaTeXTokenBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        BracketedClause.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(r"(\[[^]]*\])", source_left)
        if match:
            return BracketedClause(match.group(1), line_num), match.span()[1]

        raise ParsingException()
