
"""An example function definition."""

#First line (following) is the signature line (contract)
def my_max(a: int, b: int) -> int:
    """Returns the largest argument"""
    if a >= b:
        return a
    return b       



       

#line 7-10 is body block

#my_max is an identifier
#order and types of parameters
#return type is the arrow

print(my_max(10 +1 , 10))

#see more in gradescope lesson 12