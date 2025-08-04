"""
\\myfoilhead
"""

import re
from re import Match

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.braced_clause import BracedClause
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.tokens.slide_section_base import SlideSectionBase


class MyFoilhead(SlideSectionBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, title: str, label: str | None = None) -> None:
        super().__init__(
            string,
            line_num,
            title,
            f"my-foilhead-{MyFoilhead.num_instances}" if label is None else label,
        )
        MyFoilhead.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(r"(\\(myfoilhead|labelfoilhead)\s*)", source_left)
        if match:
            token, length = BracedClause.parse_and_create(
                source_left[match.span()[1] :], line_num  # noqa: E203
            )
            assert isinstance(token, BracedClause), token.__class__
            return MyFoilhead(
                match.group(1) + token.string, line_num, token.string[1:-1]
            ), match.span()[1] + len(token.string)

        raise ParsingException()
