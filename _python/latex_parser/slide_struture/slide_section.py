"""
(slide) section corresponding to \\TITLEFOIL
"""

from copy import copy
from latex_parser.slide_struture.slide_subsection import SlideSubsection


class SlideSection:
    def __init__(self) -> None:
        self.subsections: list[SlideSubsection] = list()

    def add_subsection(self, subsection: SlideSubsection) -> None:
        self.subsections.append(copy(subsection))
