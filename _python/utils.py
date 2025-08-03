"""
utils
"""


def get_all_subclasses(cls) -> list[type]:
    """Get all subclasses recursively"""
    subclasses = set(cls.__subclasses__())
    for subclass in list(subclasses):
        subclasses.update(get_all_subclasses(subclass))
    return list(subclasses)
