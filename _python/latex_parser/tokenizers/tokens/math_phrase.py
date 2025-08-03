"""
LaTeX math phrase $ ... $
"""

from latex_parser.tokenizers.tokens.math_phrase_base import MathPhraseBase


class MathPhrase(MathPhraseBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, content: str) -> None:
        super().__init__(string, line_num, content)
        MathPhrase.num_instances += 1

    @property
    def markdown_str(self) -> str:
        return f"${self.content}$"

    @property
    def opening_markdown_symbol(self) -> str:
        raise NotImplementedError()

    @property
    def closing_markdown_symbol(self) -> str:
        raise NotImplementedError()
