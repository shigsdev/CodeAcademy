'''
CONTROL FLOW
Control Flow: An Introduction
Imagine waking up in the morning.

You wake up and think,

“Ugh, is it a weekday?”

If so, you have to get up and get dressed and get ready for work or school. If not, you can sleep in a bit longer and catch a couple extra Z’s. But alas, it is a weekday, so you are up and dressed and you go to look outside, “What’s the weather like? Do I need an umbrella?”

These questions and decisions control the flow of your morning, each step and result is a product of the conditions of the day and your surroundings. Your computer, just like you, goes through a similar flow every time it executes code. A program will run (wake up) and start moving through its checklists, is this condition met, is that condition met, okay let’s execute this code and return that value.

This is the Control Flow of your program. In Python, your script will execute from the top down, until there is nothing left to run. It is your job to include gateways, known as conditional statements, to tell the computer when it should execute certain blocks of code. If these conditions are met, then run this function.

Over the course of this lesson, you will learn how to build conditional statements using boolean expressions, and manage the control flow in your code.

'''

'''
Boolean Expressions
In order to build control flow into our program, we want to be able to check if something is true or not. A boolean expression is a statement that can either be True or False.

Let’s go back to the ‘waking up’ example. The first question, “Is today a weekday?” can be written as a boolean expression:

Today is a weekday.
This expression can be True if today is Tuesday, or it can be False if today is Saturday. There are no other options.

Consider the phrase:

Friday is the best day of the week.
Is this a boolean expression?

No, this statement is an opinion and is not objectively True or False. Someone else might say that “Wednesday is the best weekday,” and their statement would be no less True or False than the one above.

How about the phrase:

Sunday starts with the letter 'C'.
Is this a boolean expression?

Yes! This expression can only be True or False, which makes it a boolean expression. Even though the statement itself is false (Sunday starts with the letter ‘C’), it is still a boolean expression.

Instructions
1.
Determine if the following statements are boolean expressions or not. If they are, set the matching variable to the right to "Yes" and if not set the variable to "No". Here’s an example of what to do:

Example statement:

My dog is the cutest dog in the world.
This is an opinion and not a boolean expression, so you would set example_statement to "No" in the editor to the right. Okay, now it’s your turn:

Statement one:

Dogs are mammals.
Statement two:

My dog is named Pavel.
Statement three:

Dogs make the best pets.
Statement four:

Cats are female dogs.
'''

'''
elational Operators: Equals and Not Equals
Now that we understand what boolean expressions are, let’s learn to create them in Python. We can create a boolean expression by using relational operators.

Relational operators compare two items and return either True or False. For this reason, you will sometimes hear them called comparators.

The two boolean operators we’ll cover first are:

Equals: ==
Not equals: !=
These operators compare two items and return True or False if they are equal or not.

We can create boolean expressions by comparing two values using these operators:

>>> 1 == 1
True
>>> 2 != 4
True
>>> 3 == 5
False
>>> '7' == 7
False
Each of these is an example of a boolean expression. >>> is the prompt when you run Python in your terminal, which you can then use to evaluate simple expressions, such as these.

Why is the last statement false? The '' marks in '7' make it a string, which is different from the integer value 7, so they are not equal. When using relational operators it is important to always be mindful of type.

'''

'''
CONTROL FLOW
Boolean Variables
Before we go any further, let’s talk a little bit about True and False. You may notice that when you type them in the code editor (with uppercase T and F), they appear in a different color than variables or strings. This is because True and False are their own special type: bool.

True and False are the only bool types, and any variable that is assigned one of these values is called a boolean variable. Boolean variables can be created in several ways. The easiest way is to simply assign True or False to a variable:
'''
set_to_true = True
set_to_false = False

# You can also set a variable equal to a boolean expression.

bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

'''
These variables now contain boolean values, so when you reference them they will only return the True or False values of the expression they were assigned.

>>>bool_three
True
>>>bool_four
False
>>>bool_five
True
'''

# Create a variable named my_baby_bool and set it equal to "true".

# Check the type of my_baby_bool using type(my_baby_bool).

