import random

# Challenge: Build up a string
while True:
    sentence = input('Please write a 10 character long string: ')
    if len(sentence) > 10:
        current = ''
        for char in sentence:
            current += char
            print(current)
        break
chars = list(sentence)
random.shuffle(chars)
print(''.join(chars))