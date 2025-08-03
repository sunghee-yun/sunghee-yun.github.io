"""
LaTeX math phrase
"""

import re
from re import Match

from latex_parser.tokenizers.tokens.latex_token_base import LaTeXTokenBase
from latex_parser.tokenizers.parsing_exception import ParsingException


class AlgorithmicClause(LaTeXTokenBase):
    num_instances: int = 0

    SINGLE_KEYWORDS: dict[str, str] = dict(
        EndLoop="end loop", Loop="loop", Repeat="repeat", EndWhile="end while"
    )

    CLAUSE_KEYWORDS: dict[str, tuple[str, str]] = dict(
        Require=("Require:", ""),
        State=("", ""),
        Until=("until", ""),
        While=("while", "do"),
    )

    ALL_KEYWORDS: list[str] = list(SINGLE_KEYWORDS) + list(CLAUSE_KEYWORDS)

    def __init__(self, string: str, line_num: int, content: str) -> None:
        super().__init__(string, line_num)
        self.content: str = content
        AlgorithmicClause.num_instances += 1

    @property
    def markdown_str(self) -> str:
        def replace_clause_middle(keyword: str, command: str, postfix: str, string: str) -> str:
            return re.sub(
                r"\\"
                + keyword
                + r"\s*{\s*([\s\S]*?)}(\s*("
                + "|".join([rf"\\{keyword}" for keyword in self.ALL_KEYWORDS])
                + "|<li>))",
                rf"<li>\n\t<strong>{command}</strong>\t\1 {postfix}\n</li>\n\2",
                string,
            )

        def replace_clause_end(keyword: str, command: str, postfix: str, string: str) -> str:
            return re.sub(
                r"\\" + keyword + r"\s*{\s*([\s\S]*?)}\s*$",
                rf"<li>\n\t<strong>{command}</strong>\t\1 {postfix}\n</li>\n",
                string,
            )

        def replace_token(keyword: str, replacement: str, string: str):
            return re.sub(
                r"\\" + keyword,
                f"<li>\n\t<strong>{replacement}</strong>\n</li>",
                string,
            )

        markdown_list: str = self.content
        for keyword, (command, postfix) in self.CLAUSE_KEYWORDS.items():
            for _ in range(100):
                markdown_list = replace_clause_middle(keyword, command, postfix, markdown_list)
            markdown_list = replace_clause_end(keyword, command, postfix, markdown_list)

        for keyword, replacement in self.SINGLE_KEYWORDS.items():
            markdown_list = replace_token(keyword, replacement, markdown_list)

        return f"<ul>\n{markdown_list}\n</ul>"

    @classmethod
    def parse_and_create(cls, source_left: str, line_num: int) -> tuple[LaTeXTokenBase, int]:
        match: Match | None = re.match(
            r"(\\begin\s*{\s*algorithmic\s*}((.|\n)*?)\\end\s*{\s*algorithmic\s*})",
            source_left,
        )
        if match is None:
            raise ParsingException()

        return (
            AlgorithmicClause(match.group(1), line_num, match.group(2).strip()),
            match.span()[1],
        )
