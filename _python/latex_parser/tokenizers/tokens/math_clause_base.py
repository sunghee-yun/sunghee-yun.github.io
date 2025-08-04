"""
Base class for all math related clause, env, etc.
"""

from abc import abstractmethod

from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.parsing_exception import ParsingException


class MathClauseBase(LaTeXTokenBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int, content: str) -> None:
        super().__init__(string, line_num)
        self.content: str = content
        MathClauseBase.num_instances += 1

    @property
    @abstractmethod
    def opening_markdown_symbol(self) -> str:
        pass

    @property
    @abstractmethod
    def closing_markdown_symbol(self) -> str:
        pass

    @property
    def markdown_content(self) -> str:
        return self.content

    @property
    def markdown_str(self) -> str:
        return (
            self.new_line
            + self.opening_markdown_symbol
            + self.new_line
            + self.markdown_content
            + self.new_line
            + self.closing_markdown_symbol
            + self.new_line
        )

    @property
    def new_line(self) -> str:
        return "\n"

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        from latex_parser.tokenizers.tokens.math_clause import MathClause
        from latex_parser.tokenizers.tokens.multiline_math_clause import MultilineMathClause
        from latex_parser.tokenizers.tokens.equation_math_clause import EquationMathClause
        from latex_parser.tokenizers.tokens.eqnarray_math_clause import EqnArrayMathClause

        # ~ 5030
        try:
            return MathClause.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # ~ 855
        try:
            return MultilineMathClause.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # ~ 60
        try:
            return EqnArrayMathClause.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # ~ 0
        try:
            return EquationMathClause.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        raise ParsingException()
