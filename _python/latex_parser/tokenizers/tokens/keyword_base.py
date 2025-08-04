"""
Base class for keywords of interest such as
- \\begin{itemize}
- \\end{itemize}
- \\bit
- \\eit
"""

from latex_parser.tokenizers.parsing_exception import ParsingException
from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase


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
        from latex_parser.tokenizers.tokens.begin_document_token import BeginDocumentToken
        from latex_parser.tokenizers.tokens.end_document_token import EndDocumentToken
        from latex_parser.tokenizers.tokens.begin_theorem_like_token import BeginTheoremLikeToken
        from latex_parser.tokenizers.tokens.end_theorem_like_token import EndTheoremLikeToken

        # ~ 2593
        try:
            return ItemToken.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # ~ 1074
        try:
            return BeginItemizeToken.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # ~ 1074
        try:
            return EndItemizeToken.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # ~ 584
        try:
            return MyFoilhead.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # ~ 420
        try:
            return BeginTheoremLikeToken.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # ~ 420
        try:
            return EndTheoremLikeToken.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # ~ 34
        try:
            return TitleFoil.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # ~ 7
        try:
            return TopTitleFoil.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # = 1
        try:
            return BeginDocumentToken.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        # = 1
        try:
            return EndDocumentToken.parse_and_create(source_left, line_num)
        except ParsingException:
            pass

        raise ParsingException()
