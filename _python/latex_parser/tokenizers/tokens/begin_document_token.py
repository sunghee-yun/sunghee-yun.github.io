"""
- \\begin{document}
"""

from latex_parser.tokenizers.tokens.keyword_base import KeywordBase


class BeginDocumentToken(KeywordBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        BeginDocumentToken.num_instances += 1
