"""
html tag <a>... </a>
"""

from html_writer.tag_base import TagBase
from html_writer.contents import Contents


class Anchor(TagBase):
    def __init__(self, contents: Contents | str, /, **kwargs) -> None:
        super().__init__("a", contents, **kwargs)

    def _check_attrs(self) -> None:
        assert "href" in self.attrs
