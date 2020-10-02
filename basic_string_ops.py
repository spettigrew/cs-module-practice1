"""
Modify the "mystery_string" below until all of the print statements print as expected based on the comments above each print call expression.
"""
mystery_string = "Unlocking potentials regardless of circumstance."

# Should print out 48
print(len(mystery_string))

# Should print out 5
print(mystery_string.index("k"))

# Should print out 4
print(mystery_string.count("c"))

# Should print out "potential"
print(mystery_string[10:19])

# Should print out "sseldrager"
print(mystery_string[30:20:-1])

# Should print out "Ulcigptnil eadeso icmtne"
print(mystery_string[::2])

# Should print out True
print(mystery_string.startswith("Unlo"))

# Should print out True
print(mystery_string.endswith("stance."))

# Should print out 5
print(len(mystery_string.split()))