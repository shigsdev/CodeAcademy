"""

Introduction
This lesson will help you review Python functions by providing some challenge exercises involving Strings.

As a refresher, function syntax looks like this:

def some_function(some_input1, some_input2):
  … do something with the inputs …
  return output
For example, a function that finds the difference in length between two Strings would look like this:

def lengthDiff(str1, str2):
  return len(str1) - len(str2)
And this would produce output like:

#>>> lengthDiff("Python", "rocks")
1
#>>> lengthDiff("Marco", "Polo")
1
#>>> lengthDiff("Kevin", "Durant")
-1
When you’re ready to do this series of short function challenges, continue on to the rest of the lesson!

"""

# Write a function called unique_english_letters that takes the string word as a parameter. The function should
# return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as
# different letters.
#
# We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to
# include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
"""
def unique_english_letters(words):
    counter = 0
    unique_list = []
    for w in words:
        if unique_list.count(w.lower) == 0:
            counter += 1
            unique_list.append(w.lower)
    return counter
"""


def unique_english_letters(words):
    counter = 0

    for l in letters:
        if l in words:
            counter += 1
    return counter


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))


# should print 4


# Write a function named count_char_x that takes a string named word and a single character named x as parameters.
# The function should return the number of times x appears in word.

# Write your count_char_x function here:

def count_char_x(word, x):
    counter = 0
    for w in word:
        if w == x:
            counter += 1
    return counter


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))


# should print 1

# Write a function named count_multi_char_x that takes a string named word and a string named x. This function should
# do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in
# word. However, this time, make sure your function works when x is multiple characters long.
#
# For example, count_multi_char_x("Mississippi", "iss") should return 2

# Write your count_multi_char_x function here:
# def count_multi_char_x(word,x):
#    return word.count(x)

def count_multi_char_x(word, x):
    # temp_list = []
    # print(len(word.split(x)))
    # temp_list.append(word.split(x))
    print(word.split(x))
    return len(word.split(x)) - 1


print("##############Count Multi X##################")
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print

# Write a function named substring_between_letters that takes a string named word, a single character named start,
# and another character named end. This function should return the substring between the first occurrence of start
# and end in word. If start or end are not in word, the function should return word.
#
# For example, substring_between_letters("apple", "p", "e") should return "pl".

print("##############Substring Between##################")

'''
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
  	return(word[start_ind+1:end_ind])
  return word
'''


def substring_between_letters(word, start, end):
    if word.find(start) == -1 or word.find(end) == -1:
        print("Error")
        return word
    elif start in word and end in word:
        starting_index = word.index(start)
        ending_index = word.index(end)
        return word[starting_index + 1:ending_index]


# Write your substring_between_letters function here:

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

print("##############X Length##################")


# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters.
# This function should return True if every word in sentence has a length greater than or equal to x.


# Write your x_length_words function here:
def x_length_words(sentence, x):
    words = sentence.split(" ")
    for word in words:
        if len(word) < x:
            return False
    return True


'''
# Write your x_length_words function here:
def x_length_words(sentence,x):
    counter = 0
    for item in sentence.split(" "):
        if len(item) >= x:
            counter += 1
    if counter == len(sentence.split(" ")):
        return True
    else:
        return False

'''
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

print("##############Check Name##################")

# Write a function called check_for_name that takes two strings as parameters named sentence and name. The function
# should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of
# uppercase and lowercase letters. The function should return False otherwise.
#
# For example, the following three calls should all return True:
#
# check_for_name("My name is Jamie", "Jamie")
# check_for_name("My name is jamie", "Jamie")
# check_for_name("My name is JAMIE", "Jamie")
"""
# Write your check_for_name function here:
def check_for_name(sentence, name):
    return name.lower() in sentence.lower()
"""


# Write your check_for_name function here:
def check_for_name(sentence, name):
    if name.lower() in sentence.lower():
        return True
    else:
        return False


# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

print("############## Every Other Letter ##################")

# Create a function named every_other_letter that takes a string named word as a parameter. The function should
# return a string containing every other letter in word.

"""
# Write your every_other_letter function here:
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other
"""


# Write your every_other_letter function here:
def every_other_letter(word):
    temp_string = ""
    for w in range(len(word) - 1):
        if w % 2 == 0:
            temp_string += word[w]
    return temp_string


# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print


print("############## Reverse ##################")


# Write a function named reverse_string that has a string named word as a parameter. The function should return word
# in reverse.


# Write your reverse_string function here:
# def reverse_string(word):
#    return word[::-1]

def reverse_string(word):
    temp_string = ""
    for w in range(len(word) - 1, -1, -1):
        temp_string += word[w]
    return temp_string


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

print("############## Make Spoonerism ##################")


# A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is
# made when someone says “Belly Jeans” instead of “Jelly Beans”.
#
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the
# first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each
# word. Return the two new words as a single string separated by a space.

'''
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    if len(word1) == 1 and len(word2) == 1:
        return word2 + " " + word1
    elif len(word1) == 1 and len(word2) > 1:
        return word2[0] + " " + word1[0] + word2[1:]
    elif len(word1) > 1 and len(word2) == 1:
        return word2[0] + word1[1:] + " " + word1[0]
    else:
        return word2[0] + word1[1:] + " " + word1[0] + word2[1:]
'''
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

print("############## Add Excalmation ##################")

# Create a function named add_exclamation that has one parameter named word. This function should add exclamation
# points to the end of word until word is 20 characters long. If word is already at least 20 characters long,
# just return word.

'''
# Write your add_exclamation function here:
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

'''

# Write your add_exclamation function here:
def add_exclamation(word):
    if len(word) >= 20:
        return word
    else:
        for w in range(20-len(word)):
            word += "!"
        return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