# You’ll have to print it to get the results to display in the terminal.
my_baby_bool = "true"
print(type(my_baby_bool))
'''
It’s not a boolean variable! Boolean values True and False always need to be capitalized and do not have quotation marks.

Create a variable named my_baby_bool_two and set it equal to True.
'''
my_baby_bool_two = True

'''
Check the type of my_baby_bool_two and make sure you successfully created a boolean variable.

You’ll have to print it to get the results to display in the terminal.
'''
print(type(my_baby_bool_two))

'''
CONTROL FLOW
If Statements
“Okay okay okay, boolean variables, boolean expressions, blah blah blah, I thought I was learning how to build control flow into my code!”

You are, I promise you!

Understanding boolean variables and expressions is essential because they are the building blocks of conditional statements.

Recall the waking-up example from the beginning of this lesson. The decision-making process of “Is it raining? If so, bring an umbrella” is a conditional statement. Here it is phrased in a different way:

If it is raining then bring an umbrella.
Can you pick out the boolean expression here?

Right, "it is raining" is the boolean expression, and this conditional statement is checking to see if it is True.

If "it is raining" == True then the rest of the conditional statement will be executed and you will bring an umbrella.

This is the form of a conditional statement:

If [it is raining] then [bring an umbrella]
In Python, it looks very similar:

if is_raining:
  bring_umbrella()
You’ll notice that instead of “then” we have a colon, :. That tells the computer that what’s coming next is what should be executed if the condition is met. Let’s take a look at another conditional statement:

if 2 == 4 - 2: 
  print("apple")
Will this code print apple to the terminal? Yes, because the condition of the if statement, 2 == 4 - 2 is True.

Let’s work through a couple more together:

'''

'''
In the workspace script.py there is a function with an if statement. I wrote this function because my coworker Dave kept using my computer without permission and he is a real doofus. It takes user_name as an input and if the user is Dave it tells him to stay off my computer.

Enter a user name in the field for user_name and try running the function.
'''


def dave_check(user_name):
    if user_name == "Dave":
        return "Get off my computer Dave!"
    if user_name == "angela_catlady_87":
        return "I know it is you Dave! Go away!"


# Enter a user name here, make sure to make it a string
user_name = "Dave"

print(dave_check(user_name))

'''
CONTROL FLOW
Relational Operators II
Now that we’ve added conditional statements to our toolkit for building control flow, let’s explore more ways to create boolean expressions. So far we know two relational operators, equals and not equals, but there are a ton (well, four) more:

Greater than: >
Less than: <
Greater than or equal to: >=
Less than or equal to: <=
Let’s say we’re running a movie streaming platform and we want to write a function that checks if our users are over 13 when showing them a PG-13 movie. We could write something like:

def age_check(age):
  if age >= 13:
    return True
This function will take the users age and compare it to the number 13. If age is greater than or equal to 13 it will return True.

Let’s try some more!
'''

'''
Write a function called greater_than that takes two integer inputs, x and y and returns the value that is greater. If x and y are equal, return the string

"These numbers are the same"
'''


def greater_than(x, y):
    if x > y:
        return x
    if y > x:
        return y
    if x == y:
        return "These numbers are the same"


'''
The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it) requires students to earn 120 credits to graduate. Write a function called graduation_reqs that takes an input credits and checks if the student has enough credits to graduate. If they do, return the string

"You have enough credits to graduate!"
'''


def graduation_reqs(credits):
    if credits >= 120:
        return "You have enought credits to graduate"


print(graduation_reqs(120))

'''
Boolean Operators: and
Often, the conditions you want to check in your conditional statement will require more than one boolean expression to cover. In these cases, you can build larger boolean expressions using boolean operators. These operators (also known as logical operators) combine smaller boolean expressions into larger boolean expressions.

There are three boolean operators that we will cover:

and
or
not
Let’s start with and.

and combines two boolean expressions and evaluates as True if both its components are True, but False otherwise.

Consider the example

Oranges are a fruit and carrots are a vegetable.
This boolean expression is comprised of two smaller expressions, oranges are a fruit and carrots are a vegetable, both of which are True and connected by the boolean operator and, so the entire expression is True.

Let’s look at an example of some AND statements in Python:

>>> (1 + 1 == 2) and (2 + 2 == 4)
True
>>> (1 + 1 == 2) and (2 < 1)
False
>>> (1 > 9) and (5 != 6)
False
>>> (0 == 10) and (1 + 1 == 1) 
False
Notice that in the second and third examples, even though part of the expression is True, the entire expression as a whole is False because the other statement is False. The fourth statement is also False because both components are False.

'''

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
'''
Let’s return to Calvin Coolidge’s Cool College. 120 credits aren’t the only graduation requirement, you also need to have a GPA of 2.0 or higher. Rewrite the graduation_reqs function so it takes two inputs, gpa and credits, and checks to see if a student meets both requirements using an and statement.

If they do, return the string

"You meet the requirements to graduate!"
'''


