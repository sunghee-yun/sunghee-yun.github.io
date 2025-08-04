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
from latex_parser.utils import make_label_consistent


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
    PROOF = "proof"


class TheoremLikeElement(LaTeXElementBase):
    def __init__(self, type_: TheoremLikeType, name: str | None, contents: LaTeXContents) -> None:
        self.type: TheoremLikeType = type_
        self.name: str | None = name
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
        assert self.name is not None or self.type == TheoremLikeType.PROOF, (self.name, self.type)

        id_str: str = (
            ""
            if self.name is None
            else f' id="{self.type.value}:{make_label_consistent(self.name)}"'
        )
        data_name_str: str = (
            ""
            if self.name is None
            else (
                f' data-name="{LaTeXElementBase.process_markdown_string(self.name)}"'
                if len(self.name) > 0
                else ""
            )
        )

        return "\n".join(
            [
                indent + f'<div class="{self.type.value}"{id_str}' + data_name_str + ">",
                self.contents.to_markdown_str(indent + "\t"),
                indent + "</div>",
            ]
        )
