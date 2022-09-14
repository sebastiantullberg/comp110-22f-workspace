"""Examples of using lists in a single 'game'. """

# rolls - list of int values
# 2, 6, 4, 1
# total -> 8, then 12, then 13

from random import randint


rolls: list[int] = list()

# while the last values roll isn't == 1:
while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# Remove an item from the list by itsindex ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# sum the values of our rolls!
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i += 1

print(f"Total score: {sum}")

# " list of int" #blist[T] of type T
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# constructor list() creates and empty list in memory
# add items rolls.append(expr[t]) adds an item to the end of the list

# access and individual item. rolls[int expr] using subsciption notation to access 0-based indices
# print(rolls[0])
# print(rolls[1])

# access length of a list (number of items)
# print(len(rolls))

# # access the last item of a list. Numeric length to index
# last_index: int = len(rolls) - 1
# print(rolls[last_index])

# command + / to make everything comments

# words: list[str] = ["the", "quick", "fox"]
# print(words) -> ['the', 'quick', 'fox']
# print(words[0]) -> the
# square brackets - different meanings ind different context
# 1 data type ist[Type] list[str]
# 2 subscription op rolls[0] 0 is int expression
# 3 list literal [2, 4, 6]
# words[0] = "THE" -> print(words): ['The', 'quick', 'fox']
# words.append("!!!") -> ['The', 'quick', '!!!']