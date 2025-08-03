"""
Math environment such as Theorem, Lemma, etc.
"""

from __future__ import annotations

import re

from latex_parser.basic_latex_elements.env_base import LaTeXEnvBase


class MathEnvironment(LaTeXEnvBase):
    """Handles mathematical environments like mytheorem, mydefinition"""

    ENV_TYPE_MAP = {
        "mytheorem": "theorem",
        "mydefinition": "definition",
        "mylemma": "lemma",
        "mycorollary": "corollary",
        "myproposition": "proposition",
        "myinequality": "inequality",
        "myaxiom": "axiom",
        "mylaw": "law",
        "myprinciple": "principle",
        "myformula": "formula",
        "myalgorithm": "algorithm",
        "myproof": "proof",
    }

    def __init__(self, env_type: str, title: str, content: str):
        self.env_type = env_type
        self.title = title
        self.css_class = self.ENV_TYPE_MAP.get(env_type, env_type.replace("my", ""))
        label = self.generate_label(title, self.css_class)
        super().__init__(content, label)

    def generate_label(self, title: str, env_type: str) -> str:
        """Generate label like theorem:fundamental-theorem-of-arithmetic"""
        clean_title = re.sub(r"[^\w\s-]", "", title.lower())
        clean_title = re.sub(r"\s+", "-", clean_title.strip())
        return f"{env_type}:{clean_title}"

    def to_markdown(self) -> str:
        return f'<div class="{self.css_class}" id="{self.label}">\n{self.content}\n</div>'