def graduation_reqs(gpa, credits):
    if credits >= 120 and gpa >= 2.0:
        return "You meet the requirements to graduate!"


print(graduation_reqs(2.1, 130))

'''
CONTROL FLOW
Boolean Operators: or
The boolean operator or combines two expressions into a larger expression that is True if either component is True.

Consider the statement

Oranges are a fruit or apples are a vegetable.
This statement is composed of two expressions: oranges are a fruit which is True and apples are a vegetable which is False. Because the two expressions are connected by the or operator, the entire statement is True. Only one component needs to be True for an or statement to be True.

In English, or implies that if one component is True, then the other component must be False. This is not true in Python. If an or statement has two True components, it is also True.

Let’s take a look at a couple example in Python:

>>> True or (3 + 4 == 7)
True
>>> (1 - 1 == 0) or False
True
>>> (2 < 0) or True
True
>>> (3 == 8) or (3 > 4) 
False
Notice that each or statement that has at least one True component is True, but the final statement has two False components, so it is False.

'''
'''
Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

(2 - 1 > 3) or (-5 * 2 == -10)
Statement two:

(9 + 5 <= 15) or (7 != 4 + 3)
'''

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

'''
The registrars office at Calvin Coolidge’s Cool College has another request. They want to send out a mailer with information on the commencement ceremonies to students who have met at least one requirement for graduation (120 credits and 2.0 GPA).

Write a function called graduation_mailer that takes two inputs, gpa and credits and checks if a student either has 120 or more credits or a GPA 2.0 or higher and if so returns True.
'''


def graduation_mailer(gpa, credits):
    if (credits >= 120) or (gpa >= 2.0):
        return True


'''
Boolean Operators: not
The final boolean operator we will cover is not. This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement.

not True == False
not False == True
Consider the following statement:

Oranges are not a fruit.
Here, we took the True statement oranges are a fruit and added a not operator to make the False statement oranges are not a fruit.

This example in English is slightly different from the way it would appear in Python because in Python we add the not operator to the very beginning of the statement. Let’s take a look at some of those:

>>> not 1 + 1 == 2
False
>>> not 7 < 0
True
'''

'''
Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

not (4 + 5 <= 9)
Statement two:

not (8 * 2) != 20 - 4
'''
statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

'''
The registrar’s office at Calvin Coolidge’s Cool College has been so impressed with your work so far that they have another task for you. They want you to return to the first function you wrote, graduation_reqs, and add in several checks using and and not statements.

If a student meets both requirements the function should return
"You meet the requirements to graduate!"
If a student’s GPA is greater or equal to 2.0 but they don’t have enough credits the function should return
"You do not have enough credits to graduate."
If they have enough credits but their GPA is less than 2.0 the function should return
"Your GPA is not high enough to graduate."
If they do not have enough credits and their GPA is less than 2.0, the function should return
"You do not meet either requirement to graduate!"
Make sure your return value matches those strings exactly. Capitalization, punctuation, and spaces matter!

'''


def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    if (gpa >= 2.0) and (credits < 120):
        return "You do not have enough credits to graduate."
    if (gpa < 2.0) and not (credits < 120):
        return "Your GPA is not high enough to graduate."
    if (gpa < 2.0) and (credits < 120):
        return "You do not meet either requirement to graduate!"


print(graduation_reqs(1, 200))

