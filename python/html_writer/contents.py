"""
class representing html content
"""


class Contents:
    def __init__(self, content: str) -> None:
        self.content: str = content

    def __repr__(self) -> str:
        return self.content
