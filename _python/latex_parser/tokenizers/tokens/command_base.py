"""
Base class for LaTeX commands
"""

from __future__ import annotations

import re
from re import Match

from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.parsing_exception import ParsingException


class CommandBase(LaTeXTokenBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        CommandBase.num_instances += 1

    @staticmethod
    def create_command_token(string: str, line_num: int) -> CommandBase:
        from latex_parser.tokenizers.tokens.latex_command import LaTeXCommand
        from latex_parser.tokenizers.tokens.user_defined_command import UserDefinedCommand

        if LaTeXCommand.is_latex_command_string(string):
            return LaTeXCommand(string, line_num)
        return UserDefinedCommand(string, line_num)

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(r'(\\\w+|\\")', source_left)
        if match:
            return cls.create_command_token(match.group(1), line_num), match.span()[1]

        raise ParsingException()
