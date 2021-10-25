# http://learn.di-learning.com/courses/collection/18/course/12/section/52/chapter/211
# Exercise 1
print("hello world ".capitalize() * 4)

# Exercise 2
print((99 ** 3) * 8)

# Exercise 3
# Answers: False, True, False, TypeError, False

computer_brand = "Apple"  # Exercise 4
print(f"I have an {computer_brand} computer")

# Exercise 5
name = 'Ophir'
age = 29
shoe_size = 41
info = f'''My name is {name}, {age} years old.
I'm a web programmer. My shoe size is {shoe_size}'''

# Exercise 6
print(info)
a = 1
b = 1
if a > b:
    print('Hello World')

# Exercise 7
number = input('Write any number: ')
try:
    is_even = int(number) % 2 == 0
    if is_even:
        print(f'{number} is an even number')
    elif not isEven:
        print(f'{number} is an odd number')
except ValueError as error:
    print('You didn\'t give me a number!')

# Exercise 8
name = input('What\'s your name? ')
funny_message = f'Hey {name}, cool socks!'
print(funny_message)

# Exercise 9
height = input('What\'s your height in inches? ')
try:
    is_over_145_cm = float(height) * 2.54 > 145
    if is_over_145_cm:
        print('You can ride')
    else:
        print('Sorry you need to be taller to ride')
except ValueError as error:
    print('You didn\'t give me a number!')


# print('You can ride the roller coaster!')

# sentence = input('Please write a 10 character long string ')
# if len(sentence) < 10:
#     print('string not long enough')
#     exit()
# # new_sentence = list(sentence)
# # def()
