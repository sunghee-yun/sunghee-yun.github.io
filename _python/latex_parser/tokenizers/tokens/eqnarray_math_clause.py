"""
LaTeX equation - \\begin{eqnarray} ... \\end{eqnarray} or \\begin{eqnarray*} ... \\end{eqnarray*}
"""

import re
from re import Match

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.tokens.math_clause_base import MathClauseBase
from utils import parse_nested_braced_clause


class EqnArrayMathClause(MathClauseBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, content: str) -> None:
        super().__init__(string, line_num, content)
        EqnArrayMathClause.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(
            r"(\\begin\s*{\s*eqnarray(\*?)\s*}((.|\n)*?)\\end\s*{\s*eqnarray\*?\s*})",
            source_left,
        )
        if match:
            return (
                EqnArrayMathClause(match.group(1), line_num, match.group(3)),
                match.span()[1],
            )

        match = re.match(r"(\\begin\s*{\s*eqna\s*}((.|\n)*?)\\end\s*{\s*eqna\s*})", source_left)
        if match:
            return (
                EqnArrayMathClause(match.group(1), line_num, match.group(2)),
                match.span()[1],
            )

        raise ParsingException()

    @property
    def opening_markdown_symbol(self) -> str:
        return "$$\n\\begin{eqnarray*}"

    @property
    def closing_markdown_symbol(self) -> str:
        return "\\end{eqnarray*}\n$$"

    @property
    def markdown_content(self) -> str:
        semi_final_result: str = self.content

        match: Match | None = re.match(r"[\s\S]*\\lefteqn\s*([\s\S]*)$", self.content)
        if match:
            string_after_lefteqn: str = match.group(1)
            lefteqn_clause: str = parse_nested_braced_clause(string_after_lefteqn)
            lefteqn_clause_: str = lefteqn_clause[1:-1]
            if "=" in lefteqn_clause_:
                assert re.match(r"[\s\S]*\s=\s", lefteqn_clause_) is not None, lefteqn_clause_
                lefteqn_clause_ = re.sub(r"(\s)=(\s)", r"\1&=&\2", lefteqn_clause_, 1)
            else:
                lefteqn_clause_ = "&&" + lefteqn_clause_

            semi_final_result = (
                lefteqn_clause_ + string_after_lefteqn[len(lefteqn_clause) :]  # noqa: E203
            )

        semi_final_result = re.sub(r"([^}\s]+){}", r"\n\\\\\n&\1&", semi_final_result)
        return re.sub(r"(\s){}", r"\1\n\\\\\n&&", semi_final_result)
        # return semi_final_result.replace("={}", "\n\\\\\n&=& ")
