"""
Import the "math" module. Then, print an alphabetically sorted list of all the functions available in the "math" module that start with the letters "is".
"""
# YOUR CODE HERE

import math

math_strings = dir(math)
math_list = [math_strings for math_strings in math_strings if math_strings.startswith("is")]

    

print(dir(math_list))