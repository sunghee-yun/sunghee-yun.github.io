"""
Base class for LaTeX elements
"""

import re
from abc import ABC, abstractmethod


class LaTeXElementBase(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def to_markdown_str(self, indent: str = "") -> str:
        pass

    @staticmethod
    def process_markdown_string(string: str) -> str:
        string = re.sub(r"\\'(a|e|i|o|u|y)", r"\1&#769;", string, flags=re.IGNORECASE)
        string = re.sub(r"\\'{(a|e|i|o|u|y)}", r"\1&#769;", string, flags=re.IGNORECASE)
        string = re.sub(r'\\"(a|e|i|o|u|y)', r"\1&#776;", string, flags=re.IGNORECASE)
        string = re.sub(r'\\"{(a|e|i|o|u|y)}', r"\1&#776;", string, flags=re.IGNORECASE)
        return string
