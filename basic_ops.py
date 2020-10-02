"""
1. Assign two different types to the variables "a" and "b".

2. Use basic operators to create a list that contains three instances of "a" and three instances of "b".
"""
# Modify the code below to meet the requirements outlined above
a = object()
b = object()

a_list = [a] * 2
b_list = [b] * 4

my_list = a_list + b_list

print(len(my_list))