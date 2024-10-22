"""
class representing a paper or similar entity
"""

from articles.entity_base import EntityBase
from html_writer.anchor import Anchor


class Paper(EntityBase):
    def __init__(
        self,
        **kwargs,
    ) -> None:
        self.url: dict[str, str] | None = kwargs.pop("url", None)
        self.authors: str | None = kwargs.pop("authors", None)
        self.org: str | None = kwargs.pop("org", None)
        super().__init__(**kwargs)

    @property
    def html_str(self) -> str:
        res: list[str] = list()

        # attrs: dict[str, str] = dict(href=self.url)
        # if self.id_ is not None:
        #     attrs["id"] = self.id_
        # attrs_str: str = " ".join(f'{key}="{val}"' for key, val in attrs.items())

        res.append("<li>")
        res.append(f'\t"{self.title}"')

        if self.authors is not None:
            author_str: str = self.authors.strip()
            author_names: list[str] = [author.strip() for author in self.authors.split(",")]
            if len(author_names) > 1:
                author_str = ", ".join(author_names[:-1]) + " &amp; " + author_names[-1]
            res.append(f"\t- {author_str}")
        if self.org is not None:
            res.append(f"\t({self.org})")
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
