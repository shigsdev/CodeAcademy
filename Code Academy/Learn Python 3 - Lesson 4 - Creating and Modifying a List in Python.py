'''
What is a list?
A list is an ordered set of objects in Python.

Suppose we want to make a list of the heights of students in a class:

Jenny is 61 inches tall
Alexus is 70 inches tall
Sam is 67 inches tall
Grace is 64 inches tall
In Python, we can create a variable called heights to store these numbers:

heights = [61, 70, 67, 64]
Notice that:

A list begins and ends with square brackets ([ and ]).
Each item (i.e., 67 or 70) is separated by a comma (,)
It’s considered good practice to insert a space () after each comma, but your code will run just fine if you forget the space.


'''

'''
A new student just joined the class:

Cole is 65 inches tall
Add Cole’s height to the end of the list heights.
Remove the # in front of the definition of the list broken_heights. If you run this code, you’ll get an error:

SyntaxError: invalid syntax
Add commas (,) to broken_heights so that it runs without errors.

'''

heights = [61, 70, 67, 64, 65]

print(heights)
broken_heights = [65, 71, 59, 62]
print(broken_heights)

'''
Lists II
Lists can contain more than just numbers.

Let’s revisit our height example:

Jenny is 61 inches tall
Alexus is 70 inches tall
Sam is 67 inches tall
Grace is 64 inches tall
We can make a list of strings that contain the students’ names:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
We can also combine multiple data types in one list. For example, this list contains both a string and an integer:

mixed_list = ['Jenny', 61]

'''

ints_and_strings = [1, 2, 3, 'four', 'five', 'scott']

'''
Create a new list called sam_height that contains:

The string 'Sam'
The number 67

'''

sam_height = ['Sam', 67]

'''
List of Lists
We’ve seen that the items in a list can be numbers or strings. They can also be other lists!

Once more, let’s return to our class height example:

Jenny is 61 inches tall
Alexus is 70 inches tall
Sam is 67 inches tall
Grace is 64 inches tall
Previously, we saw that we could create a list representing both Jenny’s name and height:

jenny = ['Jenny', 61]
We can put several of these lists into one list, such that each entry in the list represents a student and their height:

heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64]]

'''

# A new student named 'Vik' has joined our class. Vik is 68 inches tall. Add a sublist to heights that represents Vik and his height.

heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]

ages = [['Aaron', 15], ['Dhrutti', 16]]

'''
Zip
Again, let’s return to our class height example:

Jenny is 61 inches tall
Alexus is 70 inches tall
Sam is 67 inches tall
Grace is 64 inches tall
Suppose that we already had a list of names and a list of heights:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 65]
If we wanted to create a list of lists that paired each name with a height, we could use the command zip. zip takes two (or more) lists as inputs and returns an object that contains a list of pairs. Each pair contains one element from each of the inputs. You won’t be able to see much about this object from just printing it:

names_and_heights = zip(names, heights)
print(names_and_heights)
because it will return the location of this object in memory. Output would look something like this:

<zip object at 0x7f1631e86b48>
To see the nested lists, you can convert the zip object to a list first:

print(list(names_and_heights))
returns:

[('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 65)]
Use zip to create a new variable called names_and_dogs_names that combines names and dogs_names into a zip object.

Make sure to run the code for this step before proceeding to the next instruction!
'''
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

'''
Empty Lists
A list doesn’t have to contain anything! You can create an empty list like this:

empty_list = []
Why would we create an empty list?

Usually, it’s because we’re planning on filling it later based on some other input. We’ll talk about two ways of filling up a list in the next exercise.

Instructions
1.
Create an empty list and call it my_empty_list.
'''

my_empty_list = []

'''
Growing a List: Append
We can add a single element to a list using .append(). For example, suppose we have an empty list called empty_list:

empty_list = []
We can add the element 1 using the following commands:

empty_list.append(1)
If we examine empty_list, we see that it now contains 1:

>>> print(empty_list)
[1]
When we use .append() on a list that already has elements, our new element is added to the end of the list:

# Create a list
my_list = [1, 2, 3]

# Append a number
my_list.append(5)
print(my_list) # check the result
the output looks like:

[1, 2, 3, 5]
It’s important to remember that .append() comes after the list. This is different from functions like print, which come before.

'''

orders = ['daisies', 'periwinkle']

print(orders)

