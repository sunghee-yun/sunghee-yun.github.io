"""
LaTeX contents
"""

from copy import copy

from latex_parser.latex_elements.latex_element_base import LaTeXElementBase


class LaTeXContents(LaTeXElementBase):
    def __init__(self, latex_element_list: list[LaTeXElementBase] | None = None) -> None:
        self.element_list: list[LaTeXElementBase] = list()

        if latex_element_list:
            for element in latex_element_list:
                self.add_element(element)

    def __repr__(self) -> str:
        return "".join([str(element) for element in self.element_list])

    def add_element(self, element: LaTeXElementBase) -> None:
        self.element_list.append(copy(element))

    def to_markdown_str(self, indent: str = "") -> str:
        return indent + "".join([element.to_markdown_str(indent) for element in self.element_list])
