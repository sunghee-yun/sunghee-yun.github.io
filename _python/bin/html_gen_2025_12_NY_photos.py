"""
generates html input for photos of the trips to New York in Dec, 2024
"""

import os

if __name__ == "__main__":
    directory_name: str = "resource/photos/2025-NY"
    directory_path: str = os.path.join(os.curdir, directory_name)

    for idx, file in enumerate(os.listdir(directory_path)):
        if file == ".DS_Store":
            continue
        print(idx)
        print('<div class="img-container">')
        print(f'\t<img src="/{directory_name}/{file}">')
        print("</div>")
        print("")
