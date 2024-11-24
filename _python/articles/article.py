"""
class representing an article or similar entity
"""

from articles.entity_base import EntityBase
from html_writer.anchor import Anchor


class Article(EntityBase):
    def __init__(
        self,
        **kwargs,
    ) -> None:
        self.url: str = kwargs.pop("url")
        self.id_: str | None = kwargs.pop("id", None)
        self.press: str | None = kwargs.pop("press", None)
        super().__init__(**kwargs)

    @property
    def html_str(self) -> str:
        res: list[str] = list()

        a_attrs: dict[str, str] = dict(href=self.url)
        if self.id_ is not None:
            a_attrs["id"] = self.id_

        res.append("<li>")
        res.append(f"\t{Anchor(self.title, **a_attrs)}")
        if self.authors is not None:
            res.append(f"\t- {self.convert_comma_separated_str(self.authors)}")
        if self.press is not None:
            res.append(f"\t- {self.press}")
        if self.date_str is not None:
            res.append(f"\t@ {self.date_str}")
        if self.postfix is not None:
            for line in self.postfix:
                res.append(f"\t{line}")
        res.append("</li>")

        return "\n".join(res)
