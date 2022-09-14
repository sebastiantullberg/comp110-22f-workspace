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

secret: str = "hello"
secret_len = len(secret)


def emojified(guess: str, secret: str) -> str:
    """Returns right emoji after all characters in secret are analyzed."""
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

# print(emojified("hellp", "world"))

def input_guess(num: int) -> str:
    "Prompts user for specific character number guess"
    guess: str = input(f"Enter a {num} character word ")
    while len(guess) != num:
        # loop to continue prompting the guesser until lengths equal each other
        guess = input(f"That wasn't {num} chars! Try again ")
    assert len(guess) == num
    return guess
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "secret_word" # you can switch it up and put in another word
    win: bool = True
    turn: int = 1
    while turn <= 6 and win:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(SECRET)) # asking the user for a guess
        print(emojified(guess, SECRET))
        if guess == SECRET:
            print(f"You won in {turn}/6 turns!")
    i += 1

if __name__ == "__main__":
    main()