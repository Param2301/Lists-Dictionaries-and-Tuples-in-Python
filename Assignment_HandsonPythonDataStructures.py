# Task 1 - Working with Lists

my_fruits = ["apple", "strawberry", "banana", "mango", "kiwi"]

print("Original list:", my_fruits)

my_fruits.append("pineapple")
print("After adding a fruit:", my_fruits)

my_fruits.remove("apple")  
print("After removing a fruit:", my_fruits)

reversed_fruits = my_fruits[::-1]  
print("Reversed list:", reversed_fruits)

print("\n") 

# Task 2 - Exploring Dictionaries

my_info = {
   "name": "Param",
   "age": 20,
   "city": "Mumbai"
}

print("My information:", my_info)

my_info["favorite color"] = "Blue"
print("After adding favorite color:", my_info)

my_info["city"] = "Delhi"
print("After updating city:", my_info)


print("Keys:", end=" ")
for key in my_info:
   print(key, end=", ")
print() 

print("Values:", end=" ")
for key in my_info:
   print(my_info[key], end=", ")
print()

print("\n")  

# Task 3 - Using Tuples

favorite_things = ("Avengers: Endgame", "Perfect by Ed Sheeran", "Harry Potter")
print("Favorite things:", favorite_things)

try:
   favorite_things[0] = "The Dark Knight" 
except TypeError:
   print("Oops! Tuples cannot be changed.")

print("Length of tuple:", len(favorite_things))
