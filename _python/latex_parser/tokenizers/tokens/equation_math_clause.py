"""
LaTeX equation - \\begin{equation} ... \\end{equation}
"""

import re
from re import Match

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.tokens.math_clause_base import MathClauseBase


class EquationMathClause(MathClauseBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, content) -> None:
        super().__init__(string, line_num, content)
        EquationMathClause.num_instances += 1

    @property
    def opening_markdown_symbol(self) -> str:
        return "$$\n\\begin{equation}"

    @property
    def closing_markdown_symbol(self) -> str:
        return "\\end{equation}\n$$"

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(
            r"(\\begin\s*{\s*equation\s*}((.|\n)*?)\\end\s*{\s*equation\s*})", source_left
        )
        if match:
            return (
                EquationMathClause(match.group(1), line_num, match.group(2).strip()),
                match.span()[1],
            )

        raise ParsingException()
