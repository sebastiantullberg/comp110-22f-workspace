"""This is Wordle."""

__author__ = "730523735"

# 
def contains_char(word: str, letter: str) -> bool:
    """Returns True or False."""
    i: int = 0
    assert len(letter) == 1
    while i < len(word):
        if letter == word[i]:
            return True
        i += 1
    return False

# set up color constants
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

emoji: str = ""

def emojified(guess: str, secret: str) -> str:
    """Returns """
    i: int = 0
    assert len(REPLACE_THIS_WITH_YOUR_GUESS_PARAMETERS_NAME) == len(REPLACE_THIS_WITH_YOUR_SECRET_PARAMETERS_NAME)
    while i < len(word):
        if contains_char(guess, secret[i]) == True:
            emoji += yellow_box
        else:
            emoji += white_box
