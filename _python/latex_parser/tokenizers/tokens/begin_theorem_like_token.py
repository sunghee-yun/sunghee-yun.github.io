"""
- \\begin{myaxiom}{...}
- \\begin{mylaw}{...}
- \\begin{myprinciple}{...}
- \\begin{mydefinition}{...}
- \\begin{mytheorem}{...}
- \\begin{mylemma}{...}
- \\begin{myproposition}{...}
- \\begin{mycorollary}{...}
- \\begin{myconjecture}{...}
- \\begin{myinequality}{...}
- \\begin{myformula}{...}
- \\begin{myalgorithm}{...}
"""

import re
from re import Match

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.tokens.keyword_base import KeywordBase


class BeginTheoremLikeToken(KeywordBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, env_name: str, name: str | None) -> None:
        assert name is not None or env_name == "proof", (env_name, name)
        super().__init__(string, line_num)
        self.env_name: str = env_name
        self.name: str | None = name
        BeginTheoremLikeToken.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(
            r"(\\begin\s*{\s*(" + cls.REG_EXP_THEOREM_LIKE_NAMES + r")\s*}{\s*([\s\S]*?)\s*})",
            source_left,
        )

        if match:
            return (
                BeginTheoremLikeToken(match.group(1), line_num, match.group(2), match.group(3)),
                match.span()[1],
            )

        match = re.match(r"(\\begin\s*{\s*(proof)\s*})", source_left)

        if match:
            return (
                BeginTheoremLikeToken(match.group(1), line_num, match.group(2), None),
                match.span()[1],
            )

        raise ParsingException()
