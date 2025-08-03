"""
LaTeX element corresponding
- \\begin{itemize} ... \\end{itemize}
- \\begin{enumerate} ... \\end{enumerate}
- \\begin{description} ... \\end{description}
"""

from copy import copy

from latex_parser.latex_elements.latex_element_base import LaTeXElementBase
from latex_parser.latex_elements.item_element import ItemElement


class ItemizeElement(LaTeXElementBase):
    def __init__(self, item_list: list[ItemElement] | None = None) -> None:
        self.item_list: list[ItemElement] = list()

        if item_list:
            for item in item_list:
                self.add_item(item)

    def __repr__(self) -> str:
        return "\n".join([r"\BIT"] + ["\t" + str(item) for item in self.item_list] + [r"\EIT"])

    def add_item(self, item: ItemElement) -> None:
        self.item_list.append(copy(item))

    def to_markdown_str(self, indent: str = "") -> str:
        return "\n".join(
            [indent + "<ul>"]
            + [item.to_markdown_str(indent) for item in self.item_list]
            + [indent + "</ul>"]
        )
