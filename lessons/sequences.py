"""Notes and examples of tuple and ramge sequences types."""

# Sequence is an abstract data type ordered in 0-indexed set of values

# there are many specific types of sequences 
#1 str - a seq of char data
#2 list - dynamically sized seq of vals of a specif type
#3 tuple - a fixed size sequence of values of any type
#4 range - a sequence of integers at intervals 

# tuples: ex: tuple[int, str] = ("Bacot, 5")
# ex[0] -> Bacot
# ex[1] -> 5
# origin: point2d = (0.0, 0.0)

# declaring a type alias that "invents" the point2d type
from re import A


Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10.0)
start_position = (start_position[0] + 5.0, start_position[1] + 10.0)
end_position: Point2D = (99.0, 99.0)

# tuples are 0 indexed because they are a sequence
print(start_position[0])

# you can't append or change a tuple

for item in end_position:
    print(item)


"""Ranges"""
# range(start: int, stop: int[, step. int = 1]) -> range

a_range: range = range(0, 10, 3)
# access its items
print(a_range[0])
print(a_range[1])
print(len(a_range))
for i in a_range:
    print(i)


# An example of using the default parameter step
# where the default step is 1

another_range: range = range(0, 10)

# if you only pass one argument to range, it specifies
# the stop marker and start is 0 by default
zero_start: range = range(10)
