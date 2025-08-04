"""
LaTeX command such as \\newcommand, \\usepackage, \\def, etc.
"""

from enum import Enum

from latex_parser.latex_elements.latex_element_base import LaTeXElementBase
from latex_parser.tokenizers.tokens.command_token_base import CommandTokenBase
from latex_parser.utils import make_label_consistent


class LaTeXCommandEnum(Enum):
    BEGIN = "begin"
    DEF = "def"
    ELSE = "else"
    END = "end"
    FOOTNOTE = "footnote"
    FI = "fi"
    HSPACE = "hspace"
    HYPERREF = "hyperref"
    IFDEFINED = "ifdefined"
    IFTHENELSE = "ifthenelse"
    INCLUDEGRAPHICS = "includegraphics"
    INDEX = "index"
    ITEM = "item"
    LABEL = "label"
    LDOTS = "ldots"
    MBOX = "mbox"
    NEWCOMMAND = "newcommand"
    NEWCOUNTER = "newcounter"
    NEWENVIRONMENT = "newenvironment"
    NEWTHEOREM = "newtheorem"
    NOCITE = "nocite"
    NOINDENT = "noindent"
    PARELABEL = "pagelabel"
    PAREREF = "pageref"
    RENEWCOMMAND = "renewcommand"
    PHANTOMSECTION = "phantomsection"
    USEPACKAGE = "usepackage"
    VFILL = "vfill"
    VSPACE = "vspace"


class LaTeXCommandToken(CommandTokenBase):
    num_instances: int = 0

    COMMANDS_CALLED: set[str] = set()
    COMMANDS_IGNORED_WHEN_CONVERTED_TO_MARKDOWN: set[str] = set()
    NUM_ARGS: dict[str, tuple[bool, int, int]] = dict(
        begin=(False, 1, 0),
        end=(False, 1, 0),
        footnote=(True, 1, 0),
        hspace=(True, 1, 0),
        hyperref=(True, 1, 1),
        ifthenelse=(False, 3, 0),
        includegraphics=(False, 1, 1),
        index=(False, 1, 0),
        label=(True, 1, 0),
        ldots=(True, 0, 0),
        noindent=(True, 0, 0),
        pagelabel=(True, 1, 0),
        pageref=(True, 1, 0),
        phantomsection=(True, 0, 0),
        nocite=(False, 1, 0),
        vfill=(True, 0, 0),
        vspace=(True, 1, 0),
    )

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

    def _latex_command_to_markdown_str(
        self, arg_list: list[str], opt_arg_list: list[str], max_num_opt_arg_list: int
    ) -> str:
        num_arg_list: int = len(arg_list)
        if num_arg_list == 0 and max_num_opt_arg_list == 0:
            if self.string == r"\ldots":
                return "&hellip;"

            if self.string == r"\noindent":
                return ""

            if self.string == r"\phantomsection":
                return ""

            if self.string == r"\vfill":
                return ""

        if num_arg_list == 1 and max_num_opt_arg_list == 0:
            arg: str = arg_list[0]
            if self.string == r"\footnote":
                return f"&nbsp;(footnote &ndash; {LaTeXElementBase.process_markdown_string(arg)})"

            if self.string == r"\hspace":
                return "&nbsp;"

            if self.string == r"\label":
                return f'<div id="{make_label_consistent(arg)}"></div>'

            if self.string == r"\pagelabel":
                return f'<div id="{make_label_consistent(arg)}"></div>'

            if self.string == r"\pageref":
                return f'<a href="#{make_label_consistent(arg)}">here</a>'

            if self.string == r"\vspace":
                return ""

        if num_arg_list == 1 and max_num_opt_arg_list == 1:
            arg = LaTeXElementBase.process_markdown_string(arg_list[0])
            if self.string == r"\hyperref":
                assert len(opt_arg_list) == 1, (opt_arg_list, len(opt_arg_list))
                return f'<a href="#{make_label_consistent(opt_arg_list[0])}">{arg}</a>'

        raise NotImplementedError(self.string)
