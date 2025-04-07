"""
generate some markdown source
"""

import os
from pathlib import Path

if __name__ == "__main__":

    home_dir: str = str(Path.home())
    proj_dir: str = os.path.join(home_dir, "workspace/sunghee-yun.github.io")
    dir: str = "resource/conferences/gtc 2025 spring"
    dir_path: str = os.path.join(proj_dir, dir)

    for file_name in os.listdir(dir_path):
        if file_name.startswith("."):
            continue
        print()
        print('<div class="img-container">')
        print(f'<img src="{os.path.join("/", dir, file_name)}">')
        print("</div>")
