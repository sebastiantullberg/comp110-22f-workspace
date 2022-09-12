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

def emojified(guess: str, secret: str) -> str:
    """Returns righjt emoji after all characters in secret are analyzed"""
    i: int = 0
    emoji: str = ""
    assert len(guess) == len(secret)
    while i < len(secret):
        if contains_char(secret, guess[i]) == True:
            if guess[i] == secret[i]:
                emoji += green_box
            else:
                emoji += yellow_box
        else:
            emoji += white_box
        i += 1
    return emoji

print(emojified("hello", "world"))