'''
Python Code Challenges: Dictionaries
Python Code Challenges Involving Dictionaries

This article will help you review Python functions by providing some code challenges involving dictionaries.

Some of these challenges are difficult! Take some time to think about them before starting to code.

You might not get the solution correct on your first try — look at your output, try to find where you’re going wrong,
and iterate on your solution.

Finally, if you get stuck, use our solution code! If you “Check Answer” twice with an incorrect solution, you should
see an option to get our solution code. However, truly investigate that solution — experiment and play with the
solution code until you have a good grasp of how it is working. Good luck!

Function Syntax def some_function(some_input1, some_input2): … do something with the inputs … return output For
example, a function that counts the number of values in a dictionary that are above a given number would look like
this:

def greater_than_ten(my_dictionary, number):
  count = 0
  for value in my_dictionary.values():
    if value > number:
      count += 1
  return count
And this would produce output like:

>>> greater_than_ten({"a":1, "b":2, "c":3}, 0)
3
>>> greater_than_ten({"a":1, "b":2, "c":3}, 5)
0
'''

'''1. Sum Values For the first code challenge, we are going to look at only the values in a dictionary. This function 
should sum up all of the values from the key-value pairs in the dictionary. Here are the steps we need: 

Define the function to accept one parameter for our dictionary 
Create a variable to keep track of our sum 
Loop 
through every value in the dictionary 
Inside the loop, add each value to the sum 
Return the sum 

Code Challenge Write 
a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return 
the sum of the values of the dictionary 

'''


# Write your sum_values function here:
def sum_values(my_dictionary):
    total = 0
    for value in my_dictionary.values():
        total += value
    return total


# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6

'''2. Even Keys Next, we are going to do something similar, but we are going to use the keys in order to retrieve the 
values. Additionally, we are going to only look at every even key within the dictionary. Here are the steps: 

Define the function to accept one parameter for our dictionary
Create a variable to keep track of our sum
Loop through every key in the dictionary
Inside the loop, if the key is even, add the value from the even key
After the loop, return the sum

Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, 
as a parameter. This function should return the sum of the values of all even keys. '''


# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
    total = 0
    for key in my_dictionary.keys():
        if key % 2 == 0:
            total += my_dictionary[key]
    return total


# Uncomment these function calls to test your  function:
print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6

'''3. Add Ten Let’s loop through the keys again, but this time let’s modify the values within the dictionary. Our 
function should add 10 to every value in the dictionary and return the modified dictionary. Here is what we need to do: 

Define the function to accept one parameter for our dictionary
Loop through every key in the dictionary
Retrieve the value using the key and add 10 to it. Make sure to re-save the new value to the original key.
After the loop, return the modified dictionary

Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The 
function should add 10 to every value in my_dictionary and return my_dictionary 

Here is how we did it:

def add_ten(my_dictionary): for key in my_dictionary.keys(): my_dictionary[key] += 10 return my_dictionary We use a 
for loop to iterate through each key and we access the value using the key. After accessing it, we overwrite the 
value with the value plus 10. Finally, we return the modified dictionary. '''


# Write your add_ten function here:
def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] += 10
    return my_dictionary


# Uncomment these function calls to test your  function:
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}

'''4. Values That Are Keys We are making a program that will create a family tree. Using a dictionary, we want to 
return a list of all the children who are also parents of other children. Using dictionaries we can consider those 
people to be values which are also keys in our dictionary of family data. Here is what we need to do: 

Define the function to accept one parameter for our dictionary Create an empty list to hold the values we find Loop 
through every value in the dictionary Inside the loop, test if the current value is a key in the dictionary. If it is 
then append it to the list of values we found After the loop, return the list of values which are also keys 

'''


# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This
# function should return a list of all values in the dictionary that are also keys.

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
    value_keys = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            value_keys.append(value)
    return value_keys


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]

# For this solution, we iterate through every value within the dictionary. In order to check if it is also a key,
# we can use the in keyword. This checks the value against all of the keys in the dictionary to see if it exists as a
# key as well. If it does, then we append it to our list of values which are also keys.


