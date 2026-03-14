"""

CREATING DICTIONARIES
Introduction to Dictionary
A dictionary is an unordered set of key: value pairs.

It provides us with a way to map pieces of data to each other so that we can quickly find values that are associated 
with one another. 

Suppose we want to store the prices of various items sold at a cafe:

Avocado Toast is 6 dollars
Carrot Juice is 5 dollars
Blueberry Muffin is 2 dollars
In Python, we can create a dictionary called menu to store this data:

menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
Notice that:

A dictionary begins and ends with curly braces { and }.
Each item consists of a key ("avocado toast") and a value (6).
Each key: value pair is separated by a comma.
It’s considered good practice to insert a space () after each comma, but our code will still run without the space.

"""

# Suppose we have a dictionary of temperature sensors in the house and what temperatures they read. We’ve just added
# a sensor to the "pantry", and it reads 22 degrees.
#
# Add this pair to the dictionary on line 1.

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

# Remove the # in front of the definition of the dictionary num_cameras, which represents the number of cameras in each area around the house.

# If you run this code, you’ll get an error:
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)

'''

Make a Dictionary In the previous exercise, we saw a dictionary that maps strings to numbers (i.e., "avocado toast": 
6). However, the keys can be numbers as well. 

For example, if we were mapping restaurant bill subtotals to the bill total after tip, a dictionary could look like:

subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18} Values can be of any type. We can use a string, a number, a list, 
or even another dictionary as the value associated with a key! 

For example:

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", 
"Marco"], "philosophy": ["Frederica", "Manuel"]} The list ["Aaron", "Delila", "Samson"], which is the value for the 
key "software design", represents the students in that class. 

We can also mix and match key and value types. For example:

person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}

'''

# Create a dictionary called translations that maps the following words in English to their definitions in Sindarin (
# the language of the elves):

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

print(translations)

'''Invalid Keys We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these 
data types as keys of the dictionary. If we try to, we will get a TypeError. 

For example:

powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
This code will yield:

TypeError: unhashable type: 'list'
The word “unhashable” in this context means that this ‘list’ is an object that can be changed.

Dictionaries in Python rely on each key having a hash value, a specific identifier for the key. If the key can 
change, that hash value would not be reliable. So the keys must always be unchangeable, hashable data types, 
like numbers or strings. 

'''

# Run the code inside script.py. You should get an error: children = {["Johannes", "Rosmarie", "Eleonore"]: "von
# Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"} TypeError: unhashable type Make the code run without errors by
# flipping the items in the dictionary so that the strings are the keys and the lists are the values

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

print(children)

''' 
# Empty Dictionary A dictionary doesn’t have to contain anything. Sometimes we need to create an empty dictionary
# when we plan to fill it later based on some other input.
#
# We can create an empty dictionary like this:
#
# empty_dict = {}

'''

# Create an empty dictionary called my_empty_dictionary.
my_empty_dictionary = {}

print(my_empty_dictionary)

''' 
Add A Key
To add a single key: value pair to a dictionary, we can use the syntax:

dictionary[key] = value
For example, if we had our menu dictionary from the first exercise:

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
And we wanted to add a new item, "cheesecake" for 8 dollars, we could use:

menu["cheesecake"] = 8
Now, menu looks like:

{"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}
'''

# Create an empty dictionary called animals_in_zoo.

animals_in_zoo = {}

# Walking around the zoo, you see 8 zebras. Add "zebras" to animals_in_zoo as a key with a value of 8.

animals_in_zoo["zebras"] = 8

# The primate house was bananas! Add "monkeys" to animals_in_zoo as a key with a value of 12.

animals_in_zoo["monkeys"] = 12

# As you leave the zoo, you are saddened that you did not see any dinosaurs. Add "dinosaurs" to animals_in_zoo as a
# key with a value of 0.

animals_in_zoo["dinosaurs"] = 0

# Print animals_in_zoo.

print(animals_in_zoo)

''' 
Add Multiple Keys
If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

Looking at our sensors object from a previous exercise:

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
If we wanted to add 3 new rooms, we could use:

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
This would add all three items to the sensors dictionary.

Now, sensors looks like:

{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}

'''

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

# In one line of code, add two new users to the user_ids dictionary:
#
# theLooper, with an id of 138475
# stringQueen, with an id of 85739

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)

''' 
Overwrite Values
We know that we can add a key by using syntax like:

menu["avocado toast"] = 7 This will create a key "avocado toast" and set the value to 7. But what if we already have 
an 'avocado toast' entry in the menu dictionary? 

In that case, our value assignment would overwrite the existing value attached to the key 'avocado toast'.

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)
This would yield:

{"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
Notice the value of "oatmeal" has now changed to 5.

'''

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

# Add the key "Supporting Actress" and set the value to "Viola Davis".

oscar_winners.update({"Supporting Actress": "Viola Davis"})

print(oscar_winners)

# Without changing the definition of the dictionary oscar_winners, change the value associated with the key "Best
# Picture" to "Moonlight".

oscar_winners["Best Picture"] = "Moonlight"

print(oscar_winners)

'''List Comprehensions to Dictionaries Let’s say we have two lists that we want to combine into a dictionary, 
like a list of students and a list of their heights, in inches: 

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
Python allows you to create a dictionary using a list comprehension, with this syntax:

students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
Remember that zip() combines two lists into a zipped list of pairs. This list comprehension:

Takes a pair from the zipped list of pairs from names and heights Names the elements in the pair key (the one 
originally from the names list) and value (the one originally from the heights list) Creates a key : value item in 
the students dictionary Repeats steps 1-3 for the entire list of pairs 

'''

# You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First,
# create a variable called zipped_drinks that is a zipped list of pairs between the drinks list and the caffeine list.

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks,caffeine)
print(zipped_drinks)
#zipped_drinks = {key:value for key, value in zip(drinks,caffeine)}

# Create a dictionary called drinks_to_caffeine by using a list comprehension that goes through the zipped_drinks
# list and turns each pair into a key:value item.


drinks_to_caffine = {key:value for key, value in zipped_drinks}

print(drinks_to_caffine)

''' 

Review
So far we have learned:

How to create a dictionary
How to add elements to a dictionary
How to update elements in a dictionary
How to use a list comprehension to create a dictionary from two lists
Let’s practice these skills!

'''
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# We are building a music streaming service. We have provided two lists, representing songs in a user’s library and
# the amount of times each song has been played.
#
# Using a list comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a
# song:playcount pair for each song in songs and each playcount in playcounts.

plays = {key:value for key, value in zip(songs,playcounts)}

print(plays)

# After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1.

plays.update({"Purple Haze": 1})

print(plays)

# This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for "Respect"
# to be 94 in the plays dictionary.

plays["Respect"]=94

print(plays)

''' 

Create a dictionary called library that has two key: value pairs:

key "The Best Songs" with a value of plays, the dictionary you created
key "Sunday Feelings" with a value of an empty dictionary

'''

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)