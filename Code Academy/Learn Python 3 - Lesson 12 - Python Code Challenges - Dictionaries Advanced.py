"""
Python Code Challenges: Dictionaries (Advanced)
Difficult Python Code Challenges Involving Dictionaries

This article will help you review Python functions by providing some code challenges involving dictionaries.

Some of these challenges are difficult! Take some time to think about them before starting to code.

You might not get the solution correct on your first try — look at your output, try to find where you’re going wrong,
and iterate on your solution.

Finally, if you get stuck, use our solution code! If you “Check Answer” twice with an incorrect solution, you should
see an option to get our solution code. However, truly investigate that solution — experiment and play with the
solution code until you have a good grasp of how it is working. Good luck!
Function Syntax
def some_function(some_input1, some_input2):
  … do something with the inputs …
  return output
For example, a function that counts the number of values in a dictionary that are above a given number would look like this:

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
"""


'''1. Word Length Dict Let’s start by writing a function that creates a new dictionary based on a list of strings. 
The keys of our dictionary will be every string in our list of strings, while the values will be the length of each 
of the words in the string list. Here are the steps: 

Define the function to accept one parameter for our list of strings
Create a new empty dictionary
Loop through every string in the list of strings
Inside the loop, add the string as a key and the length of the string as the value to the dictionary
After the loop, return the new dictionary
'''

# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. The function
# should return a dictionary of key/value pairs where every key is a word in words and every value is the length of
# that word.
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths
# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# To create a new dictionary we set a variable equal to {}. While iterating through each string in our string list,
# we can add the key and value to our dictionary using this syntax: word_lengths[word] = len(word).

'''2. Frequency Count This next function is similar, but instead of counting the length of each string in the list of 
strings, we will be counting the frequency of each string. This function will also accept a list of strings as input 
and return a new dictionary. Here is what we need to do: 

Define the function to accept one parameter for our list of strings Create a new empty dictionary Loop through every 
string in the list of strings Inside the loop, if the string is not already in our dictionary, store the string as a 
key with a value of 0 in our dictionary. Then, increment the value by 1. After the loop, return the new dictionary 

'''