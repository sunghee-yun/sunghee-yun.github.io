"""
\\TITLEFOIL
"""

import re
from re import Match

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.slide_section_base import SlideSectionBase
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase


class TopTitleFoil(SlideSectionBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, title: str, label: str) -> None:
        super().__init__(string, line_num, title, label)
        TopTitleFoil.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(
            r"(\\TITLEFOIL\s*{\s*([\s\S]*?)\s*}\s*{\s*([\s\S]*?)\s*})", source_left
        )
        if match:
            return (
                TopTitleFoil(match.group(1), line_num, match.group(2), match.group(3)),
                match.span()[1],
            )

        raise ParsingException()
