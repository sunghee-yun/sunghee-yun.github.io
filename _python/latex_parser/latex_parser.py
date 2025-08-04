"""
LaTeX parser
"""

from enum import Enum, auto
from logging import Logger, getLogger

from latex_parser.latex_elements.itemize_element import ItemizeElement
from latex_parser.latex_elements.latex_contents import LaTeXContents
from latex_parser.latex_elements.latex_document import LaTeXDocument
from latex_parser.latex_elements.theorem_like_element import (
    TheoremLikeElement,
    TheoremLikeType,
)
from latex_parser.latex_elements.token_element import TokenElement
from latex_parser.latex_elements.latex_command_element import LaTeXCommandElement
from latex_parser.latex_elements.foiltex_section_element import FoiltexSectionElement
from latex_parser.latex_elements.item_element import ItemElement
from latex_parser.latex_elements.latex_element_base import LaTeXElementBase
from latex_parser.parsing_error import ParsingError
from latex_parser.tokenizers.latex_tokenizer import LaTeXTokenizer
from latex_parser.tokenizers.tokens.begin_document_token import BeginDocumentToken
from latex_parser.tokenizers.tokens.begin_itemize_token import BeginItemizeToken
from latex_parser.tokenizers.tokens.begin_theorem_like_token import (
    BeginTheoremLikeToken,
)
from latex_parser.tokenizers.tokens.braced_clause import BracedClause
from latex_parser.tokenizers.tokens.bracketed_clause import BracketedClause
from latex_parser.tokenizers.tokens.command_token_base import CommandTokenBase
from latex_parser.tokenizers.tokens.end_document_token import EndDocumentToken
from latex_parser.tokenizers.tokens.end_itemize_token import EndItemizeToken
from latex_parser.tokenizers.tokens.end_theorem_like_token import EndTheoremLikeToken
from latex_parser.tokenizers.tokens.item_token import ItemToken
from latex_parser.tokenizers.tokens.latex_command import LaTeXCommandToken
from latex_parser.tokenizers.tokens.new_lines_token import NewLines
from latex_parser.tokenizers.tokens.white_spaces import WhiteSpaces
from latex_parser.tokenizers.tokens.top_title_foil import TopTitleFoil
from latex_parser.tokenizers.tokens.title_foil import TitleFoil
from latex_parser.tokenizers.tokens.my_foilhead import MyFoilhead

logger: Logger = getLogger()


class ItemizeMode(Enum):
    NOT_ITEMIZE = auto()
    JUST_STARTED = auto()
    ITEMS_STARTED = auto()