'''
Else Statements
As you can tell from your work with Calvin Coolidge’s Cool College, once you start including lots of if statements in a function the code becomes a little cluttered and clunky. Luckily, there are other tools we can use to build control flow.

else statements allow us to elegantly describe what we want our code to do when certain conditions are not met.

else statements always appear in conjunction with if statements. Consider our waking-up example to see how this works:

if weekday:
  wake_up("6:30")
else:
  sleep_in()
In this way, we can build if statements that execute different code if conditions are or are not met. This prevents us from needing to write if statements for each possible condition, we can instead write a blanket else statement for all the times the condition is not met.

Let’s return to our age_check function for our movie streaming platform. Previously, all it did was check if the user’s age was over 13 and if so return True. We can use an else statement to return a message in the event the user is too young to watch the movie.

def age_check(age):
  if age >= 13:
    return True
  else:
    return "Sorry, you must be 13 or older to watch this movie."


'''
'''
Calvin Coolidge’s Cool College has another request for you. They want you to add an additional check to the graduation_reqs function. If a student is failing to meet both graduation requirements, they want the function to return:

"You do not meet the GPA or the credit requirement for graduation."
Use an else statement to add this to your function.
'''


def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    if (gpa >= 2.0) and not (credits >= 120):
        return "You do not have enough credits to graduate."
    if not (gpa >= 2.0) and (credits >= 120):
        return "Your GPA is not high enough to graduate."
    else:
        return "You do not meet the GPA or the credit requirement for graduation."


print(graduation_reqs(0, 0))

'''

CONTROL FLOW
Else If Statements
We have if statements, we have else statements, we can also have elif statements.

Now you may be asking yourself, what the heck is an elif statement? It’s exactly what it sounds like, “else if”. An elif statement checks another condition after the previous if statements conditions aren’t met.

We can use elif statements to control the order we want our program to check each of our conditional statements. First, the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is executed if none of the previous conditions have been met.

Let’s take a look at this in practice. The following function will display a “thank you” message after someone donates to a charity: It takes the donation amount and prints a message based on how much was donated.
'''


def thank_you(donation):
    if donation >= 1000:
        print("Thank you for your donation! You have achieved platinum donation status!")
    elif donation >= 500:
        print("Thank you for your donation! You have achieved gold donation status!")
    elif donation >= 100:
        print("Thank you for your donation! You have achieved silver donation status!")
    else:
        print("Thank you for your donation! You have achieved bronze donation status!")


'''
Take a second to think about this function. What would happen if all of the elif statements were simply if statements? If you donated $1000.00, then the first three messages would all print because each if condition had been met.

But because we used elif statements, it checks each condition sequentially and only prints one message. If I donate $600.00, the code first checks if that is over $1000.00, which it is not, then it checks if it’s over $500.00, which it is, so it prints that message, then because all of the other statements areelif and else, none of them get checked and no more messages get printed.

Try your hand at some other elif statements.
'''
''' 
Calvin Coolidge’s Cool College has noticed that students prefer to get letter grades over GPA numbers. They want you to write a function called grade_converter that converts an inputted GPA into the appropriate letter grade. Your function should be named grade_converter, take the input gpa, and convert the following GPAs:

4.0 or higher should return "A"
3.0 or higher should return "B"
2.0 or higher should return "C"
1.0 or higher should return "D"
0.0 or higher should return "F"
You can do this by creating a variable called grade.

Then, you should use elif statements to set grade to the appropriate letter grade for the gpa entered.

At the end of the function, return grade.

'''


def grade_converter(gpa):
    if gpa >= 4.0:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    elif gpa >= 1.0:
        grade = "D"
    elif gpa >= 0:
        grade = "F"
    return grade


'''

CONTROL FLOW
Try and Except Statements
if, elif, and else statements aren’t the only way to build a control flow into your program. You can use try and except statements to check for possible errors that a user might encounter.

The general syntax of a try and except statement is

try:
    # some statement
except ErrorName:
    # some statement
First, the statement under try will be executed. If at some point an exception is raised during this execution, such as a NameError or a ValueError and that exception matches the keyword in the except statement, then the try statement will terminate and the except statement will execute.

Let’s take a look at this in an application. I want to write a function that takes two numbers, a and b as an input and then returns a divided by b. But, there is a possibility that b is zero, which will cause an error, so I want to include a try and except flow to catch this error.
'''


