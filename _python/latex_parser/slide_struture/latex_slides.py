"""
LaTeX slides
"""

from copy import copy

from latex_parser.slide_struture.slide import Slide
from latex_parser.slide_struture.slide_section import SlideSection


class LaTeXSlides:
    def __init__(self, front_page: Slide) -> None:
        self.front_page: Slide = copy(front_page)
        self.sections: list[SlideSection] = list()

    def add_section(self, section: SlideSection) -> None:
        self.sections.append(copy(section))
