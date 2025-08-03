"""
LaTeX element corresponding
- \\begin{itemize} ... \\end{itemize}
- \\begin{enumerate} ... \\end{enumerate}
- \\begin{description} ... \\end{description}
"""

from copy import copy

from latex_parser.latex_elements.latex_contents import LaTeXContents
from latex_parser.latex_elements.latex_element_base import LaTeXElementBase


class ItemElement(LaTeXElementBase):
    def __init__(self, contents: LaTeXContents, opt_arg: str | None = None) -> None:
        self.contents: LaTeXContents = copy(contents)
        self.opt_arg: str | None = opt_arg

    def __repr__(self) -> str:
        return r"\item " + str(self.contents)

    def to_markdown_str(self, indent: str = "") -> str:
        return "\n".join(
            [
                indent + "<li>",
                self.contents.to_markdown_str(indent + "\t"),
                indent + "</li>",
            ]
        )
