"""An example of a list utility algorithm. """

# Name: contains
# function with 2 parameters:
#   needle - what we are searching for
#   haystack - what we are searching through
# Return type: bool
def contains(needle: str, haystack: list[str]) -> bool:
# start from first index
    i: int = 0
# loop through each index of list
    while i < len(haystack):
    #    Test if equal to needle
        if haystack[i] == needle:
    #    # Yes! Return True
            return True
        i += 1
# Return False
    return False

