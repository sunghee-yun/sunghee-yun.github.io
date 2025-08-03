"""
The part that is enclosed by braces
"""

import re
from re import Match

from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.parsing_exception import ParsingException


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

        return self.string

    @property
    def abbr_string(self) -> str:
        if self.string.count("\n") < 12:
            return self.string

        lines: list[str] = self.string.split("\n")
        return "\n".join(lines[:4] + ["."] * 3 + lines[-4:])

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        if source_left.startswith("{"):
            number_braces_opened: int = 1
            escape_character_just_before: bool = False
            for idx, character in enumerate(source_left[1:]):
                if character == "\\":
                    escape_character_just_before = True
                    continue

                if (
                    not escape_character_just_before or (idx >= 2 and source_left[idx - 1] == "\\")
                ) and character == "}":
                    number_braces_opened -= 1

                if number_braces_opened == 0:
                    break

                if (
                    not escape_character_just_before or (idx >= 2 and source_left[idx - 1] == "\\")
                ) and character == "{":
                    number_braces_opened += 1

                escape_character_just_before = False

            if number_braces_opened > 0:
                raise ParsingException("Open braces are not completed closed!")

            return BracedPhrase(source_left[: idx + 2], line_num), idx + 2

        raise ParsingException()
