"""
LaTeX to Jekyll Markdown Converter
Converts sophisticated LaTeX documents (like fun_math_Main - sample.tex)
to Jekyll-compatible markdown with minimal-mistakes theme support.

Author: Claude & Sunghee Yun
Version: 1.0
"""

from __future__ import annotations

from pathlib import Path
import logging

import click
from click import command, option, argument
from freq_used.logging_utils import set_logging_basic_config

from converters.foiltex_markdown_conversion_config import FoiltexToMarkdownConversionConfig
from converters.foiltex_markdown_converter import LaTeXToMarkdownConverter


@command(help="Convert Math Slide LaTeX to Jekyll Markdown")
@argument(
    "config_file", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True)
)
@argument("slide_tex", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True))
@option("-v", "--verbose", is_flag=True, help="Verbose mode")
def main(
    config_file: str,
    slide_tex: str,
    verbose: bool,
) -> None:

    assert isinstance(config_file, str)
    assert isinstance(slide_tex, str)
    assert isinstance(verbose, bool)

    set_logging_basic_config(__file__, level=logging.DEBUG if verbose else logging.INFO)

    config_path: Path = Path(config_file)
    config: FoiltexToMarkdownConversionConfig = FoiltexToMarkdownConversionConfig.from_yaml(
        config_path
    )

    converter: LaTeXToMarkdownConverter = LaTeXToMarkdownConverter(config)

    tex_file: Path = Path(slide_tex)
    try:
        converter.convert_to_markdown(tex_file)
    except Exception as e:
        print(f"Conversion failed: {e}")
        raise


if __name__ == "__main__":
    main()
