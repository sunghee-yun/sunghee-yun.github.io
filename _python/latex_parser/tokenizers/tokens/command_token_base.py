"""
Base class for LaTeX commands
"""

from __future__ import annotations

from abc import abstractmethod
import re
from re import Match

from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.parsing_exception import ParsingException


class CommandTokenBase(LaTeXTokenBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        CommandTokenBase.num_instances += 1

    @abstractmethod
    def latex_command_to_markdown_str(self, arg_list: list[str], opt_arg_list: list[str]) -> str:
        pass

    @staticmethod
    def create_command_token(string: str, line_num: int) -> CommandTokenBase:
        from latex_parser.tokenizers.tokens.latex_command import LaTeXCommandToken
        from latex_parser.tokenizers.tokens.user_defined_command import (
            UserDefinedCommandToken,
        )

        if LaTeXCommandToken.is_latex_command_string(string):
            return LaTeXCommandToken(string, line_num)
        return UserDefinedCommandToken(string, line_num)

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        from latex_parser.tokenizers.tokens.def_command import DefCommandToken

        match: Match | None = re.match(r"(\\def)(\\\w+)", source_left)
        if match:
            return DefCommandToken(match.group(1), line_num, match.group(2)), match.span()[1]

        match = re.match(r"(\\(newcommand|renewcommand)){(\\\w+)}", source_left)
        if match:
            return DefCommandToken(match.group(1), line_num, match.group(3)), match.span()[1]

        match = re.match(r'(\\\w+|\\")', source_left)
        if match:
            return cls.create_command_token(match.group(1), line_num), match.span()[1]

        raise ParsingException()
