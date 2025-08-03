"""
LaTeX element corresponding LaTeX token
"""

from copy import copy

from latex_parser.latex_elements.latex_element_base import LaTeXElementBase
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase


class TokenElement(LaTeXElementBase):
    def __init__(self, token: LaTeXTokenBase) -> None:
        self.token: LaTeXTokenBase = copy(token)

    def __repr__(self) -> str:
        return str(self.token)

    def to_markdown_str(self, indent: str = "") -> str:
        return self.token.markdown_str
