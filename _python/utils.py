"""
utils
"""


def get_all_subclasses(cls) -> list[type]:
    """Get all subclasses recursively"""
    subclasses = set(cls.__subclasses__())
    for subclass in list(subclasses):
        subclasses.update(get_all_subclasses(subclass))
    return list(subclasses)


def parse_nested_braced_clause(string: str) -> str:
    return _parse_nested_parenthesized_clause(string, "{", "}")


def _parse_nested_parenthesized_clause(string: str, left: str, right: str) -> str:
    assert len(left) == 1, left
    assert len(right) == 1, right

    if len(string) < 2:
        raise Exception(f"String too short: {string}")

    if not string.startswith(left):
        raise Exception(f"String does not start with `{left}`: {string}")

    number_braces_opened: int = 1
    escape_character_just_before: bool = False
    for idx, character in enumerate(string[1:]):
        if character == "\\":
            escape_character_just_before = True
            continue

        if (
            not escape_character_just_before or (idx >= 2 and string[idx - 1] == "\\")
        ) and character == right:
            number_braces_opened -= 1

        if number_braces_opened == 0:
            break

        if (
            not escape_character_just_before or (idx >= 2 and string[idx - 1] == "\\")
        ) and character == left:
            number_braces_opened += 1

        escape_character_just_before = False

    if number_braces_opened > 0:
        raise Exception("Open braces are not completed closed!")

    return string[: idx + 2]
