"""This is one shot wordle"""

__author__ = "730523735"

#defining the boxes
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
emoji: str = ""
secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
i: int = 0
t: int = 0

while len(guess) != len(secret_word):                                                                           
    guess = input("That was not 6 letters! Try again ")      
    
#now we will go into the alternative if statement where the length is correct
if len(guess) == 6:
    if guess != secret_word:
        while i < len(secret_word):
            if guess[i] == secret_word[i]:
                emoji = (f"{emoji}{green_box}")
                i = i + 1 
            else:      
                emoji = (f"{emoji}{white_box}")
                i = i + 1     
        print(emoji)
        print("Not quite. Play again soon!")   
    else:
        while i < len(secret_word):
            if guess[i] == secret_word[i]:
                emoji = (f"{emoji}{green_box}")
                i = i + 1
        print(emoji)
        print("Woo! You got it!")    
             
    