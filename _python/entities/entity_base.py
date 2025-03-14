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
        self.authors: str | None = kwargs.pop("authors", None)
        self.date_str: str | None = kwargs.pop("date", None)
        self.date: date | None = (
            None
            if self.date_str is None
            else datetime.strptime(
                re.match(r"(\d\d?-\w\w\w-\d\d\d\d)", self.date_str).group(1),  # type:ignore
                "%d-%b-%Y",
            ).date()
        )
        self.last_revised_str: str | None = kwargs.pop("last_revised", None)
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

    @staticmethod
    def convert_comma_separated_str(names: str) -> str:
        names_str: str = names.strip()
        name_str_list: list[str] = [name.strip() for name in names.split(",")]
        if len(name_str_list) > 1:
            names_str = ", ".join(name_str_list[:-1]) + " &amp; " + name_str_list[-1]
        return names_str
