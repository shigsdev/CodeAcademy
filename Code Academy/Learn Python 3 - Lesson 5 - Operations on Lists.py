'''
WORKING WITH LISTS IN PYTHON
Operations on Lists
Now that we know how to create a list, we can start working with existing lists of data.

In this lesson, you’ll learn how to:

Get the length of a list
Select subsets of a list (called slicing)
Count the number of times that an element appears in a list
Sort a list of items


'''

'''

Length of a List
Often, we’ll need to find the number of items in a list, usually called its length.

We can do this using the function len. When we apply len to a list, we get the number of elements in that list:

my_list = [1, 2, 3, 4, 5]
print(len(my_list))
This would yield:

5
'''
list1 = range(2, 20, 2)
# Calculate the length of list1 and save it to the variable list1_len.

list1_len = len(list1)

print(list1_len)

list2 = range(2, 20, 3)
print(len(list2))

'''
Selecting List Elements I
Chris is interviewing candidates for a job. He will call each candidate in order, represented by a Python list:

calls = ['Ali', 'Bob', 'Cam', 'Doug', 'Ellie']
First, he’ll call 'Ali', then 'Bob', etc.

In Python, we call the order of an element in a list its index.

Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.

Here are the index numbers for that list:
In this example, the element with index 2 is 'Cam'.

We can select a single element from a list by using square brackets ([]) and the index of the list item. For example, if we wanted to select the third element from the list, we’d use calls[2]:

>>> print(calls[2])
'Cam'
'''

# Use square brackets ([ and ]) to select the element with index 4 from the list employees. Save it to the variable index4.

employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

index4 = employees[4]
print(len(employees))

print(employees[6])

'''
Selecting List Elements II
What if we want to select the last element of a list?

We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.

Consider the following list with 5 elements:

list1 = ['a', 'b', 'c', 'd', 'e']
If we select the -1 element, we get the final element, 'e':

>>> print(list1[-1])
'e'
This is the same as selecting the element with index 4:

>>> print(list1[4])
'e'
'''
# Use print and len to display the length of shopping_list.

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']

print(len(shopping_list))

# Get the last element of shopping_list using the -1 index. Save this element to the variable last_element.

last_element = shopping_list[-1]
# Now select the element with index 5 and save it to the variable element5.

element5 = shopping_list[5]
# Use print to display both element5 and last_element.

print(last_element, element5)

'''
Slicing Lists
Suppose we have a list of letters:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
Suppose we want to select from b through f.

We can do this using the following syntax: letters[start:end], where:

start is the index of the first element that we want to include in our selection. In this case, we want to start at b, which has index 1.
end is the index of one more than the last index that we want to include. The last element we want is f, which has index 5, so end needs to be 6.
sublist = letters[1:6]
print(sublist)
This example would yield:
['b', 'c', 'd', 'e', 'f']
Notice that the element at index 6 (which is g) is not included in our selection.
'''

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]

'''
Use print to examine the variable beginning.

How many elements does it contain?
'''
print(beginning)

middle = suitcase[2:4]

print(middle)

'''
Slicing Lists II
If we want to select the first 3 elements of a list, we could use the following code:

>>> fruits = ['apple', 'banana', 'cherry', 'date']
>>> print(fruits[0:3])
['apple', 'banana', 'cherry']
When starting at the beginning of the list, it is also valid to omit the 0:

>>> print(fruits[:3])
['apple', 'banana', 'cherry']
We can do something similar when selecting the last few items of a list:

>>> print(fruits[2:])
['cherry' , 'date']
We can omit the final index when selecting the final elements from a list.

If we want to select the last 3 elements of fruits, we can also use this syntax:

>>> print(fruits[-3:])
['banana', 'cherry', 'date']
We can use negative indexes to count backward from the last element.

'''

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

# Create a new list called start containing the first 3 elements of suitcase.

start = suitcase[:3]
print(start)
# Create a new list called end containing the final two elements of suitcase.


end = suitcase[-2:]
print(end)

'''
Counting elements in a list
Suppose we have a list called letters that represents the letters in the word “Mississippi”:

letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
If we want to know how many times i appears in this word, we can use the function count:

num_i = letters.count('i')
print(num_i)
This would print out:

4

'''

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake',
         'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

'''
Mrs. WIlson’s class is voting for class president. She has saved each student’s vote into the list votes.

Use count to determine how many students voted for 'Jake'. Save your answer as jake_votes.
'''

jake_votes = votes.count('Jake')
print(jake_votes)

'''
Sometimes, we want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.

We can sort a list in place using .sort(). Suppose that we have a list of names:

names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
print(names)
This would print:

['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
Now we apply .sort():

names.sort()
print(names)
And we get:

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
Notice that sort goes after our list, names. If we try sort(names), we will get a NameError.

sort does not return anything. So, if we try to assign names.sort() to a variable, our new variable would be None:

sorted_names = names.sort()
print(sorted_names)
This prints:

None
Although sorted_names is None, the line sorted_names = names.sort() still edited names:

>>> print(names)
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

'''

### Exercise 1 & 2 ###
# Use sort to sort addresses.
# Use print to see how addresses changed.

addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace',
             '1600 Pennsylvania Ave', '10 Downing St.']

addresses.sort()
print(addresses)
# Sort addresses here:

### Exercise 3 ###
# Remove the # in front of the line sort(names). Edit this line so that it runs without producing a NameError.

names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort(reverse=True)
print(names)
### Exercise 4 ###
# Use print to examine sorted_cities. Why is it not the sorted version of cities?
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort(reverse=True)
print(sorted_cities)

'''
Sorting Lists II
A second way of sorting a list is to use sorted. sorted is different from .sort() in several ways:

It comes before a list, instead of after.
It generates a new list.
Let’s return to our list of names:

names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
Using sorted, we can create a new list, called sorted_names:

sorted_names = sorted(names)
print(sorted_names)
This yields the list sorted alphabetically:

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
Note that using sorted did not change names:

>>> print(names)
['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
'''

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

# Use sorted to order games and create a new list called games_sorted.

games_sorted = sorted(games)

# Use print to inspect games and games_sorted. How are they different?
print(games)
print(games_sorted)

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table',
             'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow',
             'pillow']
print(inventory)
'''
inventory is a list of items that are in the warehouse for Bob’s Furniture. How many items are in the warehouse?

Save your answer to inventory_len.
'''

inventory_len = len(inventory)
print(inventory_len)

# Select the first element in inventory. Save it to the variable first.

first = inventory[0]
print(first)

last = inventory[-1]
print(last)

# Select items from the inventory starting at index 2 and up to, but not including, index 6.

# Save your answer to inventory_2_6.

inventory_2_6 = inventory[2:6]
print(inventory_2_6)

# Select the first 3 items of inventory and save it to the variable first_3.
first_3 = inventory[:3]
print(first_3)

# How many 'twin bed's are in inventory? Save your answer to twin_beds.
twin_beds = inventory.count("twin bed")
print(twin_beds)

# Sort inventory using .sort().
inventory.sort()
print(inventory)
