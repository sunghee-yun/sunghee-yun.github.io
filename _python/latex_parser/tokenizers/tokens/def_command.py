"""
LaTeX command such as \\newcommand, \\usepackage, \\def, etc.
"""

from latex_parser.tokenizers.tokens.latex_command import LaTeXCommandToken


class DefCommandToken(LaTeXCommandToken):
    num_instances: int = 0

    COMMANDS_DEFINED: set[str] = set()

    def __init__(self, string: str, line_num: int, command_str: str) -> None:
        super().__init__(string, line_num)
        self.command_str: str = command_str
        DefCommandToken.num_instances += 1
        DefCommandToken.COMMANDS_DEFINED.add(command_str)

    def latex_command_to_markdown_str(self, arg_list: list[str], opt_arg_list: list[str]) -> str:
        return ""