'''5. Largest Value For the last challenge, we are going to create a function that is able to find the maximum value 
in the dictionary and return the associated key. This is a twist on the max algorithm since it is using a dictionary 
rather than a list. These are the steps: 

Define the function to accept one parameter for our dictionary Initialize the starting key to a very low number 
Initialize the starting value to a very low number Iterate through the dictionary’s key/value pairs. Inside the loop, 
if the current value is larger than the current largest value, replace the largest key and largest value with the 
current ones you are looking at Once you are done iterating through all key/value pairs, return the key which has the 
largest value '''

# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should
# return the key associated with the largest value in the dictionary.

# Write your max_key function here:
def max_key(my_dictionary):
    largest_key = float("-inf")
    largest_value = float("-inf")
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# In order to program the max algorithm using dictionaries, we need to keep track of the max value and the key which
# is used to access it. We start by using float("-inf") in order to initialize them to the lowest possible value. To
# retrieve the key and value at the same time, we use the items() function. Inside our loop, we overwrite the current
# largest value and the key used to access whenever we find a larger value. We return the largest value’s key once we
# have iterated through the entire dictionary.

''' 

2. Frequency Count This next function is similar, but instead of counting the length of each string in the list of 
strings, we will be counting the frequency of each string. This function will also accept a list of strings as input 
and return a new dictionary. Here is what we need to do: 

Define the function to accept one parameter for our list of strings Create a new empty dictionary Loop through every 
string in the list of strings Inside the loop, if the string is not already in our dictionary, store the string as a 
key with a value of 0 in our dictionary. Then, increment the value by 1. After the loop, return the new dictionary '''

# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function
# should return a dictionary containing the frequency of each element in words.

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
    freqs = {}
    for word in words:
        if word not in freqs:
            freqs[word] = 0
        freqs[word] += 1
    return freqs
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# To create a new dictionary we set a variable equal to {}. We iterate through each of the strings in the list of
# strings and check if it is already in our dictionary using the in keyword. If it is not then we add it as a new
# key-value pair where the value is 0. Regardless of whether the string was already in the dictionary, increase the
# value by 1. This will make it so all new entries will have a value of 1 and all existing entries will increase
# their old value by 1.

'''3. Unique Values Now let’s try reading a dictionary as input and finding how many values are unique. The function 
should return a number which is the count of all values from the dictionary without including duplicates. These are 
the steps: 

Define the function to accept one parameter for our dictionary
Create a new empty list
Loop through every value in our dictionary
Inside the loop, if the value is not already in our list, append the value to our list
After the loop, return the length of our list

'''

# Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function
# should return the number of unique values in the dictionary.

# Write your unique_values function here:
def unique_values(my_dictionary):
    seen_values = []
    for value in my_dictionary.values():
        if value not in seen_values:
            seen_values.append(value)
    return len(seen_values)
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# This function has a similar structure to the last one except that the input has been changed to a dictionary. We
# iterate through each of the values and whenever we find one we have not added to our list already, we add it to the
# list. After the loop, we return the length of the list since that contains all unique values from the dictionary.


'''4. Count First Letter This function accepts a dictionary where the keys are last names and the values are lists of 
first names of people who have that last name. We need to calculate the number of people who have the same first 
letter in their last name. Here are the steps we need: 

Define the function to accept one parameter for our dictionary Create a new empty dictionary called letters Loop 
through every key in our names dictionary Inside the loop, get the first letter of the last name we are looking at. 
If the first letter is not in our letter dictionary, add it as a key with a value of 0. Then, increment that key by 
the number of people that have that last name After the loop, return the letters dictionary Code Challenge 

'''

# Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a
# dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might
# look like this:
#
# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]} The
# function should return a new dictionary where each key is the first letter of a last name, and the value is the
# number of people whose last name begins with that letter.
#
# So in example above, the function would return:
#
# {"S" : 4, "L": 3}

# This function uses two dictionaries instead of one dictionary and one list. We iterate through each of the keys (
# which are the last names) and store the first letter of the last name in first_letter. We then use similar logic to
# what we have used before by testing if we have already seen that letter before. If we haven’t seen that letter
# before, then we add it to our dictionary with a value of 0. Next, we are going to increment the value. Since we
# know that some people share the last name (as seen by the list of first names in our names dictionary),
# we are going to increment the value in our letters dictionary by the length of first names that share the last name
# for our current iteration (key).

