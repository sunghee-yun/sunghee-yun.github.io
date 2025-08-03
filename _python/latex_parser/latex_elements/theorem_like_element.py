"""
- \\begin{myaxiom}{...} ... \\end{myaxiom}
- \\begin{mylaw}{...} ... \\end{mylaw}
- \\begin{myprinciple}{...} ... \\end{myprinciple}
- \\begin{mydefinition}{...} ... \\end{mydefinition}
- \\begin{mytheorem}{...} ... \\end{mytheorem}
- \\begin{mylemma}{...} ... \\end{mylemma}
- \\begin{myproposition}{...} ... \\end{myproposition}
- \\begin{mycorollary}{...} ... \\end{mycorollary}
- \\begin{myconjecture}{...} ... \\end{myconjecture}
- \\begin{myinequality}{...} ... \\end{myinequality}
- \\begin{myformula}{...} ... \\end{myformula}
- \\begin{myalgorithm}{...} ... \\end{myalgorithm}
"""

from copy import copy
from enum import Enum

from latex_parser.latex_elements.latex_contents import LaTeXContents
from latex_parser.latex_elements.latex_element_base import LaTeXElementBase


class TheoremLikeType(Enum):
    AXIOM = "axiom"
    LAW = "law"
    PRINCIPLE = "principle"
    DEFINITION = "definition"
    THEOREM = "theorem"
    LEMMA = "lemma"
    PROPOSITION = "proposition"
    COROLLARY = "corollary"
    CONJECTURE = "conjecture"
    INEQUALITY = "inequality"
    FORMULA = "formula"
    ALGORITHM = "algorithm"


class TheoremLikeElement(LaTeXElementBase):
    def __init__(self, type_: TheoremLikeType, name: str, contents: LaTeXContents) -> None:
        self.type: TheoremLikeType = type_
        self.name: str = name
        self.contents: LaTeXContents = copy(contents)

    def __repr__(self) -> str:
        return "\n".join(
            [
                r"\begin{my" + self.type.value + "} ",
                str(self.contents),
                r"\end{my" + self.type.value + "} ",
            ]
        )

    def to_markdown_str(self, indent: str = "") -> str:
        return "\n".join(
            [
                indent
                + f'<div class="{self.type.value}" id="{self.type.value}:{self.name}"'
                + (f' data-name="{self.name}"' if len(self.name) > 0 else "")
                + ">",
                self.contents.to_markdown_str(indent + "\t"),
                indent + "</div>",
            ]
        )
