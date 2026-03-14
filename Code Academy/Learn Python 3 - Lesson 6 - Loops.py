"""
Introduction
Suppose we want to print() each item from a list of dog_breeds. We would need to use the following code snippet:

dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

print(dog_breeds[0])
print(dog_breeds[1])
print(dog_breeds[2])
print(dog_breeds[3])
print(dog_breeds[4])
This seems inefficient. Luckily, Python (and most other programming languages) gives us an easier way of using, or iterating through, every item in a list. We can use loops! A loop is a way of repeating a set of code many times.

In this lesson, we’ll be learning about:

Loops that let us move through each item in a list, called for loops
Loops that keep going until we tell them to stop, called while loops
Loops that create new lists, called list comprehensions


"""

dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)

'''
Create a For Loop
In the previous exercise, we saw that we can print each item in a list using a for loop. A for loop lets us perform an action on each item in a list. Using each element of a list is known as iterating.

This loop prints each breed in dog_breeds:

dog_breeds = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
    print(breed)
The general way of writing a for loop is:

for <temporary variable> in <list variable>:
    <action>
In our dog breeds example, breed was the temporary variable, dog_breeds was the list variable, and print(breed) was the action performed on every item in the list.

Our temporary variable can be named whatever we want and does not need to be defined beforehand. Each of the following code snippets does the exact same thing as our example:

for i in dog_breeds:
    print(i)
for dog in dog_breeds:
    print(dog)
Notice that in all of these examples the print statement is indented. Everything in the same level of indentation after the for loop declaration is included in the for loop, and run every iteration.

If we forget to indent, we’ll get an IndentationError.
'''

board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
    print(game)

for game in sport_games:
    print(game)

'''
Using Range in Loops
Previously, we iterated through an existing list.

Often we won’t be iterating through a specific list, we’ll just want to do a certain action multiple times. For example, if we wanted to print out a "WARNING!" message three times, we would want to say something like:

for i in <a list of length 3>:
  print("WARNING!")
Notice that we need to iterate through a list of length 3, but we don’t care what’s in the list. To create these lists of length n, we can use the range function. range takes in a number n as input, and returns a list from 0 to n-1. For example:

zero_thru_five = range(6)
# zero_thru_five is now [0, 1, 2, 3, 4, 5]
zero_thru_one = range(2)
# zero_thru_one is now [0, 1]
So, an easy way to accomplish our "WARNING!" example would be:

for i in range(3):
  print("WARNING!")

'''

#Use the range function in a for loop to print out promise 5 times.

promise = "I will not chew gum in class"
for x in range(5):
    print(promise)

'''
Infinite Loops
We’ve iterated through lists that have a discrete beginning and end. However, let’s consider this example:

my_favorite_numbers = [4, 8, 15, 16, 42]

for number in my_favorite_numbers:
  my_favorite_numbers.append(1)
What happens here? Every time we enter the loop, we add a 1 to the end of the list that we are iterating through. As a result, we never make it to the end of the list! It keeps growing!

A loop that never terminates is called an infinite loop. These are very dangerous for your code!

A program that hits an infinite loop often becomes completely unusable. The best course of action is to never write an infinite loop.

Note: If you accidentally stumble into an infinite loop while developing on your own machine, you can end the loop by using control + c to terminate the program. If you’re writing code in our online editor, you’ll need to refresh the page to get out of an infinite loop!

'''

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)
    print(student)

print(students_period_B)

'''
Break
We often want to use a for loop to search through a list for some value:

items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]

# we want to check if the item with ID "knit_dress" is on sale:
for item in items_on_sale:
  if item == "knit_dress":
    print("Knit Dress is on sale!")
This code goes through each item in items_on_sale and checks for a match. After we find that "knit_dress" is in the list items_on_sale, we don’t need to go through the rest of the items_on_sale list. Since it’s only 5 elements long, iterating through the entire list is not a big deal in this case. But what if items_on_sale had 1000 items after "knit_dress"? What if it had 100,000 items after "knit_dress"?

You can stop a for loop from inside the loop by using break. When the program hits a break statement, control returns to the code outside of the for loop. For example:

items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]

print("Checking the sale list!")
for item in items_on_sale:
  print(item)
  if item == "knit_dress":
    break
print("End of search!")
This would produce the output:

Checking the sale list!
blue_shirt
striped_socks
knit_dress
End of search!
We didn’t need to check "red_headband" or "dinosaur_onesie" at all!

'''

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

'''
You have a list of dog breeds you can adopt, dog_breeds_available_for_adoption. Using a for loop, iterate through the dog_breeds_available_for_adoption list and print out each dog breed.
'''

for dog in dog_breeds_available_for_adoption:
    print(dog)
    if dog == dog_breed_I_want:
        print("They have the dog I want!")
        break

'''
Continue
When we’re iterating through lists, we may want to skip some values. Let’s say we want to print out all of the numbers in a list, unless they’re negative. We can use continue to move to the next i in the list:

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
  if i < 0:
    continue
  print(i)
This would produce the output:

1
2
4
5
2
Every time there was a negative number, the continue keyword moved the index to the next value in the list, without executing the code in the rest of the for loop.
'''

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

'''
Your computer is the doorman at a bar in a country where the drinking age is 21.

Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print the age.
'''

for age in ages:
    if age < 21:
        continue
    print(age)

