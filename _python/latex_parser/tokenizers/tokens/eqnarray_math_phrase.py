"""
LaTeX equation - \\begin{eqnarray} ... \\end{eqnarray} or \\begin{eqnarray*} ... \\end{eqnarray*}
"""

import re
from re import Match

from latex_parser.tokenizers.tokens.math_phrase_base import MathPhraseBase
from utils import parse_nested_braced_clause


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

    @property
    def markdown_content(self) -> str:
        match: Match | None = re.match(r"\\lefteqn\s*([\s\S]*)$", self.content)
        if match:
            string_after_lefteqn: str = match.group(1)
            lefteqn_clause: str = parse_nested_braced_clause(string_after_lefteqn)
            lefteqn_clause_: str = lefteqn_clause[1:-1]
            if "=" in lefteqn_clause_:
                assert re.match(r"[\s\S]*\s=\s", lefteqn_clause_) is not None, lefteqn_clause_
                lefteqn_clause_ = re.sub(r"(\s)=(\s)", r"\1&=&\2", lefteqn_clause_)
            else:
                lefteqn_clause_ = "&=&" + lefteqn_clause_

            return lefteqn_clause_ + string_after_lefteqn[len(lefteqn_clause) :]  # noqa: E203
        return self.content
