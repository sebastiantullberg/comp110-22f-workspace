
old: list[int] = [5, 3, 4, 3, 5, 5, 7]



new: list[int] = []
i: int = 0
while i < len(old):
    if old[i] % 2 == 1 and i % 2 == 0:
        new.append(old[i])
    i += 1
    

print(new)


