"""
new lines
"""

from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase


class WhiteSpaces(LaTeXTokenBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        WhiteSpaces.num_instances += 1
