"""Defining three different utility functions."""

__author__ = "730523735"


def only_evens(list: list[int]) -> list[int]:
    """Returns only even ints from list."""
    i: int = 0
    even_list: list[int] = []
    while i < len(list):
        if list[i] % 2 == 0:
            even_list.append(list[i])
        i += 1
    return even_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Adds list 2 to list 1."""
    accum_list: list[int] = list_1 + list_2
    return accum_list


def sub(a_list: list[int], start: int, finish: int) -> list[int]:
    """Returns a list between the specified start index."""
    """And the end index - 1."""
    result: list[int] = []
    if len(a_list) == 0 or start > len(a_list) or finish <= 0:
        return result
    i: int = 0
    if start < 0:
        start: int = 0
    if finish > len(a_list):
        finish: int = len(a_list)
    while i < len(a_list):
        if i >= start and i < finish:
            result.append(a_list[i])
        i += 1
    return result