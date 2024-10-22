"""
base class for all html tags
"""

from abc import ABC, abstractmethod

from html_writer.contents import Contents


class TagBase(ABC):
    def __init__(self, tag_name: str, contents: Contents | str, /, **kwargs) -> None:
        self.tag_name: str = tag_name
        self.attrs: dict[str, str] = kwargs.copy()
        self.contents: Contents = contents if isinstance(contents, Contents) else Contents(contents)

        self._check_attrs()

    @abstractmethod
    def _check_attrs(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"<{self.tag_name} {self.attrs_str}>{self.contents}</{self.tag_name}>"

    @property
    def attrs_str(self) -> str:
        return " ".join([f'{name}="{value}"' for name, value in self.attrs.items()])
