# import numpy as np  (need help installing)

# http://learn.di-learning.com/courses/collection/18/course/12/section/53/chapter/231
# Exercise 1
my_fav_numbers = {1, 2, 3, 7}
print(f'My favorite numbers are: {my_fav_numbers}')
my_fav_numbers.update([8, 9])
print(f'Add these numbers to my favorite numbers: {my_fav_numbers}')
my_fav_numbers.remove(max(my_fav_numbers))
print(f'Now, my favorite numbers are: {my_fav_numbers}')
friend_fav_numbers = {10, 11}
print(f'Friend\'s favorite numbers are: {friend_fav_numbers}')
our_fav_numbers = set.union(my_fav_numbers, friend_fav_numbers)
print(f'Our favorite numbers are: {our_fav_numbers}')

# Exercise 2
# Tuples can not be removed, added to or updated.

# Exercise 3
for x in range(0, 21):
    print(x)

# Exercise 4
# 1. Floats contain decimal point and are used when precision is required for a specific task.
#    Integers are whole numbers and are used in iterating (counting, etc)
# 2.
print(range(0, 4))
# 3.
# for i in np.arange(0.5, 5.5, 0.5): (need help installing)
#     print(i)

