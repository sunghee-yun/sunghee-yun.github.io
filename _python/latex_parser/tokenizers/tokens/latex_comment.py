"""
LaTeX comment, i.e., starting with %
"""

import re
from re import Match

from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.parsing_exception import ParsingException


class LaTeXComment(LaTeXTokenBase):
    num_instances: int = 0

    def __init__(self, comment: str, line_num: int) -> None:
        super().__init__(comment, line_num)
        LaTeXComment.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, Match]:
        match: Match | None = re.match(r"(%[^\n]*)\n", source_left)
        if match:
            return LaTeXComment(match.group(1), line_num), match

        raise ParsingException()
