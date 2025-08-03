"""
LaTeX math phrase
"""

import re
from abc import abstractmethod
from re import Match

from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.parsing_exception import ParsingException


class MathPhraseBase(LaTeXTokenBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, content: str) -> None:
        super().__init__(string, line_num)
        self.content: str = content
        MathPhraseBase.num_instances += 1

    @property
    @abstractmethod
    def opening_markdown_symbol(self) -> str:
        pass

    @property
    @abstractmethod
    def closing_markdown_symbol(self) -> str:
        pass

    @property
    def markdown_str(self) -> str:
        return f"\n{self.opening_markdown_symbol}\n{self.content}\n{self.closing_markdown_symbol}\n"

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        from latex_parser.tokenizers.tokens.math_phrase import MathPhrase
        from latex_parser.tokenizers.tokens.multiline_math_phrase import MultilineMathPhrase
        from latex_parser.tokenizers.tokens.equation_math_phrase import EquationMathPhrase
        from latex_parser.tokenizers.tokens.eqnarray_math_phrase import EqnArrayMathPhrase

        if source_left.startswith("$$\nX_n\\Rightarrow X, \\mbox{\\ie"):
            pass

        match: Match | None = re.match(r"(\$([^$]+)\$)", source_left)
        if match:
            return MathPhrase(match.group(1), line_num, match.group(2).strip()), match.span()[1]

        match = re.match(r"(\$\$([\s\S]*?)\$\$)", source_left)
        if match:
            return (
                MultilineMathPhrase(match.group(1), line_num, match.group(2).strip()),
                match.span()[1],
            )

        match = re.match(r"(\\\[((.|\n)*?)\\\])", source_left)
        if match:
            return (
                MultilineMathPhrase(match.group(1), line_num, match.group(2).strip()),
                match.span()[1],
            )

        match = re.match(
            r"(\\begin\s*{\s*equation\s*}((.|\n)*?)\\end\s*{\s*equation\s*})", source_left
        )
        if match:
            return (
                EquationMathPhrase(match.group(1), line_num, match.group(2).strip()),
                match.span()[1],
            )

        match = re.match(r"(\\begin\s*{\s*eqn\s*}((.|\n)*?)\\end\s*{\s*eqn\s*})", source_left)
        if match:
            return (
                MultilineMathPhrase(match.group(1), line_num, match.group(2).strip()),
                match.span()[1],
            )

        match = re.match(r"(\\begin\s*{\s*leqn\s*}((.|\n)*?)\\end\s*{\s*leqn\s*})", source_left)
        if match:
            return (
                MultilineMathPhrase(match.group(1), line_num, match.group(2).strip()),
                match.span()[1],
            )

        match = re.match(
            r"(\\begin\s*{\s*eqnarray(\*?)\s*}((.|\n)*?)\\end\s*{\s*eqnarray\*?\s*})", source_left
        )
        if match:
            return (
                EqnArrayMathPhrase(match.group(1), line_num, match.group(3).strip()),
                match.span()[1],
            )

        match = re.match(r"(\\begin\s*{\s*eqna\s*}((.|\n)*?)\\end\s*{\s*eqna\s*})", source_left)
        if match:
            return (
                EqnArrayMathPhrase(match.group(1), line_num, match.group(2).strip()),
                match.span()[1],
            )

        raise ParsingException()
