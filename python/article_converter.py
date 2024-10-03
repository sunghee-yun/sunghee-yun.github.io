"""
parse html and write to articles.md file for my blog
"""

import os
import re
from typing import Match
from datetime import date, datetime
from bs4 import BeautifulSoup
from bs4.element import Tag


class ListItem:
    def __init__(self, header_str_list: list[str], li: Tag) -> None:
        self.header_str_list: list[str] = header_str_list.copy()
        self.li: Tag = li
        self.date: date | None = parse_date(self.li)


# Recursively print the structure with indentation
def parse_date(element: Tag) -> date | None:
    # Loop over the children elements
    for child in element.children:
        if child.name:  # If the child is a tag, recursively print its structure
            res: date | None = parse_date(child)
            if res is not None:
                return res
        elif child.strip():  # If it's a string and not just whitespace, print it
            match: Match = re.match(r".*[^\d](\d\d?-\w\w\w-\d\d\d\d)", child.strip())
            if match is not None:
                return datetime.strptime(match.group(1), "%d-%b-%Y").date()
    return None


def print_structure(element: Tag, indent: int = 0):
    # Create indentation for structure levels
    indent_str = " " * indent

    # Print the current tag
    if element.name:
        print(f"{indent_str}<{element.name}>")

    # Print attributes if they exist (like href in <a>)
    if element.attrs:
        for attr, value in element.attrs.items():
            print(f"{indent_str}  {attr}: {value}")

    # Loop over the children elements
    for child in element.children:
        if child.name:  # If the child is a tag, recursively print its structure
            print_structure(child, indent + 2)
        elif child.strip():  # If it's a string and not just whitespace, print it
            print(f"{indent_str}  {child.strip()}")

    # Close the tag (not necessary but adds clarity)
    if element.name:
        print(f"{indent_str}</{element.name}>")


def extract_lis(element: Tag, li_list_: list[ListItem]) -> None:

    if element.name == "li":
        li_list_.append(ListItem(["A", "B"], element))
        return

    if element.name:
        pass
        # print(f"{indent_str}<{element.name}>")

    # Print attributes if they exist (like href in <a>)
    if element.attrs:
        for attr, value in element.attrs.items():
            pass
            # print(f"{indent_str}  {attr}: {value}")

    # Loop over the children elements
    for child in element.children:
        if child.name:  # If the child is a tag, recursively print its structure
            extract_lis(child, li_list_)
            # print_structure(child, indent + 2)
        elif child.strip():  # If it's a string and not just whitespace, print it
            pass
            # print(f"{indent_str}  {child.strip()}")

    # Close the tag (not necessary but adds clarity)
    if element.name:
        pass
        # print(f"{indent_str}</{element.name}>")


if __name__ == "__main__":
    github_repo_root_dir: str = os.path.abspath(os.pardir)
    html_file_path: str = os.path.join(
        github_repo_root_dir, "resource/source-files", "articles.html"
    )

    html_content: str = open(html_file_path).read()

    soup = BeautifulSoup(html_content, "html.parser")

    # Print the full HTML structure
    # print_structure(soup)

    li_list: list[ListItem] = list()
    extract_lis(soup, li_list)

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

        write(str(soup))

        write("")

        write('<h1 id="all-articles">All articles in reverse chronicle order</h1>')
        write("<ul>")
        for list_item in li_list:
            write(str(list_item.li))
        write("</ul>")
