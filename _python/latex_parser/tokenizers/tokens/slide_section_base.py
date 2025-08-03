"""
Base class for \\TITLEFOIL, \\titlefoil, and \\myfoilhead
"""

from abc import ABC

from latex_parser.tokenizers.tokens.keyword_base import KeywordBase


class SlideSectionBase(KeywordBase, ABC):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, title: str, label: str) -> None:
        super().__init__(string, line_num)
        self.title: str = title
        self.label: str = label
        SlideSectionBase.num_instances += 1
