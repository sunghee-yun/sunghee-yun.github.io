"""
The part that is enclosed by braces
"""

import re
from re import Match

from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.parsing_exception import ParsingException
from utils import parse_nested_braced_clause


class BracedPhrase(LaTeXTokenBase):
    num_instances: int = 0

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        BracedPhrase.num_instances += 1

    @property
    def markdown_str(self) -> str:
        match: Match | None = re.match(r"{\s*\\tt\s+(.*)}", self.string)
        if match:
            return f"<code>{match.group(1).strip()}</code>"

        assert (
            len(self.string) >= 2 and self.string.startswith("{") and self.string.endswith("}")
        ), self.string

        return self.string[1:-1]

    @property
    def abbr_string(self) -> str:
        if self.string.count("\n") < 12:
            return self.string

        lines: list[str] = self.string.split("\n")
        return "\n".join(lines[:4] + ["."] * 3 + lines[-4:])

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        try:
            parsed_string: str = parse_nested_braced_clause(source_left)
        except Exception as e:
            raise ParsingException(str(e))

        return BracedPhrase(parsed_string, line_num), len(parsed_string)
