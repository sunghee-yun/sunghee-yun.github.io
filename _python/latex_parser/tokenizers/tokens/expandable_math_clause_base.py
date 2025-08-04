"""
LaTeX multi-line math clause $$ ... $$ or \\[ ... \\]
"""

import re
from re import Match
from abc import ABC

from latex_parser.tokenizers.tokens.math_clause_base import MathClauseBase


class ExpandableMathClauseBase(MathClauseBase, ABC):
    @property
    def markdown_str(self) -> str:
        if re.match(r"[\s\S]*[^}]+{}", self.content) is None:
            return super().markdown_str

        markdown_content_: str = self.content

        match: Match | None = re.match(r"[\s\S]*([^}\s]+){}", markdown_content_)
        if match is None:
            assert re.match(r"[\s\S]*(\s){}", markdown_content_) is not None
            markdown_content_ = re.sub(r"(\s){}", r"\1&&", markdown_content_, 1)
        else:
            markdown_content_ = re.sub(r"([^}\s]+){}", r"&\1&", markdown_content_, 1)

        markdown_content_ = re.sub(
            r"([^}\s]+){}",
            r"\n\\\\\n&\1&",
            markdown_content_,
        )
        markdown_content_ = re.sub(
            r"(\s){}",
            r"\1\n\\\\\n&&",
            markdown_content_,
        )

        return "$$\n\\begin{eqnarray*}\n" + markdown_content_ + "\n\\end{eqnarray*}\n$$"
