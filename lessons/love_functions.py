"""So e tender, loving functions."""
def love(subject: str) -> str:
    """giving a subject as a parameter, returns a loving string."""
    return f"I love you {subject}!"

#no parenthesis for return because return is not a function call

print(love("Seb"))


def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love_note(to) + "\n"
        i += 1
    return love_note
print(spread_love("Seb", 2))


#something is wrong