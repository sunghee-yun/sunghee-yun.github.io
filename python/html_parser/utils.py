"""
html parsing-related utils
"""

from bs4 import Tag


def print_structure(element: Tag, indent: int = 0):
    """
    Recursively print the structure with indentation
    """

    # Create indentation for structure levels
    indent_str = " " * indent

    # Print the current tag
    if element.name:
        print(f"{indent_str}<{element.name}>")

    # Print attributes if they exist (like href in <a>)
    if element.attrs:
        for attr, value in element.attrs.items():
            print(f"{indent_str}  {attr}: {value}")

    # Loop over the children elements
    for child in element.children:
        if child.name:  # If the child is a tag, recursively print its structure
            print_structure(child, indent + 2)
        elif child.strip():  # If it's a string and not just whitespace, print it
            print(f"{indent_str}  {child.strip()}")

    # Close the tag (not necessary but adds clarity)
    if element.name:
        print(f"{indent_str}</{element.name}>")
