

                               # Week 6 Day 6 Xp

# ************************* Exercise 1 : Convert Lists Into Dictionaries ************************


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

nums_dict = dict(zip(keys,values))
#print(nums_dict)

# ************************* Exercise 2 : Cinemax #2 *******************************************

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

family_price = {}
total = 0

for key in family:
    if family[key] < 3:
        family_price[key] = 0
    if family[key] >= 3 and family[key] <= 12:
        family_price[key] = 10
    else: family_price[key] = 15

print(f"here is the price each family member should pay in dollars: {family_price}")

for key in family_price:
    total += family_price[key]

print(f"the total amount for the tickets is: {total}$")


# ************************* Exercise 3: Zara  *******************************************

brand = {
"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000 ,
"major_color": {
    "France": "blue",
    "Spain": "red",
    "US": ["pink", "green"]
    }
}

#Change the number of stores to 2
brand["number_stores"] = 2

#Print a sentence that explains who Zaras clients are
print(f"Zara's clients are everyone including {brand['type_of_clothes'][0]}, "
      f"{brand['type_of_clothes'][1]} and {brand['type_of_clothes'][2]}")

#Add a key called country_creation with a value of Spain
brand["country_creation"] = "spain"

#Check if the key international_competitors is in the dictionary. If it is, add the store Desigual
for i in brand:
    if i == "international_competitors":
        brand["international_competitors"].append("Desigual")

#Delete the information about the date of creation.
brand["creation_date"] = ""
#or if you ment:
del brand["creation_date"]

# Print the last international competitor
print(brand["international_competitors"][-1])

#Print the major clothes colors in the US
print(f"the major clothes colors in the US are {brand['major_color']['US'][0]} and "
      f"{brand['major_color']['US'][1]}")
#or put inside a var for future use:
us_colors = brand['major_color']['US']
print(f"the major clothes colors in the US are {us_colors[0]} and "
      f"{us_colors[1]}")

#Print the amount of key value pairs (ie. length of the dictionary)
keys_in_groupe = 0
for i in brand:
    keys_in_groupe += 1
print(f"the amount of keys in the brand dictionary are {keys_in_groupe}")

#Print the keys of the dictionary
for key, value in brand.items():
    print(key)

#Create another dictionary called more_on_zara with the following details:
#creation_date: 1975
#number_stores: 10000
more_on_zara = {"creation_date": 1975,"number_stores": 10000 }
brand.update(more_on_zara)

#Print the value of the key number_stores. What just happened ?
print(brand["number_stores"])
#it did not allow identical keys so so the update() did an overwrite to the value of the key instead.


# ************************* Exercise 4 : Disney Characters  *******************************************

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

#1.Use a for loop to recreate {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
users_index = []
for i,v in enumerate(users):
    users_index.append(i)

disney_users_A = dict(zip(users,users_index))
print(disney_users_A)

#2.Use a for loop to recreate {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
disney_users_B = dict(zip(users_index,users))
print(disney_users_B)

#3.Use a method to recreate {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
users.sort()
disney_users_C = dict(zip(users,users_index))
print(disney_users_C)


