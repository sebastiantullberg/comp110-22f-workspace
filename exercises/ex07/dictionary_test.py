"""This is a test file for ex 7."""

__author__ = "730523735"

from dictionary import invert, favorite_color, count


# The three following functions test invert
def test_invert1() -> None:
    """Edge case."""
    old_key: dict[str, str] = {}
    assert invert(old_key) == {}


def test_invert2() -> None:
    """Cap Words."""
    old_key: dict[str, str] = {"Hey": "Mor", "Vil": "Du"}
    assert invert(old_key) == {"Mor": "Hey", "Du": "Vil"}


def test_invert3() -> None:
    """Lowercase words."""
    old_key: dict[str, str] = {"hey": "mon", "vil": "mor"}
    assert invert(old_key) == {"mon": "hey", "mor": "vil"}


# The three following tests are for testing favorite_color
def test_favorite_color1() -> None:
    """Edge case."""
    identity: dict[str, str] = {}
    assert favorite_color(identity) == ""


def test_favorite_color2() -> None:
    """Normal use."""
    identity: dict[str, str] = {"Seb": "Yellow", "Marc": "Black", "Wilson": "Yellow"}
    assert favorite_color(identity) == "Yellow"


def test_favorite_color3() -> None:
    """Tie."""
    identity: dict[str, str] = {"Seb": "Yellow", "Marc": "Black"}
    assert favorite_color(identity) == "Yellow"


# testing count
def test_count1() -> None:
    """Edge case."""
    a: list[str] = []
    assert count(a) == {}


def test_count2() -> None:
    """Count."""
    a: list[str] = ["hey", "hvad", "hedder"]
    assert count(a) == {"hey": 1, "hvad": 1, "hedder": 1}


def test_count3() -> None:
    """Multiple."""
    a: list[str] = ["hey", "hey", "hedder"]
    assert count(a) == {"hey": 2, "hedder": 1}