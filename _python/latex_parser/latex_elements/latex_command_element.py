"""
Latex command element
"""

from copy import copy

from latex_parser.latex_elements.latex_element_base import LaTeXElementBase
from latex_parser.tokenizers.tokens.command_base import CommandBase
from latex_parser.tokenizers.tokens.user_defined_command import UserDefinedCommand


class LatexCommandElement(LaTeXElementBase):

    def __init__(
        self, latex_command: CommandBase, arg_list: list[str], opt_arg_list: list[str]
    ) -> None:
        self.latex_command: CommandBase = copy(latex_command)
        self.arg_list: list[str] = arg_list.copy()
        self.opt_arg_list: list[str] = opt_arg_list.copy()

    def __repr__(self) -> str:
        return self.latex_command.string + "".join(["{" + arg + "}" for arg in self.arg_list])

    def to_markdown_str(self, indent: str = "") -> str:
        if isinstance(self.latex_command, UserDefinedCommand):
            command_string: str = self.latex_command.string
            if command_string in [r"\eg", r"\iaoi", r"\wrt", r"\cara"]:
                assert len(self.arg_list) == 0, (self.arg_list, len(self.arg_list))
                if command_string == r"\eg":
                    return "<i>e.g.</i>"

                if command_string == r"\iaoi":
                    return "if and only if"

                if command_string == r"\wrt":
                    return "with respect to"

                if command_string == r"\cara":
                    return "Carathe&#776;odory"

                assert False

            if command_string in [r"\define", r"\emph", r"\cemph", r"\eemph", '\\"']:
                assert len(self.arg_list) == 1, (
                    self.latex_command,
                    self.arg_list,
                    len(self.arg_list),
                )
                arg: str = self.arg_list[0]

                if command_string == r"\define":
                    return f'<span class="define">{arg}</span>'

                if command_string == r"\emph":
                    return f"<i>{arg}</i>"

                if command_string == r"\cemph":
                    return f'<span class="emph">{arg}</span>'

                if command_string == r"\eemph":
                    return f'<span class="eemph">{arg}</span>'

                if command_string == '\\"':
                    assert len(arg.strip()) == 1, arg.strip()
                    return f"{arg.strip()}&#776;"

                assert False

        return ""
