"""
Base class for itemize-like envs,
e.g.,
- itemize env
- enumerate env
- description env
"""

from abc import abstractmethod

from latex_parser.basic_latex_elements.env_base import LaTeXEnvBase
from latex_parser.basic_latex_elements.latex_body import LaTeXBody


class ItemizeEnvBase(LaTeXEnvBase):
    def __init__(self, content: str, label: str | None) -> None:
        super().__init__(content, label)
        self.str_list: list[str] = list()
        self.latex_body_list: list[LaTeXBody] = list()

    @property
    @abstractmethod
    def html_tag(self) -> str:
        pass

    def add_item(self, item_content: str, is_vitem: bool = False):
        # \vitem just adds vertical space in slides, treat as \item in markdown
        self.str_list.append(item_content)

    def finalize(self) -> None:
        assert len(self.latex_body_list) == 0, (self.latex_body_list, len(self.latex_body_list))
        for item in self.str_list:
            self.latex_body_list.append(LaTeXBody.create_latex_body_from_str_list(item.split("\n")))

    def to_markdown(self) -> str:
        assert len(self.latex_body_list) > 0

        res: list[str] = list()

        res.append(f"<{self.html_tag}>")
        for latex_body in self.latex_body_list:
            res.append("<li>")
            res.append(latex_body.to_markdown())
            res.append("</li>")

        res.append(f"</{self.html_tag}>")

        return "\n".join(res)
