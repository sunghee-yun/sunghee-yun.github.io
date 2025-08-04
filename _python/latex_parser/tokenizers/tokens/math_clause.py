"""
LaTeX inline math clause $ ... $
"""

import re
from re import Match

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.expandable_math_clause_base import ExpandableMathClauseBase
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase


class MathClause(ExpandableMathClauseBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, content: str) -> None:
        super().__init__(string, line_num, content)
        MathClause.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(r"(\$([^$]+)\$)", source_left)
        if match:
            return (
                MathClause(match.group(1), line_num, match.group(2)),
                match.span()[1],
            )

        raise ParsingException()

    @property
    def opening_markdown_symbol(self) -> str:
        return "$"

    @property
    def closing_markdown_symbol(self) -> str:
        return "$"

    @property
    def new_line(self) -> str:
        return ""
