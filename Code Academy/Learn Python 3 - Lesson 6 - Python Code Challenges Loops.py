"""
his lesson will help you review Python loops by providing some challenge exercises involving loops.

Some of these challenges are difficult! Take some time to think about them before starting to code.

You might not get the solution correct on your first try — look at your output, try to find where you’re going wrong,
and iterate on your solution.

Finally, if you get stuck, use our solution code! If you “Check Answer” twice with an incorrect solution, you should
see an option to get our solution code. However, truly investigate that solution — experiment and play with the
solution code until you have a good grasp of how it is working. Good luck!

Function and Loop Syntax
As a refresher, function syntax looks like this:

def some_function(some_input1, some_input2):
  … do something with the inputs …
  return output
For example, a function that prints all odd numbers in a list would look like this:

def odd_nums(lst):
  for item in lst:
    if item % 2 == 1:
      print(item)
And this would produce output like:

#>>> odd_nums([4, 7, 9, 10, 13]) 7 9 13 Challenges We’ve included 5 challenges below. Try to answer all of them and
polish up your problem-solving skills and your loop expertise.
"""


# Divisible By Ten Let’s start our code challenges with a function that counts how many numbers are divisible by ten
# from a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check
# each of the numbers in the list. Every time a number is divisible by 10, a counter will be incremented and the final
# count will be returned. These are the steps we need to complete this:

# Define the function to accept one input parameter called nums
# Initialize a counter to 0
# Loop through every number in nums
# Within the loop, if any of the numbers are divisible by 10, increment our counter
# Return the final counter value

def divisible_by_ten(nums):
    counter = 0
    for num in nums:
        if num % 10 == 0:
            counter += 1
    return counter


print(divisible_by_ten([20, 25, 30, 35, 40]))


# 2. Greetings You are invited to a social gathering, but you are tired of greeting everyone there. Luckily we can
# create a function to accomplish this task for us. In this challenge, we will take a list of names and prepend the
# string 'Hello, ' before each name. This will require a few steps:
#
# Define the function to accept a list of strings as a single parameter called names Create a new list of strings
# Loop through each name in names Within the loop, concatenate 'Hello, ' and the current name together and append
# this new string to the new list of strings Afterwards, return the new list of strings Create a function named
# add_greetings() which takes a list of strings named names as a parameter.
#
# In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each
# name in names and append the greeting to the list.
#
# Return the new list containing the greetings.

# Create a function named add_greetings() which takes a list of strings named names as a parameter.
#
# In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each
# name in names and append the greeting to the list.
#
# Return the new list containing the greetings.


# Write your function here
def add_greetings(names):
    lst = []
    for name in names:
        lst.append('Hello, ' + name)
    return lst


# Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

# 3. Delete Starting Even Numbers Let’s try a tricky challenge involving removing elements from a list. This function
# will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. It will
# accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning
# of the list are removed. To do this, we will need the following steps:
#
# Define our function to accept a single input parameter lst which is a list of numbers
# Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
# Within the loop, if the first number in the list is even, then remove the first number of the list
# Once we hit an odd number or we run out of numbers, return the modified list
# Write a function called delete_starting_evens() that has a parameter named lst.
#
# The function should remove elements from the front of lst until the front of the list is not even. The function
# should then return lst.
#
# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
#
# Make sure your function works even if every element in the list is even!

# Write your function here
'''
def delete_starting_evens(lst):
    for item in lst:
        if item % 2 == 0:
            #lst.pop(0)
            del lst[0]
    if lst[0] % 2 == 0:
        return []
    else:
        return lst
'''
'''
def delete_starting_evens(lst):
    while len(lst) >= 1 and lst[0] % 2 == 0:
        lst = lst[1:]
    return lst
'''


def delete_starting_evens(lst):
    for x in range(len(lst) - 1):
        if lst[0] % 2 == 0:
            lst = lst[1:]
    # return lst
    if lst[0] % 2 == 0:
        return []
    else:
        return lst


# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

'''
This is the way we solved it:
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst
def delete_starting_evens(lst): while (len(lst) > 0 and lst[0] % 2 == 0): lst = lst[1:] return lst After defining our 
method, we use a while loop to keep iterating as long as some provided conditions are true. We provide two conditions 
for the while loop to continue. We will keep iterating as long as there is at least one number left in the list len(
lst) > 0 and if the first element in the list is even lst[0] % 2 == 0. If both of these conditions are true, 
then we replace the list with every element except for the first one using lst[1:]. Once the list is empty or we hit 
an odd number, the while loop terminates and we return the modified list. 

'''

#4. Odd Indices This next function will give us the values from a list at every odd index. We will need to accept a
#list of numbers as an input parameter and loop through the odd indices instead of the elements. Here are the steps
#needed:

#Define the function header to accept one input which will be our list of numbers
#Create a new list which will hold our values to return
#Iterate through every odd index until the end of the list
#Within the loop, get the element at the current odd index and append it to our new list
#Return the list of elements which we got from the odd indices.
#Create a function named odd_indices() that has one parameter named lst.

#The function should create a new empty list and add every element from lst that has an odd index. The function should
#then return this new list.

#For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].


# Write your function here
def odd_indices(lst):
    new_list = []
    for x in range(len(lst)):
        print("postion " + str(x) + " has value: ", str(lst[x]))
        if x % 2 == 1:
            new_list.append(lst[x])
    return new_list

# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

''' 
Here is this solution:

def odd_indices(lst): new_lst = [] for index in range(1, len(lst), 2): new_lst.append(lst[index]) return new_lst In 
our solution, we iterate through a range of values. The function range(1, len(lst), 2) returns a list of numbers 
starting at 1, ending at the length of len, and incrementing by 2. This causes the loop to iterate through every odd 
number until the last index of our list of numbers. Using this, we can simply append the element at whatever index we 
are at since we know that using our range we will be iterating through only odd indices. 

Another way to do this would be to iterate through all indices and use an if statement to see if the index you’re 
currently looking at is odd. 

'''

# 5. Exponents In this challenge, we will be using nested loops in order to raise a list of number to the power of a
# list of other numbers. What this means is that for every number in the first list, we will raise that number to the
# power of every number in the second list. If you provide the first list with 2 elements and the second list with 3
# numbers, then there will be 6 final answers. Let’s look at the steps we need:
#
# Define the function to accept two lists of numbers, bases and powers
# Create a new list that will contain our answers
# Create a loop that iterates through every base in bases
# Within that loop, create another loop that iterates through every power in power
# Within that nested loop, append the result of the current base raised to the current power.
# After all iterations of both loops are complete, return the list of answers

def exponents(bases,powers):
    lst = []
    for base in bases:
        for power in powers:
            lst.append(base**power)
    return lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))