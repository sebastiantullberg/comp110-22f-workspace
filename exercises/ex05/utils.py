"""Defining three different utility functions."""

__author__ = "730523735"


def only_evens(list: list[int]) -> list[int]:
    i: int = 0
    even_list: list[int] = []
    while i < len(list):
        if list[i] % 2 == 0:
            even_list.append(list[i])
        i += 1
    return even_list


# print(only_evens([1, 6, 3, 8]))


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    accum_list: list[int] = list_1 + list_2
    return accum_list

list_1: list[int] = [1, 5, 4]
list_2: list[int] = [8, 2, 3]

# print(concat(list_1, list_2))

# print(list_1)
# print(list_2)




def sub(a_list: list[int], start: int, finish: int) -> list[int]:
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


a_list: list[int] = [5, 4, 4]
start: int = 1
finish: int = 10

print(sub(a_list, start, finish))