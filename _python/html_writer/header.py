"""
html header, i.e., h1, h2, h3, ..., h6
"""

from html_writer.tag_base import TagBase
from html_writer.contents import Contents


class Header(TagBase):
    def __init__(self, level: int, contents: Contents | str, /, **kwargs) -> None:
        assert level >= 1 and level <= 6, level
        super().__init__(f"h{level}", contents, **kwargs)

    def _check_attrs(self) -> None:
        pass
