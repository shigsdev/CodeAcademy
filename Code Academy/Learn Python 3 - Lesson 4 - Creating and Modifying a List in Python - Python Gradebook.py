'''
Python Gradebook
You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

'''

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

'''

Create a list called subjects and fill it with the classes you are taking:

"physics"
"calculus"
"poetry"
"history"

'''

subjects = ['physics', 'calculus', 'poetry', 'history']
subjects.append('computer science')
'''

Create a list called grades and fill it with your scores:

98
97
85
88

'''
grades = [98, 97, 85, 88]
grades.append(100)
'''

Use the zip() function to combine subjects and grades.

Save this zip object as a list into a variable called gradebook.

'''

gradebook = list(zip(subjects, grades))

print(gradebook)

'''
Your grade for Computer Science class just came in! You got a perfect score, 100!

After your definitions of subjects and grades but before you create gradebook, use append to add "computer science" to subjects and 100 to grades.

'''


# You also have your grades from last semester, stored in last_semester_gradebook. Create a new variable
# full_gradebook with the items from both gradebook and last_semester_gradebook.

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)

