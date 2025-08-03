"""
User-defined commands defined by \\def, \\newcommand
"""

from latex_parser.tokenizers.tokens.command_base import CommandBase


class UserDefinedCommand(CommandBase):
    num_instances: int = 0
    user_command_set: set[str] = set()

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        UserDefinedCommand.num_instances += 1
        UserDefinedCommand.user_command_set.add(string)
