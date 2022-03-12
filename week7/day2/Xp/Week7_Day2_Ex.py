#import random

#----------------------------------- Exercise 1 : What Are You Learning ? ----------------------------------------

def display_message():
    print("I'm learning Python")

display_message()


#----------------------------------- Exercise 2: What’s Your Favorite Book ? ----------------------------------------


def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("war and peace")

#----------------------------------- Exercise 3 : Some Geography  ------------------------------------

def describe_city(city, country_of_city="planet earth"):
    print(f"{city} is in {country_of_city}")

describe_city("Santiago","Chile")
describe_city("Afula")

# ----------------------------------- Exercise 4 : Random -----------------------------------------

import random

def enter_number(num):
    if num > 0 and num < 101:
        random_num = random.randint(1,100)
        if num == random_num:
            print(f"SUCCESS! {num} matches our secret number {random_num}")
        else:
            print(f"FAIL! {num} do not match our secret number {random_num}")
    else:
        print("please run the function again with a number between 1 and 100")

enter_number(2)

# ------------------------------------ Exercise 5 : Let’s Create Some Personalized Shirts ! ----------------------

def make_shirt(size="large", text_to_print_on_shirt="I Love Python"):
    print(f'''
the size of the shirt is {size}
and the text will be {text_to_print_on_shirt}
    ''')

make_shirt("XXS","momo")
make_shirt()
make_shirt("medium")

# --------------------------------------- Exercise 6 : Magicians … ---------------------------------------------

magicians = ["Gandalf", "Marilin", "Houdini", "Uri Geller"]

def show_magicians(): #prints the items inside the list
    for magician in magicians:
        print(magician)

def make_great(): #modifys the items inside the list
    add_on = " the greate"
    x = 0
    for magician in magicians:
        magicians[x] += add_on
        x += 1

show_magicians()
make_great()
show_magicians()



