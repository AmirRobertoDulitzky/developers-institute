#------------------ Week6 Day4 Xp --------------------------------

# ------------------------------------------ Exercise 1 : Favorite Numbers ---------------------------------

# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

#1
my_fav_numbers = {10,20,30,40,50}
print(my_fav_numbers)

#2
my_fav_numbers.add(60)
my_fav_numbers.add(70)
print(my_fav_numbers)

#3
my_fav_numbers.discard(70)
print(my_fav_numbers)

#4
friend_fav_numbers = {80,90}

#5
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)


# ------------------------------------------ Exercise 2: Tuple ---------------------------------
print("")
#Given a tuple which value is integers, is it possible to add more integers to the tuple?

#ANSWER:
#no. a tuple is immutable

# ------------------------------------------ Exercise 3: Print A Range Of Numbers ---------------------------------

#Use a for loop to print all numbers from 1 to 20, inclusive

nums = range(1,21)

for num in nums:
    print(num)

# ------------------------------------------ Exercise 4: Floats ---------------------------------
print("")
#1 Recap – What is a float? What is the difference between an integer and a float?
#2 Can you think of another way to generate a sequence of floats?
#3 Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

#1

#ANSWER:
#INT = 1
#FLOAT = 1.0

#2

#ANSWER:
# no.

#3

int_and_floats = [1.5]
while int_and_floats[-1] < 5:
    int_and_floats.append(int_and_floats[-1]+0.5)
    if (int_and_floats[-1]).is_integer():
        int_and_floats[-1] = int(int_and_floats[-1])

print(int_and_floats)

# ------------------------------------------ Exercise 5: Shopping List ---------------------------------
print("")
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
#1 Remove “Banana” from the list.
#2 Remove “Blueberries” from the list.
#3 Add “Kiwi” to the end of the list.
#4 Add “Apples” to the beginning of the list.
#5 Count how many apples are in the basket.
#6 Empty the basket.
#7 Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)

#1
basket.remove("Banana")
print(basket)

#2
basket.pop(-1)
print(basket)

#3
basket.append("Kiwi")
print(basket)

#4
basket.insert(0,"Apples")
print(basket)

#5
new_list = []

for x in basket:
  if "Apples" in x:
    new_list.append(x)

print(f" there are {len(new_list)} {new_list[0]} in the basket")

#6 and 7
basket.clear()
print(basket)


# ------------------------------------------ Exercise 6 : Loop --------------------------------------------

# ************ REMOVE COMMENT TO ACTIVATE CODE: **********************

# print("")

#OP1:
# name = ""
#
# while name != "momo":
#    name = input("what is your name?")
# print("we have the same name")

#Op2:
# while True:
#     name2 = input("what is your name?")
#     if name2 == "koko":
#         break
# print("we have the same name")

# ------------------------------------------ Exercise 7 --------------------------------------------------
print("")
# Given a list, use a loop to print out every element which has an even index.

nums = [3,5,8,9,11,14]

for num in nums:
    if num % 2 == 0:
        print(num)

# ------------------------------------------ Exercise 8 --------------------------------------------------
print("")
#Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

numbers = range(1,22)

for x in numbers:
    if x % 5 == 0 or x % 7 == 0:
        print(x)

# ------------------------------------------ Exercise 9: Favorite Fruits --------------------------------------------------

#1 Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
#2 Store the favorite fruit(s) in a list (convert the string of words into a list of words).
#3 Now that we have a list of fruits, ask the user to input a name of any fruit.
#4 If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# ************ REMOVE COMMENT TO ACTIVATE CODE: **********************

# print("")
# #1
# fruits_from_user = input("choose your favorite fruits (put a space between them)")
#
# #2
# fav_fruits = list(fruits_from_user.split(" "))
# print(fav_fruits)
#
# #3
# another_fruit = input("choose another fruit")
#
# #4
# for x in fav_fruits:
#     if x == another_fruit:
#         print("You chose one of your favorite fruits! Enjoy!")
#     else:
#         print("You chose a new fruit. I hope you like it.")
#         break


