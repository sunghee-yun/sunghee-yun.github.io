"""
LaTeX equation - \\begin{eqnarray} ... \\end{eqnarray} or \\begin{eqnarray*} ... \\end{eqnarray*}
"""

from latex_parser.tokenizers.tokens.math_phrase_base import MathPhraseBase


class EqnArrayMathPhrase(MathPhraseBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, content: str) -> None:
        super().__init__(string, line_num, content)
        EqnArrayMathPhrase.num_instances += 1

    @property
    def opening_markdown_symbol(self) -> str:
        return "$$\n\\begin{eqnarray*}"

    @property
    def closing_markdown_symbol(self) -> str:
        return "\\end{eqnarray*}\n$$"
