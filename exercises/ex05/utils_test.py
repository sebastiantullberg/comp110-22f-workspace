"""Testing the utils functions."""

__author__ = "730523735"

from urllib.parse import non_hierarchical
from utils import only_evens
from utils import sub
from utils import concat

from utils import only_evens, sub, concat

# The three following functions test only_evens
def test_only_evens_empty() -> None:
    # Edge case
    even_list: list[int] = []
    assert only_evens(even_list) == []

def test_only_evens_odds() -> None:
    # Only uneven numbers
    even_list: list[int] = [3, 7, 9]
    assert only_evens(even_list) == []

def test_only_evens_even_number() -> None:
    # Tests one even number
    even_list: list[int] = [2]
    assert only_evens(even_list) == [2]


# The three following tests are for testing concat
def test_concat_empty() -> None:
    # Edge case
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []

def test_concat_one_item() -> None:
    list_1: list[int] = [1]
    list_2: list[int] = [2]
    assert concat(list_1, list_2) == [1, 2]

def test_concat_multiple_items() -> None:
    list_1: list[int] = [1, 2]
    list_2: list[int] = [2, 3]
    assert concat(list_1, list_2) == [1, 2, 2, 3]

def test_sub_empty() -> None:
    # Edge case
    a_list: list[int] = []
    start: int = 0
    finish: int = 0
    assert sub(a_list, start, finish) == []

def test_sub_empty_list_integers() -> None:
    a_list: list[int] = []
    start: int = 1
    finish: int = 2
    assert sub(a_list, start, finish) == []


def test_sub_list_ints() -> None:
    a_list: list[int] = [1, 2, 3, 4]
    start: int = 1
    finish: int = 3
    assert sub(a_list, start, finish) == [2, 3]