"""
Latex parser to markdown converter
"""

from latex_parser.latex_elements.foiltex_section_element import FoiltexSectionElement
from latex_parser.latex_elements.latex_document import LaTeXDocument
from latex_parser.latex_elements.latex_element_base import LaTeXElementBase
from latex_parser.tokenizers.tokens.my_foilhead import MyFoilhead
from latex_parser.tokenizers.tokens.top_title_foil import TopTitleFoil


class LatexParserToMarkdownConverter:
    def __init__(self, latex_document: LaTeXDocument) -> None:
        self.latex_document: LaTeXDocument = latex_document
        self._markdown_str: str = ""
        self._markdown_converted: bool = False

    @property
    def markdown_str(self) -> str:
        if not self._markdown_converted:
            active_element_list: list[LaTeXElementBase] = list()

            mute_mode: bool = False
            first_section: FoiltexSectionElement | None = None
            for element in self.latex_document.document_body.element_list:
                if mute_mode and isinstance(element, FoiltexSectionElement):
                    mute_mode = False

                if mute_mode:
                    continue

                if isinstance(element, FoiltexSectionElement):
                    if (
                        r"\talktitle" in element.token.title  # type:ignore
                        or element.token.title  # type:ignore
                        == "Navigating Mathematical and Statistical Territories"
                    ):
                        assert isinstance(element.token, MyFoilhead), element.token.__class__
                        mute_mode = True
                        continue

                    if (
                        isinstance(element.token, TopTitleFoil)
                        and element.token.title == "References"
                    ):
                        break

                active_element_list.append(element)

                if first_section is None and isinstance(element, FoiltexSectionElement):
                    first_section = element

            self._markdown_str = "".join(
                [element.to_markdown_str() for element in active_element_list]
            )

            if first_section is None or first_section.level > 2:
                self._markdown_str = "\n## Preamble\n" + self._markdown_str

            if first_section is None or first_section.level > 1:
                self._markdown_str = "\n# Introduction\n" + self._markdown_str

            self._markdown_converted = True

        return self._markdown_str
