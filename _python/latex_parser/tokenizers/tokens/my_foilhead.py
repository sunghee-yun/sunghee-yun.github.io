"""
\\myfoilhead
"""

from latex_parser.tokenizers.tokens.slide_section_base import SlideSectionBase


class MyFoilhead(SlideSectionBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, title: str, label: str | None = None) -> None:
        super().__init__(
            string,
            line_num,
            title,
            f"my-foilhead-{MyFoilhead.num_instances}" if label is None else label,
        )
        MyFoilhead.num_instances += 1
