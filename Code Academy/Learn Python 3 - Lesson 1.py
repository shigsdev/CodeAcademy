my_name = "Codecademy"
print("Hello and welcome " + my_name + "!")
print("Hello World!")
#Computer programmers refer to blocks of text as strings. In our last exercise, we created the string “Hello world!”. In Python a string is either surrounded by double quotes ("Hello world") or single quotes ('Hello world'). It doesn’t matter which kind you use, just be consistent.


print("Scott Higgins")
print('Scott Higgins')

#LEARN PYTHON: SYNTAX
#Variables
#Programming languages offer a method of storing data for reuse. If there is a greeting we want to present, a date we need to reuse, or a user ID we need to remember we can create a variable which can store a value. In Python, we assign variables by using the equals sign (=).

message_string = "Hello there"
# Prints "Hello there"
print(message_string)
#In the above example, we store the message “Hello there” in a variable called message_string. Variables can’t have spaces or symbols in their names other than an underscore (_). They can’t begin with numbers but they can have numbers after the first letter (e.g., cool_variable_5 is OK).

#It’s no coincidence we call these creatures “variables”. If the context of a program changes, we can update a variable but perform the same logical process on it.

# Greeting
message_string = "Hello there"
print(message_string)

# Farewell
message_string = "Hasta la vista"
print(message_string)
#Above, we create the variable message_string, assign a welcome message, and print the greeting. After we greet the user, we want to wish them goodbye. We then update message_string to a departure message and print that out.

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "sandwich"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner

meal = 'pizza'
# Printing out dinner
print("Dinner:")
print(meal)

print("This message has mismatched quote marks!")
print('Abracadabra')

# Define the release and runtime integer variables below:
release_year = 2020
runtime = 2


# Define the rating_out_of_10 float variable below: 

rating_out_of_10 = 8.5

#Print out the result of this equation: 25 * 68 + 13 / 28

print(25*68+13/28)

coffee_price = 1.50
number_of_coffees = 4

# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# Updating the price 
coffee_price = 2.00

# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

#You’ve decided to get into quilting! To calculate the number of squares you’ll need for your first quilt let’s create two variables: quilt_width and quilt_length. Let’s make this first quilt 8 squares wide and 12 squares long.



quilt_width = 8 
quilt_length = 12

#Print out the number of squares you’ll need to create the quilt!

print(quilt_width * quilt_length)

#It turns out that quilt required a little more material than you have on hand! Let’s only make the quilt 8 squares long. How many squares will you need for this quilt instead?


quilt_length = 8

print(quilt_width * quilt_length)

#Python can also perform exponentiation. In written math, you might see an exponent as a superscript number, but typing superscript numbers isn’t always easy on modern keyboards. Since this operation is so related to multiplication, we use the notation **.



# 2 to the 10th power, or 1024
print(2 ** 10)

# 8 squared, or 64
print(8 ** 2)

# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)

# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)

# Calculation of squares for:
# 6x6 quilt
print(6 ** 2)

# 7x7 quilt
print(7**2)
# 8x8 quilt
print(8**2)
# How many squares for 6 people to have 6 quilts each that are 6x6?

# Calculation of squares for:
# 6x6 quilt
print(6 ** 2)

# 7x7 quilt
print(7**2)
# 8x8 quilt
print(8**2)
# How many squares for 6 people to have 6 quilts each that are 6x6?

print(6**4)

#Python offers a companion to the division operator called the modulo operator. The modulo operator is indicated by % and gives the remainder of a division calculation. If the number is divisible, then the result of the modulo operator will be 0.

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)

# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)

# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)

#You’re trying to divide a group into four teams. All of you count off, and you get number 27.

#Find out your team by computing 27 modulo 4. Save the value to my_team.

my_team = 27 % 4;

print(my_team)

#Food for thought: what number team are the two people next to you (26 and 28) on? What are the numbers for all 4 teams?

print(28 % 4)
print(26 % 4)
print(25 % 4)

#The + operator doesn’t just add two numbers, it can also “add” two strings! The process of combining two strings is called string concatenation. Performing string concatenation creates a brand new string comprised of the first string’s contents followed by the second string’s contents (without any added space in-between).

greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text

# Prints "Hey there!How are you doing?"
print(full_text)

#In this sample of code, we create two variables that hold strings and then concatenate them. But we notice that the result was missing a space between the two, let’s add the space in-between using the same concatenation operator!

full_text = greeting_text + " " + question_text

# Prints "Hey there! How are you doing?"
print(full_text)

#If you want to concatenate a string with a number you will need to make the number a string first, using the str() function. If you’re trying to print() a numeric variable you can use commas to pass it as a different argument rather than converting it to a string.

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"

# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2

# Prints "I am 10 years old today!"
print(full_birthday_string)

# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.

# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)

#Concatenate the strings and save the message they form in the variable message.

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:

message = string1 + string2 + string3 + string4 + string5 + string6
#print(message)

print(message)

#Python offers a shorthand for updating variables. When you have a number saved in a variable and want to add to the current value of the variable, you can use the += (plus-equals) operator.

# First we have a variable with a number saved
number_of_miles_hiked = 12

# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2

# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14

#Above, we keep a running count of the number of miles a person has gone hiking over time. Instead of recalculating from the start, we keep a grand total and update it when we’ve gone hiking further.

#The plus-equals operator also can be used for string concatenation, like so:

hike_caption = "What an amazing time to walk through nature!"

# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"

print(hike_caption)

#We’re doing a little bit of online shopping and find a pair of new sneakers. Right before we check out, we spot a nice sweater and some fun books we also want to purchase!



total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:

total_price += nice_sweater
total_price += fun_books

print("The total price is", total_price)

#Python strings are very flexible, but if we try to create a string that occupies multiple lines we find ourselves face-to-face with a SyntaxError. Python offers a solution: multi-line strings. By using three quote-marks (""" or ''') instead of one, we tell the program that the string doesn’t end until the next triple-quote. This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don’t close it prematurely.

leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""

# Assign the string here

to_you = """Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?"""


print(to_you)

#Create variables:

#my_age
#half_my_age
#greeting
#name
#greeting_with_name
#Assign values to each using your knowledge of division and concatenation!

my_age = 42
half_my_age = 42/2
greeting = "how you doing "
name = "higs"
greeting_with_name = greeting + name

print(greeting_with_name + " i am " + str(my_age))