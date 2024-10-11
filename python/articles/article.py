"""
class representing an article or similar entity
"""

import re
from datetime import date, datetime


class Article:
    def __init__(
        self,
        **kwargs,
    ) -> None:
        self._category: list[str] | list[list[str]] = kwargs.pop("category")
        self.title: str = kwargs.pop("title")
        self.url: str = kwargs.pop("url")
        self.id_: str | None = kwargs.pop("id", None)
        self.press: str | None = kwargs.pop("press", None)
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
            else [tuple(self._category)]
        )

    @property
    def html_str(self) -> str:
        res: list[str] = list()

        attrs: dict[str, str] = dict(href=self.url)
        if self.id_ is not None:
            attrs["id"] = self.id_
        attrs_str: str = " ".join(f'{key}="{val}"' for key, val in attrs.items())

        res.append("<li>")
        res.append(f"\t<a {attrs_str}>")
        res.append(f"\t\t{self.title}")
        res.append("\t</a>")
        if self.press is not None:
            res.append(f"\t- {self.press}")
        if self.date_str is not None:
            res.append(f"\t@ {self.date_str}")
        if self.postfix is not None:
            for line in self.postfix:
                res.append(f"\t{line}")
        res.append("</li>")

        return "\n".join(res)
