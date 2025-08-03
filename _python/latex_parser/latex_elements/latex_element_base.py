"""
Base class for LaTeX elements
"""

from abc import ABC, abstractmethod


class LaTeXElementBase(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def to_markdown_str(self, indent: str = "") -> str:
        pass
