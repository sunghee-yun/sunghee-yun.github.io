"""
test latex parser
"""

import os
import unittest
from logging import Logger, getLogger

from freq_used.logging_utils import set_logging_basic_config

from latex_parser.latex_parser import LaTeXParser

logger: Logger = getLogger()

DATA_DIR: str = os.path.join(os.curdir, "data")


class TestLaTeXParser(unittest.TestCase):
    def_tex_filepath: str = os.path.join(DATA_DIR, "mydefs.tex")
    fun_math_tex_filepath: str = os.path.join(DATA_DIR, "fun_math_Main.tex")
    processed_slide_tex_filepath: str = os.path.join(DATA_DIR, "2025-08-01-PDT - math-slides.tex")

    @classmethod
    def setUpClass(cls) -> None:
        set_logging_basic_config(__file__)

    # def test_latex_parser_mydefs(self) -> None:
    #     self._test_latex_parser(self.def_tex_filepath)
    #
    # def test_latex_parser_fun_math(self) -> None:
    #     self._test_latex_parser(self.fun_math_tex_filepath)

    def test_latex_parser_processed_slides(self) -> None:
        self._test_latex_parser(self.processed_slide_tex_filepath)

    def _test_latex_parser(self, filepath: str) -> None:
        logger.info(f"Reading {filepath} ...")
        with open(filepath, "r", encoding="utf-8") as fid:
            content: str = fid.read()

        parser: LaTeXParser = LaTeXParser(content)
        parser.parse()

        self.assertTrue(True)  # add assertion here


if __name__ == "__main__":
    unittest.main()
