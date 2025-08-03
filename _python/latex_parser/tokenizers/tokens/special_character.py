"""
some special LaTeX characters such as \\&, \\
"""

import re
from re import Match

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase


class SpecialCharacter(LaTeXTokenBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        SpecialCharacter.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(
            r"((\\#)|(---)|(--)|('')|(``)|(\\&)|(\\)|(/)|(`)|('))", source_left
        )
        if match:
            return SpecialCharacter(match.group(1), line_num), match.span()[1]

        raise ParsingException()

    @property
    def markdown_str(self) -> str:
        if self.string == r"\&":
            return "&amp;"

        if self.string == "\\":
            return ""

        if self.string == "---":
            return "&mdash;"

        if self.string == "--":
            return "&ndash;"

        if self.string == "``":
            return "&ldquo;"

        if self.string == "''":
            return "&rdquo;"

        if self.string == "`":
            return "&lsquo;"

        if self.string == "'":
            return "&rsquo;"

        if self.string == "/":
            return "/"

        if self.string == r"\#":
            return "#"

        assert False
