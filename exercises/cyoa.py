"""Rock, paper, scissors!"""

__author__ = "730523735"

from random import randint

points: int = 200

player: str = ""

garbage: str = "\U0001F5D1"
gold: str = "\U0001F3C6"


def main() -> None:
    """Main function."""
    global points
    greet()
    print(f"You have got {points} hp")
    while True:
        game_mode: int = int(input("Choose a number from 1-3. Option 1: normal. Option 2, gamble. Option 3, quit "))
        if game_mode == 1:
            normal()
        elif game_mode == 2:
            points = gamble(points)
        else:
            stop_playing()
        print(points)
        if points <= 0:
            print(f"Game over {garbage}")
            stop_playing()
        if points >= 400:
            print(f"You won! {gold}")
            stop_playing()


def greet() -> None:
    """Greets the player."""
    global player
    player = input("Hello, what is your name? ")
    print(f"Hello {player}! We are excited for you to play RPS with us!")


def normal() -> None:
    """Normal function which is the regular rock, paper, scissors game."""
    global points
    robot_choice: int = randint(1, 3)
    robot_weapon: str = ""
    if robot_choice == 1:
        robot_weapon = "rock"
    if robot_choice == 2:
        robot_weapon = "paper"
    else:
        robot_weapon = "scissors"

    Choice_of_weapon: str = input("What's your choice of weapon? ")
    if Choice_of_weapon == "rock":
        if robot_weapon == "paper":
            points -= 50
        if robot_weapon == "scissors":
            points += 50
        if robot_weapon == "rock":
            points = points

    if Choice_of_weapon == "paper":
        if robot_weapon == "scissors":
            points -= 50
        if robot_weapon == "rock":
            points += 50
        if robot_weapon == "paper":
            points = points

    if Choice_of_weapon == "scissors":
        if robot_weapon == "rock":
            points -= 50
        if robot_weapon == "paper":
            points += 50
        if robot_weapon == "scissors":
            points = points


def gamble(health: int) -> float:
    """Gamble your health!"""
    x: int = randint(1, 2)
    if x == 1:
        return health * 0.70
    else:
        return health * 1.25


def stop_playing() -> None:
    """Quits and resets the game."""
    print("Thanks for playing with us!")
    quit()


if __name__ == "__main__":
    main()