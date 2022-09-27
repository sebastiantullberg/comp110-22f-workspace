"""Testing the utils functions."""

__author__ = "730523735"

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