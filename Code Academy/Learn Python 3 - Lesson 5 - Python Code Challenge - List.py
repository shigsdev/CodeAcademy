'''

This article will help you review Python functions by providing some code challenges involving lists.

Some of these challenges are difficult! Take some time to think about them before starting to code.

You might not get the solution correct on your first try — look at your output, try to find where you’re going wrong, and iterate on your solution.

Finally, if you get stuck, use our solution code! If you “Check Answer” twice with an incorrect solution, you should see an option to get our solution code. However, truly investigate that solution — experiment and play with the solution code until you have a good grasp of how it is working. Good luck!

Function Syntax
As a refresher, function syntax looks like this:

def some_function(some_input1, some_input2):
    # … do something with the inputs …
    return output
For example, a function that returns the sum of the first and last elements of a given list might look like this:

def first_plus_last(lst):
    return lst[0] + lst[-1]
And this would produce output like:

 first_plus_last([1, 2, 3, 4])
5
 first_plus_last([8, 2, 5, -8])
0
 first_plus_last([-10, 2, 3, -4])
-14
Challenges
We’ve included 5 list challenges below. Try to answer all of them and polish up your problem-solving skills and your list expertise

1. Append Sum
Write a function named append_sum that has one parameter — a list named named lst.

The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

'''


def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst


print(append_sum([1, 1, 2]))

'''
Larger List
Write a function named larger_list that has two parameters named lst1 and lst2.

The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.

'''


# Write your function here
def larger_list(lst1, lst2):
    if len(lst1) > len(lst2) or len(lst2) == len(lst1):
        return lst1[-1]
    elif (len(lst2) > len(lst1)):
        return lst2[-1]


# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

'''
3. More Than N
Create a function named more_than_n that has three parameters named lst, item, and n.

The function should return True if item appears in the list more than n times. The function should return False otherwise.
'''

def more_than_n(lst,item,n):
    if(lst.count(item) > n):
        return True
    else:
        return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

'''
Append Size
Create a function called append_size that has one parameter named lst.

The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.

For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.
'''

def append_size(lst):
    lst.append(len(lst))
    return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

'''
Combine Sort
Write a function named combine_sort that has two parameters named lst1 and lst2.

The function should combine these two lists into one new list and sort the result. Return the new sorted list.
'''

def combine_sort(lst1,lst2):
    return sorted(lst1+lst2)

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
