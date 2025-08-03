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

from latex_parser.tokenizers.tokens.keyword_base import KeywordBase


class BeginTheoremLikeToken(KeywordBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, env_name: str, name: str) -> None:
        super().__init__(string, line_num)
        self.env_name: str = env_name
        self.name: str = name
        BeginTheoremLikeToken.num_instances += 1
