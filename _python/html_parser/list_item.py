"""
<li> ... </li> in html
"""

from __future__ import annotations

import re
from datetime import date, datetime
from re import Match

from bs4 import PageElement


class ListItem:
    def __init__(self, header_str_list: list[str], li: PageElement) -> None:
        self.header_str_list: list[str] = header_str_list.copy()
        self.li: PageElement = li
        self.date: date | None = self.parse_date(self.li)

    @classmethod
    def extract_lis(cls, element: PageElement, li_list_: list[ListItem]) -> None:

        if element.name == "li":  # type:ignore
            li_list_.append(ListItem(["A", "B"], element))
            return

        if element.name:  # type:ignore
            pass
            # print(f"{indent_str}<{element.name}>")

        # Print attributes if they exist (like href in <a>)
        if element.attrs:  # type:ignore
            for attr, value in element.attrs.items():  # type:ignore
                pass
                # print(f"{indent_str}  {attr}: {value}")

        # Loop over the children elements
        for child in element.children:  # type:ignore
            if child.name:  # If the child is a tag, recursively print its structure
                cls.extract_lis(child, li_list_)
                # print_structure(child, indent + 2)
            elif child.strip():  # If it's a string and not just whitespace, print it
                pass
                # print(f"{indent_str}  {child.strip()}")

        # Close the tag (not necessary but adds clarity)
        if element.name:  # type:ignore
            pass
            # print(f"{indent_str}</{element.name}>")

    @classmethod
    def parse_date(cls, element: PageElement) -> date | None:
        for child in element.children:  # type:ignore
            if child.name:  # If the child is a tag, recursively print its structure
                res: date | None = cls.parse_date(child)
                if res is not None:
                    return res
            elif child.strip():  # If it's a string and not just whitespace, print it
                match: Match | None = re.match(r".*[^\d](\d\d?-\w\w\w-\d\d\d\d)", child.strip())
                if match is not None:
                    return datetime.strptime(match.group(1), "%d-%b-%Y").date()
        return None
