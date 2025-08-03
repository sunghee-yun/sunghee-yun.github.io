"""
Base class for figures, e.g., \\includegraphcs, \\pics, etc.
"""

from abc import ABC

from latex_parser.basic_latex_elements.latex_element_base import LaTeXElementBase


class FigureBase(LaTeXElementBase, ABC):
    pass