'''
While Loops
We now have seen and used a lot of examples of for loops. There is another type of loop we can also use, called a while loop. The while loop performs a set of code until some condition is reached.

While loops can be used to iterate through lists, just like for loops:

dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

index = 0
while index < len(dog_breeds):
    print(dog_breeds[index])
    index += 1
Every time the condition of the while loop (in this case, index < len(dog_breeds)) is satisfied, the code inside the while loop runs.

While loops can be useful when you don’t know how many iterations it will take to satisfy a condition.

'''

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

#You are adding students to a Poetry class, the size of which is capped at 6. While the length of the students_in_poetry list is less than 6, use .pop() to take a student off the all_students list and add it to the students_in_poetry list.

while len(students_in_poetry) < 6:
        students_in_poetry.append(all_students.pop())
        print(students_in_poetry)


'''
Nested Loops
We have seen how we can go through the elements of a list. What if we have a list made up of multiple lists? How can we loop through all of the individual elements?

Suppose we are in charge of a science class, that is split into three project teams:

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
If we want to go through each student, we have to put one loop inside another:

for team in project_teams:
  for student in team:
    print(student)
This results in:

Ava
Samantha
James
Lucille
Zed
Edgar
Gabriel
'''

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
#We have provided the list sales_data that shows the numbers of different flavors of ice cream sold at three different locations of the fictional shop, Gilbert and Ilbert’s Scoop Shop. We want to sum up the total number of scoops sold. Start by defining a variable scoops_sold and set it to zero.
scoops_sold = 0

#Go through the sales_data list. Call each inner list location, and print out each location list.
for location in sales_data:
    print(location)
    #Within the sales_data loop, go through each location list and add the element to your scoops_sold variable.
    #By the end, you should have the sum of every number in the sales_data nested list.
    for data in location:
        scoops_sold += data

print(scoops_sold)

'''
List Comprehensions
Let’s say we have scraped a certain website and gotten these words:

words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
We want to make a new list, called usernames, that has all of the strings in words with an '@' as the first character. We know we can do this with a for loop:

words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)
First, we created a new empty list, usernames, and as we looped through the words list, we added every word that matched our criterion. Now, the usernames list looks like this:

>>> print(usernames)
["@coolguy35", "@kewldawg54", "@matchamom"]
Python has a convenient shorthand to create lists like this with one line:

usernames = [word for word in words if word[0] == '@']
This is called a list comprehension. It will produce the same output as the for loop did:

["@coolguy35", "@kewldawg54", "@matchamom"]
This list comprehension:

Takes an element in words
Assigns that element to a variable called word
Checks if word[0] == '@', and if so, it adds word to the new list, usernames. If not, nothing happens.
Repeats steps 1-3 for all of the strings in words
Note: if we hadn’t done any checking (let’s say we had omitted if word[0] == '@'), the new list would be just a copy of words:

usernames = [word for word in words]
#usernames is now ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
'''

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

#We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters. Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.
can_ride_rollercoaster = []
can_ride_rollercoaster = [height for height in heights if height > 161]
print(can_ride_rollercoaster)

'''
More List Comprehensions
Let’s say we’re working with the usernames list from the last exercise:

>>> print(usernames)
["@coolguy35", "@kewldawg54", "@matchamom"]
We want to create a new list with the string " please follow me!" added to the end of each username. We want to call this new list messages. We can use a list comprehension to make this list with one line:

messages = [user + " please follow me!" for user in usernames]
This list comprehension:

Takes a string in usernames
Assigns that string to a variable called user
Adds “ please follow me!” to user
Appends that concatenation to the new list called messages
Repeats steps 1-4 for all of the strings in usernames
Now, messages contains these values:

["@coolguy35 please follow me!", "@kewldawg54 please follow me!", "@matchamom please follow me!"]
Being able to create lists with modified values is especially useful when working with numbers. Let’s say we have this list:

my_upvotes = [192, 34, 22, 175, 75, 101, 97]
We want to add 100 to each value. We can accomplish this goal in one line:

updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]
This list comprehension:

Takes a number in my_upvotes
Assigns that number to a variable called vote_value
Adds 100 to vote_value
Appends that sum to the new list updated_upvotes
Repeats steps 1-4 for all of the numbers in my_upvotes
Now, updated_upvotes contains these values:

[292, 134, 122, 275, 175, 201, 197]
'''
celsius = [0, 10, 15, 32, -5, 27, 3]

'''
We have provided a list of temperatures in celsius. Using a list comprehension, create a new list called fahrenheit that converts each element in the celsius list to fahrenheit.

*Note: * To convert, use the formula:

temperature_in_fahrenheit = temperature_in_celsius * 9/5 + 32
'''
fahrenheit = []
fahrenheit = [(temperature * 9/5 + 32) for temperature in celsius]
print(fahrenheit)

'''
Review
Good job! In this lesson, you learned

how to write a for loop
how to use range in a loop
what infinite loops are and how to avoid them
how to skip values in a loop
how to write a while loop
how to make lists with one line
Let’s get some more practice with these concepts!
'''

#Create a list called single_digits that consists of the numbers 0-9 (inclusive).

single_digits = list(range(0,10))
print(single_digits)

squares = []
#Create a for loop that goes through single_digits and prints out each one.
for digit in single_digits:
    print(digit)
    squares.append(digit ** 2)

print(squares)
#Before the loop, create a list called squares. Assign it to be an empty list to begin with.

#Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.

#Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.

cubes = []
cubes = [digit ** 3 for digit in single_digits]

print(cubes)
