# Assignment 3:
"""
There is a list shown below titled original_list.

Using only what you've learned so far in the course,
write code to create a new list that contains the tuple sorted.

IMPORTANT: you must do this programmatically! Don't just
      hard code a new list with the values rearranged.
"""

original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]

# your code below:

nm1 = original_list[3][0]

nm2 = original_list[3][1]

nm3 = original_list[3][2]

my_list = [nm1,nm2,nm3]

my_list.sort()

my_tuple = (my_list[0],my_list[1],my_list[2])

original_list.pop()

original_list.append(my_tuple)

print(original_list)













































# Solution
# num1 = original_list[3][0]
# num2 = original_list[3][1]
# num3 = original_list[3][2]
# new_list = [num1, num2, num3]
# new_list.sort()
# new_tuple = (new_list[0], new_list[1], new_list[2])
# new_list = [original_list[0], original_list[1], original_list[2], new_tuple]
#
# print(new_list)
