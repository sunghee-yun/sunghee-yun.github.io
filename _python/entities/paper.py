"""
class representing a paper or similar entity
"""

from entities.entity_base import EntityBase
from html_writer.anchor import Anchor


class Paper(EntityBase):
    def __init__(
        self,
        **kwargs,
    ) -> None:
        self.url: dict[str, str] | None = kwargs.pop("url", None)
        self.org: str | None = kwargs.pop("org", None)
        self.id_: str | None = kwargs.pop("id", None)
        self.journal: str | None = kwargs.pop("journal", None)
        self.conference: str | None = kwargs.pop("conference", None)
        super().__init__(**kwargs)

    @property
    def html_str(self) -> str:
        res: list[str] = list()

        # attrs: dict[str, str] = dict(href=self.url)
        # if self.id_ is not None:
        #     attrs["id"] = self.id_
        # attrs_str: str = " ".join(f'{key}="{val}"' for key, val in attrs.items())

        res.append("<li>" if self.id_ is None else f'<li id="{self.id_}">')
        res.append(f'\t"{self.title}"')

        if self.journal is not None:
            res.append(f"\t@ {self.journal}")
        if self.conference is not None:
            res.append(f"\t@ {self.conference}")
        if self.authors is not None:
            res.append(f"\t- {self.convert_comma_separated_str(self.authors)}")
        if self.org is not None:
            res.append(f"\t({self.convert_comma_separated_str(self.org)})")
        if self.date_str is not None:
            res.append(f"\t@ {self.date_str}")
        if self.url is not None:
            res.append(
                "\t("
                + ", ".join([str(Anchor(name, href=url)) for name, url in self.url.items()])
                + ")"
            )

        if self.postfix is not None:
            for line in self.postfix:
                res.append(f"\t{line}")
        res.append("</li>")

        return "\n".join(res)
