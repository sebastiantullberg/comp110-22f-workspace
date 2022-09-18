"""This is ex 3."""

__author__ = "730523735"


def all(rolls: list[int], number: int) -> bool:
    """Evaluates all int in list and checks if number mathes all."""
    if len(rolls) == 0:
        return False
    i: int = 0
    while i < len(rolls):
        if number != rolls[i]:
            return False 
        else:
            i += 1
    return True


def max(input: list[int]) -> int:
    """Returns largest integer."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1
    largest_int = input[0]
    while i < len(input):
        if input[i] > largest_int:
            largest_int = input[i]
        i += 1
    return largest_int


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if given index of list 1 = same index of list 2."""
    i: int = 0
    if len(list_1) != len(list_2):
        return False
    while i < len(list_2):
        if list_1[i] == list_2[i]:
            i += 1
        else:
            return False
    return True