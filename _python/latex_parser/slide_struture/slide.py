"""
one slide, to be more precise, what corresponds to \\myfoilhead (or \\foilhead)
"""

from copy import copy
from latex_parser.slide_struture.basic_element_collection import BasicElementCollection


class Slide:
    def __init__(self, element_collection: BasicElementCollection) -> None:
        self.element_collection: BasicElementCollection = copy(element_collection)
