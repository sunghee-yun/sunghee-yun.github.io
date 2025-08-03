"""
Latex command element
"""

from copy import copy

from latex_parser.latex_elements.latex_element_base import LaTeXElementBase
from latex_parser.tokenizers.tokens.command_token_base import CommandTokenBase


class LaTeXCommandElement(LaTeXElementBase):

    def __init__(
        self,
        latex_command: CommandTokenBase,
        arg_list: list[str],
        opt_arg_list: list[str],
    ) -> None:
        self.latex_command: CommandTokenBase = copy(latex_command)
        self.arg_list: list[str] = arg_list.copy()
        self.opt_arg_list: list[str] = opt_arg_list.copy()

    def __repr__(self) -> str:
        return self.latex_command.string + "".join(["{" + arg + "}" for arg in self.arg_list])

    def to_markdown_str(self, indent: str = "") -> str:
        return self.latex_command.latex_command_to_markdown_str(self.arg_list, self.opt_arg_list)
