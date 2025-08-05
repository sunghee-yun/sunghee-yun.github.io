"""
foiltex to markdown conversion config
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict

import yaml


@dataclass
class FoiltexToMarkdownConversionConfig:
    """Configuration for the conversion process"""

    title: str
    date: str
    latex_source: str
    permalink: str
    categories: List[str]
    output_markdown: str
    tags: List[str] = field(default_factory=list)
    conditionals: Dict[str, bool] = field(default_factory=dict)
    def_tex: str | None = None
    foilhead_in_toc: bool = False
    notebooklm: dict[str, str] | None = None

    @classmethod
    def from_yaml(cls, yaml_file: Path):
        """Load configuration from YAML file"""
        with open(yaml_file, "r") as f:
            data = yaml.safe_load(f)
        return cls(**data)
