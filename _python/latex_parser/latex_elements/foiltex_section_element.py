"""
my foiltex section element, e.g., \\TITLEFOIL, \\titlefoil, \\myfoilhead
"""

from latex_parser.latex_elements.latex_element_base import LaTeXElementBase
from latex_parser.latex_elements.token_element import TokenElement
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.tokens.slide_section_base import SlideSectionBase
from latex_parser.tokenizers.tokens.title_foil import TitleFoil
from latex_parser.tokenizers.tokens.top_title_foil import TopTitleFoil


class FoiltexSectionElement(TokenElement):
    def __init__(self, token: LaTeXTokenBase) -> None:
        assert isinstance(token, SlideSectionBase), token.__class__
        super().__init__(token)

        self.level: int = 3
        if isinstance(self.token, TitleFoil):
            self.level = 2
        if isinstance(self.token, TopTitleFoil):
            self.level = 1

    def to_markdown_str(self, indent: str = "") -> str:
        assert isinstance(self.token, SlideSectionBase), self.token.__class__
        if self.level >= 3 and len(self.token.title) == 0:
            return "\n\n"

        assert len(self.token.title) > 0

        title: str = LaTeXElementBase.process_markdown_string(self.token.title)

        if self.level >= 3:
            return f"\n<h{self.level}>" + f"{title}</h{self.level}>\n"

        return f'\n<h{self.level} id="{self.token.label}">' + f"{title}</h{self.level}>\n"
