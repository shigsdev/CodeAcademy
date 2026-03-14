'''
This lesson will help you review Python functions by providing some challenge exercises involving loops.

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

#>>> odd_nums([4, 7, 9, 10, 13])
7
9
13
When you’re ready to do this series of short function challenges, continue on to the rest of the lesson!
'''

'''
Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

Return the count of how many numbers in the list are divisible by 10.
'''


def divisible_by_ten(nums):
    count = 0
    for x in nums:
        if x % 10 == 0:
            count += 1
    return count


print(divisible_by_ten([20, 25, 30, 35, 40]))

'''
Create a function named add_greetings() which takes a list of strings named names as a parameter.

In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.

Return the new list containing the greetings.
'''


# Write your function here
def add_greetings(names):
    greeting = []
    for name in names:
        greeting.append("Hello " + name)
    return greeting


# Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

'''
Write a function called delete_starting_evens() that has a parameter named lst.

The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!
'''


# Write your function here
def delete_starting_evens(lst):
    x = 0
    while len(lst) > 0 and lst[x] % 2 == 0:
        lst.pop(x)
    return lst


# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

'''
Create a function named odd_indices() that has one parameter named lst.

The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

'''


def odd_indices(lst):
    new_lst = []
    new_lst = [x for x in lst if lst.index(x) % 2 == 1]
    return new_lst


print(odd_indices([4, 3, 7, 10, 11, -2]))

'''
Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

For example, consider the following code.

exponents([2, 3, 4], [1, 2, 3])
the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.

'''


# Write your function here
def exponents(lst1, lst2):
    new_list = []
    for x in lst1:
        for y in lst2:
            new_list.append(x ** y)
    return new_list


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

'''
Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.
'''


def larger_sum(lst1, lst2):
    if (sum(lst1) >= sum(lst2)):
        return lst1
    else:
        return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))

'''
Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.
'''


def over_nine_thousand(lst):
    if sum(lst) == 0:
        return 0
    element_sum = 0
    for element in lst:
        element_sum += element
        if element_sum > 9000:
            break
    return element_sum


print(over_nine_thousand([8000, 900, 120, 5000]))

'''
Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums
'''


# Write your function here
def max_num(lst):
    number = lst[0]
    for numbers in lst:
        if numbers > number:
            number = numbers
    return number


# Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
print(max_num([-50, -20]))

'''
Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

'''


def same_values(lst1, lst2):
    new_lst = []
    if len(lst1) != len(lst2):
        print("Error - lists are not the same size")
        return new_lst
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            new_lst.append(int(index))
    return new_lst


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

'''
Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.


'''


def reversed_list(lst1, lst2):
    #return_value = True
    for index in range(len(lst1)):
        if lst1[index] != lst2[(len(lst2) - index - 1)]:
            #print("equal at index " + str(index))
            return False
            #break
    return True


# Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))l
print(reversed_list([1, 5, 3], [3, 2, 1]))
