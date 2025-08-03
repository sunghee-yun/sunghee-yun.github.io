"""
itemize env
"""

from latex_parser.latex_envs.itemize_env_base import ItemizeEnvBase


class ItemizeEnv(ItemizeEnvBase):
    """\\begin{itemize} ... \\end{itemize}"""

    @property
    def html_tag(self) -> str:
        return "ul"