orders.append('tulips')

print(orders)

orders.append('roses')

print(orders)

'''
Growing a List: Plus (+)
When we want to add multiple items to a list, we can use + to combine two lists.

Below, we have a list of items sold at a bakery called items_sold:

items_sold = ['cake', 'cookie', 'bread']
Suppose the bakery wants to start selling 'biscuit' and 'tart':

>>> items_sold_new = items_sold + ['biscuit', 'tart']
>>> print(items_sold_new)
['cake', 'cookie', 'bread', 'biscuit', 'tart']
In this example, we created a new variable, items_sold_new, which contained both the original items sold, and the new ones. We can inspect the original items_sold and see that it did not change:

>>> print(items_sold)
['cake', 'cookie', 'bread']
We can only use + with other lists. If we type in this code:

my_list = [1, 2, 3]
my_list + 4
we will get the following error:

TypeError: can only concatenate list (not "int") to list
If we want to add a single element using +, we have to put it into a list with brackets ([]):

my_list + [4]

'''
orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

# Create new orders here:
new_orders = orders + ['lilac'] + ['iris']

'''
Remove the # in front of the list broken_prices. If you run this code, you’ll get an error:

TypeError: can only concatenate list (not "int") to list
Fix the command by inserting brackets ([ and ]) so that it will run without errors.
'''
broken_prices = [5, 3, 4, 5, 4] + [4]

'''
Range I
Often, we want to create a list of consecutive numbers. For example, suppose we want a list containing the numbers 0 through 9:

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Typing out all of those numbers takes time and the more numbers we type, the more likely it is that we have a typo.

Python gives us an easy way of creating these lists using a function called range. The function range takes a single input, and generates numbers starting at 0 and ending at the number before the input. So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:

my_range = range(10)
Just like with zip, the range function returns an object that we can convert into a list:

>>> print(my_range)
range(0, 10)
>>> print(list(my_range))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

'''
Modify list1 so that it is a range containing numbers starting at 0 and up to, but not including, 9.

2.
Create a range called list2 with the numbers 0 through 7.
'''

list1 = range(0, 9)
list2 = range(8)

'''
Range II
We can use range to generate more interesting lists.

By default, range creates a list starting at 0. However, if we call range with two arguments, we can create a list that starts at a different number. For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):

>>> my_list = range(2, 9)
>>> print(list(my_list))
[2, 3, 4, 5, 6, 7, 8]
With one or two arguments, range will create a list of consecutive numbers (i.e., each number is one greater than the previous number). If we use a third argument, we can create a list that “skips” numbers. For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:

>>> my_range2 = range(2, 9, 2)
>>> print(list(my_range2))
[2, 4, 6, 8]
We can skip as many numbers as we want! In this example, we’ll start at 1 and skip 10 between each number until we get to 100:

>>> my_range3 = range(1, 100, 10)
>>> print(list(my_range3))
[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
Our list stops at 91 because the next number in the sequence would be 101, which is greater than 100 (our stopping point).


'''
'''
.
Modify the range function that created list1 such that it:

Starts at 5
Has a difference of 3 between each item
Ends before 15
'''
list1 = range(5, 15, 3)
print(list(list1))
'''
Create a range object called list2 that:

Starts at 0
Has a difference of 5 between each item
Ends before 40
'''
list2 = range(0,40,5)
print(list(list2))

'''
Maria is entering customer data for her web design business. You’re going to help her organize her data.

Start by turning this list of customer first names into a list called first_names. Make sure to enter the names in this order:

Ainsley
Ben
Chani
Depak
'''
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']

'''
Create an empty list called age.
'''
age = []

'''
Depak’s age is 42. Use .append() to add 42 to age.

'''
age.append(42)

'''
Maria needs a list of the ages for all customers. Create a new list called all_ages that adds age with the following list, containing the ages for Ainsley, Ben, and Chani:

[32, 41, 29]
Make sure all_ages begins with the ages for Ainsley, Ben, and Chani and ends with Depak’s age (stored in age)!
'''

all_ages = [32, 41, 29] + age

'''
Create a new variable called name_and_age that combines first_names and all_ages using zip.
'''

name_and_age = zip(first_names,all_ages)

'''
Create a range object called ids with an id number for each customer. Since there are 4 customers, so id values should go from 0 to 3.
'''
ids = range(0,4)



