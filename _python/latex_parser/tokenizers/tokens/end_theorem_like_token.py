"""
- \\end{myaxiom}
- \\end{mylaw}
- \\end{myprinciple}
- \\end{mydefinition}
- \\end{mytheorem}
- \\end{mylemma}
- \\end{myproposition}
- \\end{mycorollary}
- \\end{myconjecture}
- \\end{myinequality}
- \\end{myformula}
- \\end{myalgorithm}
"""

import re
from re import Match

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.keyword_base import KeywordBase
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase


class EndTheoremLikeToken(KeywordBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, env_name: str) -> None:
        super().__init__(string, line_num)
        self.env_name: str = env_name
        EndTheoremLikeToken.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(
            r"(\\end\s*{\s*(" + cls.REG_EXP_THEOREM_LIKE_NAMES + r")\s*})", source_left
        )
        if match:
            return EndTheoremLikeToken(match.group(1), line_num, match.group(2)), match.span()[1]

        match = re.match(r"(\\end\s*{\s*(proof)\s*})", source_left)
        if match:
            return EndTheoremLikeToken(match.group(1), line_num, match.group(2)), match.span()[1]

        raise ParsingException()
