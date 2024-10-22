"""
parse html and write to articles.md file for my blog
"""

from __future__ import annotations

import os
from datetime import date
from bs4 import BeautifulSoup

from html_parser.list_item import ListItem

if __name__ == "__main__":
    github_repo_root_dir: str = os.path.abspath(os.pardir)
    html_file_path: str = os.path.join(
        github_repo_root_dir, "resource", "source-files", "articles.html"
    )

    html_content: str = open(html_file_path).read()

    soup = BeautifulSoup(html_content, "html.parser")

    # Print the full HTML structure
    # print_structure(soup)

    li_list: list[ListItem] = list()
    ListItem.extract_lis(soup, li_list)

    li_list.sort(
        key=lambda list_item: date(9999, 12, 13) if list_item.date is None else list_item.date,
        reverse=True,
    )

    output_file_path: str = os.path.join(github_repo_root_dir, "_pages", "articles.md")
    with open(output_file_path, "w") as fid:

        def write(s: str) -> None:
            fid.write(s + "\n")

        write("---")
        write("layout: single")
        write("title: Articles")
        write("permalink: /articles")
        write("toc: true")
        write('toc_label: "ToC"')
        write('toc_icon: "cog"')
        write("toc_sticky: true")
        write("---")
        write("")

        write('(<a href="#all-articles">all articles in reverse chronicle order</a>)')

        write(str(soup))

        write("")

        write('<h1 id="all-articles">All articles in reverse chronicle order</h1>')
        write("<ul>")
        for list_item in li_list:
            if list_item.date is None:
                continue
            write(str(list_item.li))
        write("</ul>")
