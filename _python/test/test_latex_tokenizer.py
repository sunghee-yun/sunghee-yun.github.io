"""
test latex tokenizer
"""

import os
import unittest
from logging import Logger, getLogger

from freq_used.logging_utils import set_logging_basic_config

from latex_parser.tokenizers.latex_tokenizer import LaTeXTokenizer
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.tokens.user_defined_command import UserDefinedCommandToken
from latex_parser.tokenizers.tokens.punctuation_token import PunctuationToken

logger: Logger = getLogger()

DATA_DIR: str = os.path.join(os.curdir, "data")


class TestLaTeXTokenizer(unittest.TestCase):
    def_tex_filepath: str = os.path.join(DATA_DIR, "mydefs.tex")
    fun_math_tex_filepath: str = os.path.join(DATA_DIR, "fun_math_Main.tex")
    processed_slide_tex_filepath: str = os.path.join(DATA_DIR, "2025-08-01-PDT - math-slides.tex")

    @classmethod
    def setUpClass(cls) -> None:
        set_logging_basic_config(__file__)

    def test_latex_tokenizer_mydefs(self) -> None:
        self._test_latex_tokenizer(self.def_tex_filepath)

    def test_latex_tokenizer_fun_math(self) -> None:
        self._test_latex_tokenizer(self.fun_math_tex_filepath)

    def test_latex_tokenizer_processed_slides(self) -> None:
        self._test_latex_tokenizer(self.processed_slide_tex_filepath)

    def _test_latex_tokenizer(self, filepath: str) -> None:
        logger.info(f"Reading {filepath} ...")
        with open(filepath, "r", encoding="utf-8") as fid:
            content: str = fid.read()

        try:
            latex_tokenizer: LaTeXTokenizer = LaTeXTokenizer(content)
            for idx, token in enumerate(latex_tokenizer.tokenize()):
                logger.info(f"token {idx} - {token.line_num} - {token}")
        except Exception:
            raise
        finally:
            LaTeXTokenBase.log_statistics()
            logger.info(sorted(UserDefinedCommandToken.USER_COMMAND_SET))
            logger.info(PunctuationToken.punctuation_set)

        self.assertTrue(True)  # add assertion here


if __name__ == "__main__":
    unittest.main()
