"""
colleciton of non-section LaTeX (slide) elements
"""

from copy import copy
from latex_parser.latex_elements.latex_element_base import LaTeXElementBase


class BasicElementCollection:
    def __init__(self) -> None:
        self.elements: list[LaTeXElementBase] = list()

    def add_element(self, element: LaTeXElementBase) -> None:
        self.elements.append(copy(element))
