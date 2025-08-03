"""
LaTeX command such as \\newcommand, \\usepackage, \\def, etc.
"""

from enum import Enum

from latex_parser.tokenizers.tokens.command_base import CommandBase


class LaTeXCommandEnum(Enum):
    NEWCOMMAND = "newcommand"
    NEWTHEOREM = "newtheorem"
    NEWENVIRONMENT = "newenvironment"
    NEWCOUNTER = "newcounter"
    DEF = "def"
    USEPACKAGE = "usepackage"
    IFDEFINED = "ifdefined"
    IFTHENELSE = "ifthenelse"
    ELSE = "else"
    FI = "fi"
    ITEM = "item"
    VFILL = "vfill"


class LaTeXCommand(CommandBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        LaTeXCommand.num_instances += 1
        self.latex_command_enum: LaTeXCommandEnum = LaTeXCommandEnum(string[1:])

    @staticmethod
    def is_latex_command_string(string: str) -> bool:
        assert string.startswith("\\") and len(string) > 1, (string, len(string))
        try:
            LaTeXCommandEnum(string[1:])
        except ValueError:
            return False

        return True
