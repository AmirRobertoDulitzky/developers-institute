

#-------------------------------- Week6 Day2 ------------------------------------------------------

#------------------------------------ Xp ----------------------------------------------------------

#------------------------------- Exercise 1 : Hello World -------------------------------------------
# Instructions:
# Print the following output in one line of code:

print("Goodby World\nGoodby World\nGoodby World\nGoodby World\n")

#------------------------------- Exercise 2 : Some Math -------------------------------------------

# Instructions:
# Write code that calculates the result of: (99^3) * 8 (99 to the power of 3 times 8)

cal = 99**3 * 8
print(cal)

#------------------------------- Exercise 3 : What Is The Output ? -------------------------------------------

# Instructions:
# Predict the output of the following code snippets:

# 5 < 3 expect: False
# 3 == 3 expect: True
# 3 == "3" expect: False
# "3" > 3 expect: False (outcome: eror)
# "Hello" == "hello" expect: False

# 5 < 3
print(5 < 3)
print(3 == 3)
print(3 == "3")
# print("3" > 3) Error
print("Hello" == "hello")

#------------------------------- Exercise 4 : Your Computer Brand -------------------------------------------

# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = "Lenovo"

print(f"I have a {computer_brand} computer")

#------------------------------- Exercise 5 : Your Information -------------------------------------------

# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = "John"
age = 40
shoe_size = 38
info = f"{name} is a strange guy. He wares 45 size shoes\n" \
       f"but it seems like his real shoe size is {shoe_size}.\n" \
       f"kind'a strange for a {age} years old guy."
print(info)

#------------------------------- Exercise 6 : A & B -------------------------------------------

# Create two variables, a and b.
# Each variables value should be a number.
# If a is bigger then b, have your code print Hello World.

a = 5
b = 2
if a> b:
    print("Goodby World")

#------------------------------- Exercise 7 : Odd Or Even -------------------------------------------

# Write code that asks the user for a number and determines whether this number is odd or even.

#remove from comment:

# num = int(input("choose a number")) # same as num = int(num)
#
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

#------------------------------- Exercise 8 : What’s Your Name ? -------------------------------------------

# Write code that asks the user for their name and determines whether or not you have the same name
# print out a funny message based on the outcome.

#remove from comment:

# my_name = "momo dodo"
# your_name = input("what is your name")
#
# if my_name == your_name:
#     print(f"my boss and I have the same name ({my_name})")
# else:
#     print(f"I thought my name is the bad. apparently yours is MUCH MUCH worse")

#------------------------------- Exercise 9 : Tall Enough To Ride A Roller Coaster -------------------------------------------

# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

#remove from comment:

# height = int(input("how tall are you (in inches please) "))
# height_in_cm = height * 2.54
#
# if height_in_cm > 145:
#     print("you are tall enough to ride")
# else:
#     print("you need to grow some more to ride")

#----------------------------- Daily Challange: Build up a string --------------------------------



# string = input("please enter a string")
# string_length = len(string)
# if string_length < 10:
#     print("string not long enough")
# elif string_length > 10:
#     print("string too long")
# else:
#     print(f"first char is {string[0]}")
#     print(f"last char is {string[-1]}")
#     print(string[0])
#     print(string[0:2])
#     print(string[0:3])
#     print(string[0:4])
#     print(string[0:5])
#     print(string[0:6])
#     print(string[0:7])
#     print(string[0:8])
#     print(string[0:9])
#     print(string[0:10])

   #----------I couldn't make the random.shuffle thing to work.
#    here is an example:
# import random
# x = "abcde"
# xy = random.shuffle(x)
# print(xy)