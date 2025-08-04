"""
base class for LaTeX source tokens
"""

from __future__ import annotations

from abc import ABC
from logging import Logger, getLogger

from utils import get_all_subclasses

logger: Logger = getLogger()


class LaTeXTokenBase(ABC):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int) -> None:
        self.string: str = string
        self.line_num: int = line_num
        LaTeXTokenBase.num_instances += 1

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} - `{self.abbr_string}` @ {self.line_num}"

    @property
    def markdown_str(self) -> str:
        return self.string

    @property
    def abbr_string(self) -> str:
        return self.string

    @classmethod
    def log_statistics(cls) -> None:
        for subclass in sorted(
            [cls] + list(get_all_subclasses(LaTeXTokenBase)),
            key=lambda x: (x.num_instances, x.__name__),
        ):
            logger.info(f"{subclass.__name__} - {subclass.num_instances} instance")
