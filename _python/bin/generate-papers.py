"""
write AI paper page on .markdown file
"""

import os
import json
from typing import Any

from articles.paper import Paper
from articles.entity_collection import EntityCollection
from html_writer.anchor import Anchor

if __name__ == "__main__":
    paper_collection: EntityCollection = EntityCollection("paper")

    github_repo_root_dir: str = os.path.abspath(os.path.join(os.pardir, os.pardir))
    file_dir: str = os.path.join(github_repo_root_dir, "resource", "source-files")
    paper_data: list[dict[str, Any]] = json.load(open(os.path.join(file_dir, "papers.json")))

    for paper in paper_data:
        paper_collection.add_article(Paper(**paper))

    config_data: list[list] = json.load(open(os.path.join(file_dir, "config-papers.json")))

    all_papers_str: str = "All papers in reverse chronological order"
    all_papers_id: str = "all-papers-in-reverse-chronological-order"
    with open(os.path.join(github_repo_root_dir, "_pages", "ai-papers.md"), "w") as fid:
        fid.write(open(os.path.join(file_dir, "papers_heading.txt")).read())
        fid.write(Anchor(all_papers_str, href=f"#{all_papers_id}").__str__())
        fid.write("\n")
        fid.write(paper_collection.get_html_body(config_data, all_papers_str, all_papers_id))
        fid.write("\n")