class LaTeXParser:
    def __init__(self, latex_source: str) -> None:
        self.latex_source: str = latex_source

    def parse(self) -> LaTeXDocument:

        latex_tokenizer: LaTeXTokenizer = LaTeXTokenizer(self.latex_source)

        preamble: LaTeXContents = LaTeXContents()
        main_body: LaTeXContents = LaTeXContents()

        content_stack: list[LaTeXContents] = [preamble]
        itemize_stack: list[ItemizeElement] = list()

        document_main_body_started: bool = False
        met_end_document: bool = False

        itemize_mode: ItemizeMode = ItemizeMode.NOT_ITEMIZE
        begin_theorem_like_token: BeginTheoremLikeToken | None = None

        latex_command: CommandTokenBase | None = None
        latex_command_arg_list: list[BracedClause] = list()
        latex_command_opt_arg_list: list[BracketedClause] = list()
        latex_command_spaces: list[NewLines | WhiteSpaces] = list()
        latex_command_waiting_for_opt_args: bool = False
        for idx, token in enumerate(latex_tokenizer.tokenize()):
            logger.debug(f"token {idx} - {token.line_num} - {token}")

            if latex_command is not None:
                if isinstance(token, (NewLines, WhiteSpaces)):
                    latex_command_spaces.append(token)
                    continue

                if latex_command_waiting_for_opt_args and isinstance(token, BracketedClause):
                    latex_command_spaces = list()
                    latex_command_opt_arg_list.append(token)
                    continue

                if isinstance(token, BracedClause):
                    latex_command_waiting_for_opt_args = False
                    latex_command_spaces = list()
                    latex_command_arg_list.append(token)
                    continue

                content_stack[-1].add_element(
                    LaTeXCommandElement(
                        latex_command,
                        [braced_clause.string[1:-1] for braced_clause in latex_command_arg_list],
                        [
                            bracketed_arg.string[1:-1]
                            for bracketed_arg in latex_command_opt_arg_list
                        ],
                    )
                )

                for white_space_or_new_line in latex_command_spaces:
                    content_stack[-1].add_element(TokenElement(white_space_or_new_line))
                latex_command_spaces = list()

                latex_command = None
                latex_command_arg_list = list()
                latex_command_opt_arg_list = list()

            if begin_theorem_like_token is not None and isinstance(token, EndTheoremLikeToken):
                assert begin_theorem_like_token.env_name == token.env_name, (
                    begin_theorem_like_token,
                    token,
                )

                env_name: str = begin_theorem_like_token.env_name

                assert env_name.startswith("my") and len(env_name) > 2, env_name

                assert len(content_stack) >= 2, len(content_stack)

                theorem_like_element: TheoremLikeElement = TheoremLikeElement(
                    TheoremLikeType(env_name[2:]),
                    begin_theorem_like_token.name,
                    content_stack.pop(),
                )

                content_stack[-1].add_element(theorem_like_element)

                begin_theorem_like_token = None
                continue

            if itemize_mode == ItemizeMode.JUST_STARTED:
                if isinstance(token, ItemToken):
                    itemize_mode = ItemizeMode.ITEMS_STARTED
                    content_stack.append(LaTeXContents())
                    continue

                if (
                    isinstance(token, (NewLines, WhiteSpaces))
                    or isinstance(token, LaTeXCommandToken)
                    and token.string == r"\vfill"
                ):
                    continue

                raise ParsingError(r"\item expected after \begin{itemize} - " + str(token))

            if not document_main_body_started and isinstance(token, BeginDocumentToken):
                assert len(content_stack) == 1, len(content_stack)
                content_stack[0] = main_body
                document_main_body_started = True
                continue

            if itemize_mode == ItemizeMode.ITEMS_STARTED and isinstance(
                token, (ItemToken, EndItemizeToken)
            ):
                assert len(content_stack) >= 2, len(content_stack)
                assert len(itemize_stack) >= 1, (len(itemize_stack), token)
                assert len(content_stack) > len(itemize_stack), (
                    len(content_stack),
                    len(itemize_stack),
                )

                if isinstance(token, ItemToken):
                    itemize_stack[-1].add_item(ItemElement(content_stack.pop()))
                    content_stack.append(LaTeXContents())
                else:
                    itemize_stack[-1].add_item(ItemElement(content_stack.pop()))
                    content_stack[-1].add_element(itemize_stack.pop())
                continue

            if isinstance(token, BeginItemizeToken):
                itemize_stack.append(ItemizeElement())
                itemize_mode = ItemizeMode.JUST_STARTED
                continue

            if isinstance(token, EndDocumentToken):
                met_end_document = True
                break

            if isinstance(token, CommandTokenBase):
                assert latex_command is None
                assert len(latex_command_arg_list) == 0, (
                    latex_command_arg_list,
                    len(latex_command_arg_list),
                )
                assert len(latex_command_opt_arg_list) == 0, (
                    latex_command_opt_arg_list,
                    len(latex_command_opt_arg_list),
                )

                latex_command = token
                latex_command_waiting_for_opt_args = True
                assert len(latex_command_spaces) == 0, len(latex_command_spaces)
                continue

            if isinstance(token, BeginTheoremLikeToken):
                assert begin_theorem_like_token is None
                begin_theorem_like_token = token
                content_stack.append(LaTeXContents())
                continue

            element: LaTeXElementBase = TokenElement(token)
            if isinstance(token, (MyFoilhead, TitleFoil, TopTitleFoil)):
                element = FoiltexSectionElement(token)

            content_stack[-1].add_element(element)

        if not met_end_document:
            logger.warning(r"The document misses `\end{document}` statement!")

        return LaTeXDocument(preamble, main_body)
