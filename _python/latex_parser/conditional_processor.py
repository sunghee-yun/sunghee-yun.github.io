"""
LaTeX conditional processor
"""

from __future__ import annotations

import re
from logging import Logger, getLogger

logger: Logger = getLogger()


class LaTeXConditionalProcessor:
    """Robust processor for LaTeX conditionals - works like real LaTeX compiler"""

    # SUBS_STRS: dict[str, str] = {r"\\bit": r"\\begin{itemize}", r"\\eit": r"\\end{itemize}"}
    SUBS_STRS: dict[str, str] = dict()

    def __init__(self, flags: dict[str, bool]):
        self.flags: dict[str, bool] = flags.copy()
        self.processed_flags: set[str] = set()

    def process_document(self, tex_content: str) -> str:
        """Process all conditionals and return clean LaTeX"""

        logger.info("Processing LaTeX conditionals...")

        # Process in the right order
        content = tex_content
        content = self.extract_def_flags(content)
        content = self.extract_newcommand_flags(content)
        content = self.process_ifdefined_blocks(content)
        content = self.process_yesnoexec_nested(content)
        content = self.clean_latex_content(content)

        logger.info(f"Conditional processing complete. Flags used: {self.processed_flags}")

        content = self._sub_strs(content)

        return content

    def extract_def_flags(self, content: str) -> str:
        """Extract \\def statements and update flags"""
        return self._extract_def_flags(content, r"\\def\\([^{\\}\s]+)\{([^}]*)\}")

    def extract_newcommand_flags(self, content: str) -> str:
        """Extract \\newcommand statements and update flags"""
        return self._extract_def_flags(
            content, r"\s*\\newcommand\s*\{\s*\\([^{\\}\s]+\s*)\}\s*\{([^}]*)\}"
        )

    def _extract_def_flags(self, content: str, def_pattern: str) -> str:

        def process_def(match):
            flag_name = match.group(1)
            flag_value = match.group(2).strip()

            # Convert LaTeX boolean values
            if flag_value.lower() in ["yes", "true", "1"]:
                if flag_name in self.flags:
                    logger.warning(
                        f"flag `{flag_name}` being TRIED to be set to True"
                        f", but it's pre-determined as {self.flags[flag_name]}"
                    )
                else:
                    self.flags[flag_name] = True
                    logger.info(f"Set flag `{flag_name}` = True")

                # return ""  # Remove the \def statement

            if flag_value.lower() in ["no", "false", "0", ""]:
                if flag_name in self.flags:
                    logger.warning(
                        f"flag `{flag_name}` being TRIED to be set to False"
                        f", but it's pre-determined as {self.flags[flag_name]}"
                    )
                else:
                    self.flags[flag_name] = False
                    logger.info(f"Set flag `{flag_name}` = False")

                # return ""  # Remove the \def statement

            return match.group(0)

        content = re.sub(def_pattern, process_def, content)
        return content

    def process_yesnoexec_nested(self, content: str) -> str:
        """Process \\yesnoexec with proper nesting support"""

        def find_balanced_braces(text: str, start_pos: int) -> tuple[int, int]:
            """Find start and end of balanced braces"""
            if start_pos >= len(text) or text[start_pos] != "{":
                return -1, -1

            brace_count = 0
            start = start_pos
            i = start_pos

            while i < len(text):
                char = text[i]

                if char == "\\" and i + 1 < len(text):
                    i += 2  # Skip escaped character
                    continue
                elif char == "{":
                    brace_count += 1
                elif char == "}":
                    brace_count -= 1
                    if brace_count == 0:
                        return start + 1, i  # Return content positions (excluding braces)

                i += 1

            return -1, -1

        # Keep processing until no more \yesnoexec found
        max_iterations = 100  # Prevent infinite loops
        iteration = 0

        while "\\yesnoexec" in content and iteration < max_iterations:
            iteration += 1
            new_content = ""
            pos = 0

            while pos < len(content):
                yesno_match = re.search(r"\\yesnoexec\s*", content[pos:])

                if not yesno_match:
                    new_content += content[pos:]
                    break

                # Add content before \yesnoexec
                match_start = pos + yesno_match.start()
                new_content += content[pos:match_start]

                # Find the three arguments
                arg_pos = pos + yesno_match.end()

                # Get flag argument
                flag_start, flag_end = find_balanced_braces(content, arg_pos)
                if flag_start == -1:
                    new_content += content[match_start : arg_pos + 1]  # noqa: E203
                    pos = arg_pos + 1
                    continue

                flag = content[flag_start + 1 : flag_end].strip()  # noqa: E203

                # Get yes argument
                yes_pos = flag_end + 1
                while yes_pos < len(content) and content[yes_pos].isspace():
                    yes_pos += 1

                yes_start, yes_end = find_balanced_braces(content, yes_pos)
                if yes_start == -1:
                    pos = yes_pos
                    continue

                yes_content = content[yes_start:yes_end]

                # Get no argument
                no_pos = yes_end + 1
                while no_pos < len(content) and content[no_pos].isspace():
                    no_pos += 1

                no_start, no_end = find_balanced_braces(content, no_pos)
                if no_start == -1:
                    pos = no_pos
                    continue

                no_content = content[no_start:no_end]

                # Choose content based on flag
                self.processed_flags.add(flag)
                if self.flags.get(flag, False):
                    new_content += yes_content
                    logger.debug(f"\\yesnoexec: {flag} = True, using YES content")
                else:
                    new_content += no_content
                    logger.debug(f"\\yesnoexec: {flag} = False, using NO content")

                pos = no_end + 1

            content = new_content

        if iteration >= max_iterations:
            logger.warning("Maximum iterations reached in yesnoexec processing")

        return content

    def process_ifdefined_blocks(self, content: str) -> str:
        """Process \\ifdefined...\\fi blocks"""

        # Pattern to match \ifdefined\flag content \else content \fi
        # This handles the most common case in your LaTeX
        def process_ifdefined_block(match):
            flag = match.group(1)
            if_content = match.group(2) if match.group(2) else ""
            else_content = match.group(3) if match.group(3) else ""

            self.processed_flags.add(flag)

            if self.flags.get(flag, False):
                logger.debug(f"\\ifdefined {flag}: True, using IF content")
                return if_content
            else:
                logger.debug(f"\\ifdefined {flag}: False, using ELSE content")
                return else_content

        # Handle \ifdefined\flag ... \else ... \fi
        pattern = r"\\ifdefined\\([^\s\\]+)(.*?)(?:\\else(.*?))?\\fi"
        content = re.sub(pattern, process_ifdefined_block, content, flags=re.DOTALL)

        return content

    def clean_latex_content(self, content: str) -> str:
        """Clean up the processed LaTeX content"""

        # Remove LaTeX comments
        lines = []
        for line in content.split("\n"):
            # Find comment position (not escaped %)
            comment_pos = -1
            i = 0
            while i < len(line):
                if line[i] == "%" and (i == 0 or line[i - 1] != "\\"):
                    comment_pos = i
                    break
                elif line[i] == "\\" and i + 1 < len(line):
                    i += 1  # Skip next character
                i += 1

            if comment_pos != -1:
                line = line[:comment_pos]

            lines.append(line.rstrip())

        content = "\n".join(lines)

        # Clean up excessive whitespace
        content = re.sub(r"\n\s*\n\s*\n+", "\n\n", content)
        content = re.sub(r"^\s+", "", content, flags=re.MULTILINE)

        return content.strip()

    @classmethod
    def _sub_strs(cls, content: str) -> str:
        for search_str, sub_str in cls.SUBS_STRS.items():
            content = re.sub(search_str, sub_str, content)

        return content
