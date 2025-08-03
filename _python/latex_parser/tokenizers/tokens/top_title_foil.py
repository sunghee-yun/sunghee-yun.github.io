"""
\\TITLEFOIL
"""

from latex_parser.tokenizers.tokens.slide_section_base import SlideSectionBase


class TopTitleFoil(SlideSectionBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, title: str, label: str) -> None:
        super().__init__(string, line_num, title, label)
        TopTitleFoil.num_instances += 1
