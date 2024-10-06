"""
class representing collection of articles
"""

from collections import defaultdict
from datetime import date

from articles.article import Article


class ArticleCollection:
    def __init__(self) -> None:
        self.cat_articles_dict: dict[tuple[str, ...], list[Article]] = defaultdict(list)
        self.all_articles: list[Article] = list()

    def add_article(self, article: Article) -> None:
        self.cat_articles_dict[article.category].append(article)
        self.all_articles.append(article)

    def get_html_body(self, config: list[list]) -> str:
        res: list[str] = list()
        prev_cat: tuple[str, ...] = tuple()

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
                    heading__: str = (
                        "AI"
                        if heading_ == "ai"
                        else (
                            "AGI"
                            if heading_ == "agi"
                            else (
                                "LLM"
                                if heading_ == "llm"
                                else (
                                    "genAI"
                                    if heading_ == "genai"
                                    else heading_.capitalize() if idx <= 1 else heading_
                                )
                            )
                        )
                    )
                    res.append(
                        f'<h{idx+1} id="{"-".join(current_cat[:idx+1])}">"'
                        f"\n\t{heading__}\n</h{idx+1}>"
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

        res.append('<h1 id="all-articles-in-reverse-chronicl-order">')
        res.append("\tAll articles in reverse chronicle order")
        res.append("</h1>")

        res.append("<ul>")
        for article in sorted(
            self.all_articles,
            key=lambda list_item: (
                date(9999, 12, 13) if list_item.date is None else list_item.date
            ),
            reverse=True,
        ):
            if article.date is None:
                continue
            res.append(article.html_str)
        res.append("</ul>")

        return "\n".join(res)
