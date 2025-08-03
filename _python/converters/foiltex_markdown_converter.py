"""
foiltex to markdown converter
"""

import os
import time
from collections import OrderedDict
from logging import Logger, getLogger
from pathlib import Path

import yaml

from converters.foiltex_markdown_conversion_config import (
    FoiltexToMarkdownConversionConfig,
)
from converters.latex_parser_to_markdown_converter import LatexParserToMarkdownConverter
from latex_parser.conditional_processor import LaTeXConditionalProcessor
from latex_parser.latex_parser import LaTeXParser

logger: Logger = getLogger()


class LaTeXToMarkdownConverter:
    """Main converter class that orchestrates the conversion process"""

    def __init__(self, config: FoiltexToMarkdownConversionConfig) -> None:
        self.config = config

    def convert_to_markdown(self, tex_file: Path) -> None:
        logger.info(f"Starting conversion of {tex_file}")

        with open(tex_file, "r", encoding="utf-8") as fid:
            content = fid.read()

        lcp: LaTeXConditionalProcessor = LaTeXConditionalProcessor(self.config.conditionals)
        extracted_tex: str = lcp.process_document(content)

        tmp_tex_filepath: str = os.path.join(
            os.curdir,
            os.path.splitext(os.path.split(self.config.output_markdown)[1])[0] + ".tex",
        )

        with open(tmp_tex_filepath, "w") as fid:
            fid.write(extracted_tex)

        latex_parser: LaTeXParser = LaTeXParser(extracted_tex)

        latex_parser_to_markdown_converter: LatexParserToMarkdownConverter = (
            LatexParserToMarkdownConverter(latex_parser.parse())
        )

        defs: str = ""
        if self.config.def_tex:
            with open(self.config.def_tex, "r", encoding="utf-8") as fid:
                defs = fid.read()

        with open(self.config.output_markdown, "w") as fid:
            assert len(defs.split("\n")[-1]) == 0, "|" + defs.split("\n")[-1] + "|"
            fid.write(self.front_matter + "\n\n")
            fid.write(self.preamble + "\n\n")
            fid.write("$$\n")
            fid.write("\n".join([f"\t{def_}" for def_ in defs.split("\n")[:-1]]) + "\n")
            fid.write("$$\n")
            fid.write(latex_parser_to_markdown_converter.markdown_str)

    @property
    def front_matter(self) -> str:
        """Generate Jekyll front matter"""
        front_matter_ = OrderedDict(
            [
                ("title", self.config.title),
                ("date", self.config.date),
                ("last_modified_at", time.strftime("%a %b %_d %H:%M:%S %Z %Y")),
                ("permalink", self.config.permalink),
                ("categories", self.config.categories),
                ("tags", self.config.tags),
                ("toc", True),
                ("toc_label", "&nbsp;Table of Contents"),
                ("toc_icon", "fa-solid fa-list"),
                ("toc_sticky", True),
                ("usemathjax", True),
            ]
        )

        def represent_ordereddict(dumper, data):
            return dumper.represent_dict(data.items())

        yaml.add_representer(OrderedDict, represent_ordereddict)

        yaml_content = yaml.dump(front_matter_, default_flow_style=False)
        return f"---\n{yaml_content}---"

    @property
    def preamble(self) -> str:
        return "\n".join(
            [
                'posted: {{page.date | date: "%d-%b-%Y"}}',
                "&amp;",
                'updated: {{page.last_modified_at | date: "%d-%b-%Y"}}',
                "{:.notice - -primary}",
            ]
        )
