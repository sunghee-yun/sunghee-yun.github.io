"""
LaTeX document source
"""

from copy import copy

from latex_parser.latex_elements.latex_contents import LaTeXContents


class LaTeXDocument:
    def __init__(self, preamble: LaTeXContents, document_body: LaTeXContents) -> None:
        self.preamble: LaTeXContents = copy(preamble)
        self.document_body: LaTeXContents = copy(document_body)
