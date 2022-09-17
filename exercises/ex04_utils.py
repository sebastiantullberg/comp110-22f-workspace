"""This is ex 3. """

__author__ = "730523735"

from random import randint


def evaluate_list(rolls: list[int] = list(1, 2, 3), number: 2) -> bool:
    """Evaluates all int in list and checks if number mathes all"""
    i: int = 0
    # 4,4,4 4
    while i < len(list):
        if number != list[i]:
            return False 
        else:
            i += 1
    return True


def max(input: list[int]) -> int:
    """Returns largest integer"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    largest_integer = list[i]
    while i < len(list):
        if list[i + 1] > largest_int:
            largest_int = list[i]
        i += 1
    return largest_int

def is_equal(list_1: int, list_2: int) -> bool:
    """Checks if given index of list 1 = same index of list 2"""
    i: int = 0
    if len(list_1) != len(list_2):
        return False
    while i < len(list_2):
        if list_1[i] == list_2[i]:
            i += 1
        else:
            return False
    return True


