lauren: str = "a friend"

def global_access() -> None:
    print(lauren)

global_access()


def a_forceful_stranger() -> None:
    global lauren
    lauren = "MY HORSE"
    print(lauren)

print(lauren)
# the func def makes lauren a horse for globals
a_forceful_stranger()

print(lauren)

