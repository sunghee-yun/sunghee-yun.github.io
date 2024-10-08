"""
class representing collection of articles
"""

from collections import defaultdict
from datetime import date
from logging import getLogger, Logger

from articles.article import Article
from html_writer.header import Header

logger: Logger = getLogger()


class ArticleCollection:
    TRANSLATION_TABLE: dict[str, str] = dict(ai="AI", agi="AGI", llm="LLM", genai="genAI")
    TRANSLATION_TABLE["ai in general"] = "AI in general"

    @staticmethod
    def capitalize(s: str) -> str:
        if len(s) < 1:
            return s

        return s[0].capitalize() + s[1:]

    def __init__(self) -> None:
        self.cat_articles_dict: dict[tuple[str, ...], list[Article]] = defaultdict(list)
        self.all_articles: list[Article] = list()

    def add_article(self, article: Article) -> None:
        self.cat_articles_dict[article.category].append(article)
        self.all_articles.append(article)

    def get_html_body(self, config: list[list]) -> str:
        res: list[str] = list()
        prev_cat: tuple[str, ...] = tuple()

        categories_not_in_config: set[tuple[str, ...]] = set(self.cat_articles_dict).difference(
            [tuple(x) for x in list(zip(*config))[0]]
        )
        if categories_not_in_config:
            categories_not_in_config_str: str = ", ".join(
                [str(y) for y in categories_not_in_config]
            )
            logger.warning(f"The articles in categories {categories_not_in_config_str} are ignore.")

        for category_title_map in config:
            current_cat: tuple[str, ...] = tuple(category_title_map[0])
            assert current_cat in self.cat_articles_dict, (
                list(self.cat_articles_dict.keys()),
                current_cat,
            )
            start_heading: bool = False

            for idx, heading_ in enumerate(current_cat):
                if not start_heading and (len(prev_cat) <= idx or prev_cat[idx] != heading_):
                    start_heading = True

                if start_heading:
                    if idx == len(current_cat) - 1:
                        heading_ = category_title_map[1]
                    heading__: str = self.TRANSLATION_TABLE.get(
                        heading_, self.capitalize(heading_) if idx <= 1 else heading_
                    )
                    res.append("")
                    res.append(
                        Header(idx + 1, heading__, id="-".join(current_cat[: idx + 1])).__repr__()
                    )
                    res.append("")
            prev_cat = current_cat

            res.append("<ul>")
            for article in sorted(
                self.cat_articles_dict[current_cat],
                key=lambda list_item: (
                    date(9999, 12, 13) if list_item.date is None else list_item.date
                ),
                reverse=True,
            ):
                res.append(article.html_str)
            res.append("</ul>")

        res.append(
            Header(
                1,
                "All articles in reverse chronicle order",
                id="all-articles-in-reverse-chronicl-order",
            ).__repr__()
        )

        res.append("<ul>")
        for article in sorted(
            self.all_articles,
            key=lambda list_item: (
                date(9999, 12, 13) if list_item.date is None else list_item.date
            ),
            reverse=True,
        ):
            if article.date is None:
                logger.warning(
                    "The below article not listed in the last section because date "
                    "is not specified."
                )
                logger.warning(f"- title: {article.title}")
                continue
            res.append(article.html_str)
        res.append("</ul>")

        return "\n".join(res)
