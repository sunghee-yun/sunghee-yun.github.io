"""
Base class for keywords of interest such as
- \\begin{itemize}
- \\end{itemize}
- \\bit
- \\eit
"""

import re
from re import Match

from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.braced_phrase import BracedPhrase


class KeywordBase(LaTeXTokenBase):
    num_instances: int = 0
    THEOREM_LIKE_NAMES: list[str] = [
        "myaxiom",
        "mylaw",
        "myprinciple",
        "mydefinition",
        "mytheorem",
        "mylemma",
        "myproposition",
        "mycorollary",
        "myconjecture",
        "myinequality",
        "myformula",
        "myalgorithm",
    ]

    REG_EXP_THEOREM_LIKE_NAMES = "|".join(THEOREM_LIKE_NAMES)

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        KeywordBase.num_instances += 1

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        from latex_parser.tokenizers.tokens.begin_itemize_token import BeginItemizeToken
        from latex_parser.tokenizers.tokens.end_itemize_token import EndItemizeToken
        from latex_parser.tokenizers.tokens.item_token import ItemToken
        from latex_parser.tokenizers.tokens.top_title_foil import TopTitleFoil
        from latex_parser.tokenizers.tokens.title_foil import TitleFoil
        from latex_parser.tokenizers.tokens.my_foilhead import MyFoilhead
        from latex_parser.tokenizers.tokens.begin_document_token import (
            BeginDocumentToken,
        )
        from latex_parser.tokenizers.tokens.end_document_token import EndDocumentToken
        from latex_parser.tokenizers.tokens.begin_theorem_like_token import (
            BeginTheoremLikeToken,
        )
        from latex_parser.tokenizers.tokens.end_theorem_like_token import (
            EndTheoremLikeToken,
        )

        match: Match | None = re.match(r"(\\(v+i?|i|b)?item\s*(\[.*])?)", source_left)
        if match:
            return ItemToken(match.group(1), line_num), match.span()[1]

        match = re.match(r"(\\begin\s*{\s*itemize\s*})", source_left)
        if match:
            return BeginItemizeToken(match.group(1), line_num), match.span()[1]

        match = re.match(r"(\\i?bit)[^\w]", source_left)
        if match:
            return BeginItemizeToken(match.group(1), line_num), len(match.group(1))

        match = re.match(r"(\\end\s*{\s*itemize\s*})", source_left)
        if match:
            return EndItemizeToken(match.group(1), line_num), match.span()[1]

        match = re.match(r"(\\eit)", source_left)
        if match:
            return EndItemizeToken(match.group(1), line_num), match.span()[1]

        match = re.match(r"(\\TITLEFOIL\s*{\s*([\s\S]*?)\s*}\s*{\s*([\s\S]*?)\s*})", source_left)
        if match:
            return (
                TopTitleFoil(match.group(1), line_num, match.group(2), match.group(3)),
                match.span()[1],
            )

        match = re.match(r"(\\titlefoil\s*{\s*([\s\S]*?)\s*}\s*{\s*([\s\S]*?)\s*})", source_left)
        if match:
            return (
                TitleFoil(match.group(1), line_num, match.group(2), match.group(3)),
                match.span()[1],
            )

        match = re.match(r"(\\(myfoilhead|labelfoilhead)\s*)", source_left)
        if match:
            token, length = BracedPhrase.parse_and_create(
                source_left[match.span()[1] :], line_num  # noqa: E203
            )
            assert isinstance(token, BracedPhrase), token.__class__
            return MyFoilhead(
                match.group(1) + token.string, line_num, token.string[1:-1]
            ), match.span()[1] + len(token.string)

        match = re.match(r"(\\begin\s*{\s*document\s*})", source_left)
        if match:
            return BeginDocumentToken(match.group(1), line_num), match.span()[1]

        match = re.match(r"(\\end\s*{\s*document\s*})", source_left)
        if match:
            return EndDocumentToken(match.group(1), line_num), match.span()[1]

        match = re.match(
            r"(\\begin\s*{\s*(" + cls.REG_EXP_THEOREM_LIKE_NAMES + r")\s*}{\s*([\s\S]*?)\s*})",
            source_left,
        )
        if match:
            return (
                BeginTheoremLikeToken(match.group(1), line_num, match.group(2), match.group(3)),
                match.span()[1],
            )

        match = re.match(
            r"(\\end\s*{\s*(" + cls.REG_EXP_THEOREM_LIKE_NAMES + r")\s*})", source_left
        )
        if match:
            return (
                EndTheoremLikeToken(match.group(1), line_num, match.group(2)),
                match.span()[1],
            )

        raise ParsingException()
