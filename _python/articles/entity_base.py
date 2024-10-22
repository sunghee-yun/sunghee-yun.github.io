"""
base class for article or paper
"""

from abc import ABC, abstractmethod
from datetime import date, datetime
import re


class EntityBase(ABC):
    def __init__(self, **kwargs) -> None:
        self._category: list[str] | list[list[str]] = kwargs.pop("category")
        self.title: str = kwargs.pop("title")
        self.date_str: str | None = kwargs.pop("date", None)
        self.date: date | None = (
            None
            if self.date_str is None
            else datetime.strptime(
                re.match(r"(\d\d?-\w\w\w-\d\d\d\d)", self.date_str).group(1),  # type:ignore
                "%d-%b-%Y",
            ).date()
        )
        self.postfix: list[str] | None = kwargs.pop("postfix", None)

        assert len(kwargs) == 0, kwargs

        self.categories: list[tuple[str, ...]] = (
            [tuple(category) for category in self._category]
            if isinstance(self._category[0], list)
            else [tuple(self._category)]  # type:ignore
        )

    @property
    @abstractmethod
    def html_str(self) -> str:
        pass
