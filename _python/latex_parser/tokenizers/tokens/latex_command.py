"""
LaTeX command such as \\newcommand, \\usepackage, \\def, etc.
"""

from enum import Enum

from latex_parser.tokenizers.tokens.command_token_base import CommandTokenBase


class LaTeXCommandEnum(Enum):
    DEF = "def"
    NEWCOMMAND = "newcommand"
    RENEWCOMMAND = "renewcommand"
    NEWTHEOREM = "newtheorem"
    NEWENVIRONMENT = "newenvironment"
    NEWCOUNTER = "newcounter"
    USEPACKAGE = "usepackage"
    IFDEFINED = "ifdefined"
    IFTHENELSE = "ifthenelse"
    ELSE = "else"
    FI = "fi"
    ITEM = "item"
    VFILL = "vfill"
    PAREREF = "pageref"
    PARELABEL = "pagelabel"
    BEGIN = "begin"
    END = "end"
    FOOTNOTE = "footnote"
    HYPERREF = "hyperref"
    HSPACE = "hspace"
    VSPACE = "vspace"
    LABEL = "label"
    MBOX = "mbox"
    INDEX = "index"
    NOCITE = "nocite"
    LDOTS = "ldots"
    NOINDENT = "noindent"
    INCLUDEGRAPHICS = "includegraphics"
    PHANTOMSECTION = "phantomsection"


class LaTeXCommandToken(CommandTokenBase):
    num_instances: int = 0

    COMMANDS_DEFINED: set[str] = set()

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        LaTeXCommandToken.num_instances += 1
        self.latex_command_enum: LaTeXCommandEnum = LaTeXCommandEnum(string[1:])

    @staticmethod
    def is_latex_command_string(string: str) -> bool:
        assert string.startswith("\\") and len(string) > 1, (string, len(string))
        try:
            LaTeXCommandEnum(string[1:])
        except ValueError:
            return False

        return True

    def latex_command_to_markdown_str(self, arg_list: list[str], opt_arg_list: list[str]) -> str:
        self.COMMANDS_DEFINED.add(self.string)
        return ""
