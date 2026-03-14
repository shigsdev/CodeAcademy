'''
So far, we’ve covered how to assign variables values directly in a Python file. However, we often want a user of a program to enter new information into the program.

How can we do this? As it turns out, another way to assign a value to a variable is through user input.

While we output a variable’s value using print(), we assign information to a variable using input(). The input() function requires a prompt message, which it will print out for the user before they enter the new information. For example:
'''
likes_snakes = input("Do you like snakes? ")
print(likes_snakes)
'''In the example above, the following would occur:

The program would print “Do you like snakes? “ for the user.
The user would enter an answer (e.g., “Yes! I have seven pythons as pets!”).
The variable likes_snakes would be assigned a value of the user’s answer (in this case, “Yes! I have seven pythons as pets!”).
Try constructing a statement to collect user input on your own!

'''

#Fill in the blanks in the code to complete a statement that asks a user “What is your favorite flightless bird?” and then stores their answer in the variable favorite_flightless_bird.

favorite_flightless_bird = input("what is your favorite flighless bird?")
print(favorite_flightless_bird)

#Not only can input() be used for collecting all sorts of different information from a user, but once you have that information stored as a variable you can use it to simulate interaction:

favorite_fruit = input("What is your favorite fruit? ")
print("Oh cool! I like " + favorite_fruit + " too, but I think my favorite fruit is apple.")
