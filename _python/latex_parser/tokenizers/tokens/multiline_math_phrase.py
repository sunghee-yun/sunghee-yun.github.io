"""
LaTeX math phrase $$ ... $$ or \\[ ... \\]
"""

from latex_parser.tokenizers.tokens.math_phrase_base import MathPhraseBase


class MultilineMathPhrase(MathPhraseBase):
    @property
    def opening_markdown_symbol(self) -> str:
        return "$$"

    @property
    def closing_markdown_symbol(self) -> str:
        return "$$"

    num_instances: int = 0

    def __init__(self, string: str, line_num: int, content: str) -> None:
        super().__init__(string, line_num, content)
        MultilineMathPhrase.num_instances += 1
