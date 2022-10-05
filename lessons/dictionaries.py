"""Demonstration of dictionary capabilities."""

# Declare the type of dictionary

schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Acces a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key.
# schools.pop("Duke")

# test for the existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")


# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {} # same as dict()
print(schools)
# alternatively, initialise key-value pairs
schools = {
    "UNC": 19400,
    "Duke": 3717,
    "NCSU": 26150
}
print(schools)

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")


print(schools[schools])