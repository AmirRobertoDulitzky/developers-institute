

#----------------------------- Daily Challange: Build up a string --------------------------------



string = input("please enter a string")
string_length = len(string)
if string_length < 10:
    print("string not long enough")
elif string_length > 10:
    print("string too long")
else:
    print(f"first char is {string[0]}")
    print(f"last char is {string[-1]}")
    print(string[0])
    print(string[0:2])
    print(string[0:3])
    print(string[0:4])
    print(string[0:5])
    print(string[0:6])
    print(string[0:7])
    print(string[0:8])
    print(string[0:9])
    print(string[0:10])

import random

str_var = list(string)
random.shuffle(str_var)
print(''.join(str_var))