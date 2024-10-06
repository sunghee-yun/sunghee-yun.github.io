"""
parse html to write to .json file
"""

import os
import json
from typing import Any

from articles.article import Article
from articles.article_collection import ArticleCollection

if __name__ == "__main__":
    article_collection: ArticleCollection = ArticleCollection()

    github_repo_root_dir: str = os.path.abspath(os.path.join(os.pardir, os.pardir))
    file_dir: str = os.path.join(github_repo_root_dir, "resource", "source-files")
    article_data: list[dict[str, Any]] = json.load(open(os.path.join(file_dir, "articles.json")))

    for article in article_data:
        article_collection.add_article(Article(**article))

    config_data: list[list] = json.load(open(os.path.join(file_dir, "config.json")))

    with open(os.path.join(github_repo_root_dir, "_pages", "ai-hub.md"), "w") as fid:
        fid.write(open(os.path.join(file_dir, "articles_heading.txt")).read())
        fid.write("\n")
        fid.write(article_collection.get_html_body(config_data))
        fid.write("\n")
