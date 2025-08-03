"""
- \\begin{itemize}
"""

from latex_parser.tokenizers.tokens.keyword_base import KeywordBase


class BeginItemizeToken(KeywordBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        BeginItemizeToken.num_instances += 1