def divides(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Can't divide by zero!")


# Now that you see how it works, try to write one yourself.


'''
The function in the editor is very simple and serves one purpose: it raises a ValueError.

Try running it by entering raises_value_error() into the code editor and hitting run.

Remember, unindent this function call so it isn’t included in the function itself.

'''

'''
The function in the editor is very simple and serves one purpose: it raises a ValueError.

Try running it by entering raises_value_error() into the code editor and hitting run.

Remember, unindent this function call so it isn’t included in the function itself.
Great! Nice error raising! Now let’s make that error message a little more palatable.

Write a try statement and an except statement around the line of code that executes the function to catch a ValueError and make the error message print You raised a ValueError!
'''


def raises_value_error():
    raise ValueError


try:
    raises_value_error()
except ValueError:
    print("You raised a ValueError!")

'''

CONTROL FLOW
Review
Great job! We covered a ton of material in this lesson and you’ve increased the number of tools in your Python toolkit by several-fold. Let’s review what you’ve learned this lesson:

Boolean expressions are statements that can be either True or False
A boolean variable is a variable that is set to either True or False.
You can create boolean expressions using relational operators:
Equals: ==
Not equals: !=
Greater than: >
Greater than or equal to: >=
Less than: <
Less than or equal to: <=
if statements can be used to create control flow in your code.
else statements can be used to execute code when the conditions of an if statement are not met.
elif statements can be used to build additional checks into your if statements
try and except statements can be used to build error control into your code.
Let’s put these skills to the test!

'''

'''
The admissions office at Calvin Coolidge’s Cool College has heard about your programming prowess and wants to get a piece of it for themselves. They’ve been inundated with applications and need a way to automate the filtering process. They collect three pieces of information for each applicant:

Their high school GPA, on a 0.0 - 4.0 scale.
Their personal statement, which is given a score on a 1 - 100 scale.
The number of extracurricular activities they participate in.
The admissions office has a cutoff point for each category. They want students that have a GPA of 3.0 or higher, a personal statement with a score of 90 or higher, and who participated in 3 or more extracurricular activities.

Write a function called applicant_selector which takes three inputs, gpa, ps_score, and ec_count. If the applicant meets the cutoff point for all three categories, have the function return the string:

'''

'''
The admissions office at Calvin Coolidge’s Cool College has heard about your programming prowess and wants to get a piece of it for themselves. They’ve been inundated with applications and need a way to automate the filtering process. They collect three pieces of information for each applicant:

Their high school GPA, on a 0.0 - 4.0 scale.
Their personal statement, which is given a score on a 1 - 100 scale.
The number of extracurricular activities they participate in.
The admissions office has a cutoff point for each category. They want students that have a GPA of 3.0 or higher, a personal statement with a score of 90 or higher, and who participated in 3 or more extracurricular activities.

Write a function called applicant_selector which takes three inputs, gpa, ps_score, and ec_count. If the applicant meets the cutoff point for all three categories, have the function return the string:
The admissions office at Calvin Coolidge’s Cool College has heard about your programming prowess and wants to get a piece of it for themselves. They’ve been inundated with applications and need a way to automate the filtering process. They collect three pieces of information for each applicant:

Their high school GPA, on a 0.0 - 4.0 scale.
Their personal statement, which is given a score on a 1 - 100 scale.
The number of extracurricular activities they participate in.
The admissions office has a cutoff point for each category. They want students that have a GPA of 3.0 or higher, a personal statement with a score of 90 or higher, and who participated in 3 or more extracurricular activities.

Write a function called applicant_selector which takes three inputs, gpa, ps_score, and ec_count. If the applicant meets the cutoff point for all three categories, have the function return the string:

"This applicant should be accepted."
2.
Great! The admissions office also wants to give students who have a high GPA and a strong personal statement a chance even if they don’t participate in enough extracurricular activities.

If an applicant meets the cutoff point for GPA and personal statement score, but not the extracurricular activity count, the function should return the string:

"This applicant should be given an in-person interview."
3.
Finally, for all other cases, the function should return the string:

"This applicant should be rejected."
'''


def applicant_selector(gpa, ps_score, ec_count):
    if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
        return "This applicant should be accepted"
    elif gpa >= 3.0 and ps_score >= 90 and ec_count > 3:
        return "This applicant should be given an in-person interview."
    else:
        return "This applicant should be rejected."


