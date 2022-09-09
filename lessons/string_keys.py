#string(110) => "110"

#"COMP" + str(110) => "COMP110"

#sequence of characters 

#characters is not the same as letters

#every character has a corresponding int value.#


print(ord("C"))

print(chr(8))

#lowercase > uppercase

print(chr(1))
print("MX")

print(ord("C") > ord("A"))

#so C is greater than A because 67 > 65

print("C" > "A")
"C is also greater than A here"

print(chr(34))

print("The \U0001F1F2 is worse than \U0001F1F0!")

print(ord("d"))
print(ord("U"))

print(chr(129313))

#U is an indication that what will follow is an 8-digit hex representation of a unicode character
#remember quotation marks for strings
emoji: str = "\U0001F920\U0001F40E"
print(emoji)
print(len(emoji))
print(emoji[0])

#Escape Sequence	Meaning
# \"	Double quote (")
# \'	Single quote (')
# \t	Tab
# \n	New Line
# \Uxxxxxxxx	32-bit unicode character
# \\	Backslash (\)
print("The computer said, \"Hello, world.\"")

#f string

names: str = "isabela"
age_turning: int = 20
birth_date: str = "February 2nd"

print(f"Hello {names} you are turning {age_turning} on {birth_date}")

print(f"110 is on a \U0001F6A2")

print("Hello\nworld\n!!!")


age: int = 21
msg: str = f"You are {age}!"
print(msg)