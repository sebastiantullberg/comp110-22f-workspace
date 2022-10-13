"""This is ex 7."""

__author__ = "730523735"


def invert(old_key: dict[str, str]) -> dict[str, str]:
    """Changes keys from mother function to values and vice versa."""
    result = {}
    for key in old_key:
        if old_key[key] in result:
            raise KeyError("You can't have multiple identical keys.")
        result[old_key[key]] = key
    return result


def favorite_color(identity: dict[str, str]) -> str:
    """Returns a string with the color that appears the most."""
    highest_color: str = ""
    counts: int = 0
    for key in identity:
        current: str = identity[key]
        current_count: int = 0
        for key1 in identity:
            if identity[key1] == current:
                current_count += 1
        if current_count > counts:
            counts = current_count
            highest_color = current
    return highest_color


def count(a: list[str]) -> dict[str, int]:
    """Returns a dict with the words and how many times it occurs in the initial list."""
    new_dict: dict[str, int] = dict()
    i: int = 0
    while i < len(a):
        # iterates through all word (index) and adds 1 to value
        if a[i] in new_dict:
            new_dict[a[i]] += 1
        else:
            new_dict[a[i]] = 1
        i += 1
    return new_dict
