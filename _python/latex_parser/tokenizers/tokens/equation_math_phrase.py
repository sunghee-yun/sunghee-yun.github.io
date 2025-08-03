"""
LaTeX equation - \\begin{equation} ... \\end{equation}
"""

from latex_parser.tokenizers.tokens.math_phrase_base import MathPhraseBase


class EquationMathPhrase(MathPhraseBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, content) -> None:
        super().__init__(string, line_num, content)
        EquationMathPhrase.num_instances += 1

    @property
    def opening_markdown_symbol(self) -> str:
        return "$$\n\\begin{equation}"

    @property
    def closing_markdown_symbol(self) -> str:
        return "\\end{equation}\n$$"