# ------------------------------------------ Exercise 10: Who Ordered A Pizza ? --------------------------------------------------

#1 Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
#2 As they enter each topping, print a message saying you’ll add that topping to their pizza.
#3 Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

# ************ REMOVE COMMENT TO ACTIVATE CODE: **********************

# print("")
# active = True
# toppings = []
#
# while active:
#     topping = input("Please choose a topping for your pizza one at a time (enter 'exit' when you are finished): ")
#     if topping != 'exit':
#         toppings.append(topping)
#         print(f"{toppings[-1]} will be added to your pizza")
#     else:
#         active = False
#
# toppings_str = ", ".join(toppings)
# total = 10 + (len(toppings) * 2.5)
# print(f"your toppings are: {toppings_str}")
# print(f'your total is: ש"ח{total}')

# ------------------------------------------ Exercise 11: Cinemax --------------------------------------------------

# ************ REMOVE COMMENT TO ACTIVATE CODE: **********************

# print("")
#1 - 3:
# activate = True
# family = []
#
# while activate:
#     member_age = input("how old are you? (type 'exit' to calculate the sum of the tickets)")
#     if member_age == "exit":
#         activate = False
#     else:
#         member_age = int(member_age)
#         family.append(member_age)
#
# print(f"family ages: {family}")
#
# tickets = []
# for age in family:
#     if age >= 3 and age <= 12:
#         tickets.append(10)
#     elif age > 12:
#         tickets.append(15)
#
# print(f"price of family's individual tickets: {tickets}")
#
# total = 0
# for ticket_price in tickets:
#     total += ticket_price
#
# print(f"total price is: {total}")

#4:

# ************ REMOVE COMMENT TO ACTIVATE CODE: **********************

# print("")
# activating = True
# people = []
# people_names = []
#
# while activating:
#     person_name = input("whats your name")
#     person_age = input("how old are you?")
#     person_age = int(person_age)
#     if person_age >= 16 and person_age <= 21:
#         people_names.append(person_name)
#     exit = input("are you finished? (type in 'yes' to exit)")
#     if exit == "yes":
#         activating = False
# print(f'people allowed to watch the movie: {", ".join(people_names)}')


# ------------------------------------------ Exercise 12 : Who Is Under 16? --------------------------------------------------

# ************ REMOVE COMMENT TO ACTIVATE CODE: **********************

# print("")
#
# names = ["john","paul","george","ringo"]
# names_copy = []
#
#
#
# for name in names:
#     names_copy.append(name)
#     age = int(input("how old are you?"))
#     if age < 16:
#         names_copy.remove(name)
#
# names = names_copy
# print(f'above the age of 16: {", ".join(names)}')

# ------------------------------------------ Exercise 13 and 14 --------------------------------------------------

#                                                ***13***:
#1 Make a list called sandwich_orders and fill it with the names of various sandwiches .
#2 Then make an empty list called finished_sandwiches.
#3 As each sandwich is made, move it to the list of finished sandwiches.
#4 After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

#                                                ***14***:
#1 Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.
#2 Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
#3 Make sure no pastrami sandwiches end up in finished_sandwiches.

# ************ REMOVE COMMENT TO ACTIVATE CODE: **********************

# print("")
#
# sandwich_orders = ["tuna","salmon","avocado","egg","pastrami","pastrami","pastrami"]
# finished_sandwiches = []
#
# activated = True
# print("sorry, there is no pastrami left")
#
# while activated:
#     for sandwich in sandwich_orders:
#         if "pastrami" in sandwich_orders:
#             sandwich_orders.remove("pastrami")
#         if sandwich in finished_sandwiches:
#             continue
#         is_ready = input(f"is {sandwich} ready?")
#         if is_ready == "yes":
#             finished_sandwiches.append(sandwich)
#         if sandwich in finished_sandwiches and len(sandwich_orders) == len(finished_sandwiches):
#             activated = False
# print(f'your sandwiches are ready: {", ".join(finished_sandwiches)}')









