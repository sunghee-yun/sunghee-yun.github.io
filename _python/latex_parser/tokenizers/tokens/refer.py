"""
Base class for LaTeX commands
"""

from __future__ import annotations

import re
from re import Match

from latex_parser.tokenizers.tokens.keyword_base import KeywordBase
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.utils import make_label_consistent


class Refer(KeywordBase):
    num_instances: int = 0

    REG_EXP_THEOREM_LIKE_NAME_NAMES: str = "|".join(
        [f"{name[2:]}name" for name in KeywordBase.THEOREM_LIKE_NAMES]
    )

    def __init__(
        self,
        string: str,
        line_num: int,
        theorem_type: str,
        label: str,
    ) -> None:
        super().__init__(string, line_num)
        self.theorem_type: str = theorem_type
        self.label: str = label
        Refer.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(
            rf"(\\({cls.REG_EXP_THEOREM_LIKE_NAME_NAMES})" + r"~\\ref{(.*?)})",
            source_left,
        )
        if match is None:
            raise ParsingException()

        return (
            Refer(match.group(1), line_num, match.group(2)[:-4], match.group(3)),
            match.span()[1],
        )

    @property
    def markdown_str(self) -> str:
        return f'<a href="#{make_label_consistent(self.label)}"></a>'
