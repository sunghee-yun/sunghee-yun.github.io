"""
\\includegrphics
"""

from latex_parser.latex_figures.figure_base import FigureBase


class IncludeGraphics(FigureBase):
    """Handles figures and includegraphics"""

    def __init__(self, path: str, options: str = "", caption: str = ""):
        super().__init__()
        self.path = path
        self.options = options
        self.caption = caption

    def to_markdown(self) -> str:
        # Assume .png extension
        img_path = f"{self.path}.png"

        if self.caption:
            return f"""<div class="fig-container">
<figure>
<img src="{img_path}" alt="{self.caption}">
<figcaption>{self.caption}</figcaption>
</figure>
</div>
"""
        else:
            return f"""<div class="img-container">
<img src="{img_path}" alt="{self.path}">
</div>
"""
