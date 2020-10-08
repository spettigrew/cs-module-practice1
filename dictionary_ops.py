"""
Add "Herb" to the phonebook with the number 7653420789.
Remove "Bill" from the phonebook.
"""
phonebook = {
    "Abe": 4569874321,
    "Bill": 7659803241,
    "Barry": 6573214789
}

# YOUR CODE HERE

phonebook["Herb"] = 7653420789

del phonebook["Bill"]


# Should print Herb is in the phonebook.
if "Herb" in phonebook:
    print("Herb is in the phonebook.")

# Should print Bill is not in the phonebook.
if "Bill" not in phonebook:
    print("Bill is not in the phonebook.")