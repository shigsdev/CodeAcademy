'''
Python Code Challenges: Classes (Advanced)
Difficult Python Code Challenges Involving Classes

This article will help you review Python classes by providing some interesting code challenges.

Some of these challenges are difficult! Take some time to think about them before starting to code.

You might not get the solution correct on your first try — look at your output, try to find where you’re going wrong,
and iterate on your solution.

Finally, if you get stuck, use our solution code! If you “Check Answer” twice with an incorrect solution, you should
see an option to get our solution code. However, truly investigate that solution — experiment and play with the
solution code until you have a good grasp of how it is working. Good luck!

Class Syntax
As a refresher, class syntax looks like this:

class MyClass:
    # ... class variables ...

    def __init__(self):
        # ... instance variables ...
For example, a class which defines a rectangle using a class variable, instance variables, and a method looks like this:

class Rectangle:
    sides = 4

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


rectangle_1 = Rectangle(5, 10)
rect_area = rectangle_1.calculate_area()

The last two lines in the above example show how to initialize an object of the class as well as calling one of the
methods.



'''

# Challenges You have created a robotics company which began with four-wheeled driving robots, but you are now
# expanding the technology to include bipedal robots. Since a lot of robotic logic already exists from the driving
# robot, we can modularize the robot class structure using object oriented programming concepts such as inheritance.
# These five advanced challenge problems will test your knowledge of classes and interactions between multiple classes.

'''1. Robot Inheritance The generic variables and methods have been placed into a Robot class for you. You will need 
to create two new classes. One for DriveBot and one for WalkBot. Both of these should inherit from the Robot class. 
The constructor for the DriveBot will be essentially the same as the superclass constructor, but the WalkBot 
constructor will include an extra parameter for an instance variable called step_length. Here is what we need to do: 

Create a new class called DriveBot which inherits from the Robot class Call the superclass constructor within the 
DriveBot constructor but pass motor_speed as the parameter for speed in the super class Create a new class called 
WalkBot which inherits from the Robot class Add another parameter to the WalkBot constructor for step_length which 
defaults to 5 Call the superclass constructor within the constructor for the WalkBot class Assign the input parameter 
for step_length to a new instance variable for step_length 

'''


# Create two new classes which inherit from the Robot class. The first class is the DriveBot class which should use
# the Robot constructor. The speed of the DriveBot will be represented by the motor_speed. You can pass in
# motor_speed as a parameter in the superclass constructor. The next class is the WalkBot class. This class should
# also use the Robot constructor, but the speed is represented by steps_per_minute which you can pass into the
# superclass constructor. Additionally, the WalkBot constructor should include another parameter for step_length.
# This should default to 5 if not provided and should be assigned to an instance variable called step_length.

class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed=0, direction=180, sensor_range=10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

    def __add__(self, value):
        self.speed += value

    def __sub__(self, value):
        self.speed -= value


# Create the DriveBot class here!
class DriveBot(Robot):
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        super().__init__(motor_speed, direction, sensor_range)

    def __add__(self, value):
        super().__add__(value)
        self.sensor_range += value

    def __sub__(self, value):
        super().__sub__(value)
        self.sensor_range -= value


# Create the WalkBot class here!
class WalkBot(Robot):
    walk_bot_count = 0

    def __init__(self, steps_per_minute=0, direction=180, sensor_range=10, step_length=5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

        WalkBot.walk_bot_count += 1
        if WalkBot.walk_bot_count >= 5 and Robot.robot_count >= 10:
            Robot.all_disabled = True

    def adjust_sensor(self, new_sensor_range):
        super().adjust_sensor(new_sensor_range)
        self.obstacle_found = False
        self.step_length = 5

    def avoid_obstacles(self):
        if (self.obstacle_found):
            if (self.speed <= 60):
                super().avoid_obstacles()
            else:
                self.direction = (self.direction + 90) % 360
                self.obstacle_found = False
            self.speed /= 2
            self.step_length /= 2

    def __add__(self, value):
        super().__add__(value)
        self.step_length += value / 2

    def __sub__(self, value):
        super().__sub__(value)
        self.step_length -= value / 2


# Uncomment the robot instantiation!
robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = WalkBot(20, 90, 15, 10)

# Use these print statements to test your code!

print(robot_2.id)
print(robot_3.step_length)
print(robot_1.speed)

# Here are the two new classes which we created:
#
# class DriveBot(Robot):
#     def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
#         super().__init__(motor_speed, direction, sensor_range)
#
# class WalkBot(Robot): def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length =
# 5): super().__init__(steps_per_minute, direction, sensor_range) self.step_length = step_length By placing Robot in
# the parentheses next to the two new classes, we cause them to inherit from the Robot class. We can use super(
# ).__init__(self, param_1, param_2, etc...) to call the superclass constructor. This will use the constructor in the
# Robot class to assign the values to the instance variables. Any new changes can then be added afterward.

'''2. Using The Superclass There was an issue discovered when testing the WalkBot prototypes. In some cases, 
the robots were incorrectly detecting their own legs as obstacles. To overcome this, we need to modify our 
adjust_sensor method to reset obstacle_found to False and step_length to 5 while also using the original logic from 
the superclass. Here are the steps: 

Override the adjust_sensor method in the WalkBot class by re-defining it in that class.
Call the superclass version of the method within adjust_sensor
Add a line of code to set obstacle_found to False
Add a line of code to set step_length to 5
'''

# Within the WalkBot class, override the adjust_sensor method to set the obstacle_found instance variable to False
# and set the step_length to 5 in addition to the the original logic from the superclass.
robot_walk = WalkBot(60, 90, 10, 15)
robot_walk.obstacle_found = True
print(robot_walk.sensor_range)
print(robot_walk.obstacle_found)
print(robot_walk.step_length)
# Call the overridden adjust_sensor method here!
robot_walk.adjust_sensor(5)

print(robot_walk.sensor_range)
print(robot_walk.obstacle_found)
print(robot_walk.step_length)

# Here is the new version of the WalkBot class:
#
# class WalkBot(Robot):
#
#     def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
#         super().__init__(steps_per_minute, direction, sensor_range)
#         self.step_length = step_length
#
# def adjust_sensor(self, new_sensor_range): super().adjust_sensor(new_sensor_range) self.obstacle_found = False
# self.step_length = 5 As you can see, in order to override the method, we can re-define it again with the same name.
# You can use super().method_name() in order to call the superclass version of the method.

'''3. Conditional Superclass Logic Since the bipedal robot is a bit less stable, the obstacle avoidance must be more 
delicate. Because of this, we want to call the superclass method for avoiding obstacles within the bipedal robot 
class if the steps per minute are less than or equal to 60, otherwise the WalkBot should only rotate 90 degrees 
clockwise and set obstacle_found to False. In either case, we need to half the robot’s speed and step_length in order 
to slow it down during the turn. Here are the steps we need to do: 

Within the WalkBot class, override the method called avoid_obstacles by re-defining it in the class. If an obstacle 
was found If the speed if less than or equal to 60 Call the superclass version of the method Otherwise add 90 to the 
WalkBot‘s direction. If the new direction is greater than 360, it should loop back around to be between 0 and 360. 
For example, if the new direction is 370, it should really be 10. (hint: use modulo to do this!) You should also set 
obstacle_found to False is the speed was over 60. Regardless of whether an obstacle was found, half the speed and the 
step_length of the robot 

'''

# Create the method avoid_obstacles within the WalkBot class which overrides the same method from the Robot class.
# This method should call the superclass avoid_obstacles method if obstacle_found is True and the speed is less than
# or equal to 60, otherwise rotate the robot by 90 degrees (adding 90 to the current direction) and set
# obstacle_found to False. The direction should not be able to go above 360 degrees (use modulus in a similar way as
# the superclass method). In either case, the speed and step_length of the WalkBot should be halved to ensure that
# the robot does not fall over when turning to avoid the obstacle.

robot_1 = WalkBot(150, 0, 10, 10)
robot_1.obstacle_found = True
robot_1.avoid_obstacles()

print(robot_1.direction)
print(robot_1.speed)
print(robot_1.step_length)

robot_2 = WalkBot(60, 0, 20, 40)
robot_2.obstacle_found = True
robot_2.avoid_obstacles()

print(robot_2.direction)
print(robot_2.speed)
print(robot_2.step_length)

# Here is the overridden method:
#
# def avoid_obstacles(self): if(self.obstacle_found): if(self.speed <= 60): super().avoid_obstacles() else:
# self.direction = (self.direction + 90) % 360 self.obstacle_found = False self.speed /= 2 self.step_length /= 2 This
# method shows how the superclass method can be called conditionally. In this case it depends on the speed of the
# robot and if an obstacle was found. We use modulus when rotating the robot to loop back past 0 if we go over 360
# degrees. This is because the robot would have made a full circle.

'''4. Overriding Dunder Methods Let’s add an easy way to increase and decrease our speed as well as some other 
attributes depending on the type of robot. For the Robot class, we want to increase and decrease the speed using the 
+ and - operators. For the DriveBot class, we want to adjust the speed and sensor_range with those operators. Lastly, 
for the WalkBot class, we want to adjust the speed and step_length with those operators. We can override the dunder 
methods which represent those operations and call the superclass version of those dunder methods. Here are the steps: 

In the Robot class, override the + operator to add to the speed of the robot In the Robot class, override the - 
operator to subtract from the speed of the robot In the DriveBot class, override the + operator to call the 
superclass version of the operator as well as add to the sensor_range of the robot In the DriveBot class, 
override the - operator to call the superclass version of the operator as well as subtract from the sensor_range of 
the robot In the WalkBot class, override the + operator to call the superclass version of the operator as well as add 
half of the value on the right side of the operator to the step_length of the robot In the WalkBot class, 
override the - operator to call the superclass version of the operator as well as subtract half of the value on the 
right side of the operator from the step_length of the robot 

'''

# Within the Robot class, override the + and - operations to increase or decrease the speed of the robot. For the
# DriveBot class, the + and - operations should also increase and decrease the sensor_range of the robot. For the
# WalkBot class, those operations should increase or decrease the step_length by half of the amount added. This will
# change the distance that the robot travels per step based on the change in speed from the operations.


robot_1 = DriveBot()
robot_2 = WalkBot()

# Uncomment these lines when you are ready to test your code!
robot_1 + 20
robot_1 - 10
robot_2 + 10
robot_2 - 5

print(robot_1.speed)
print(robot_1.sensor_range)
print(robot_2.speed)
print(robot_2.step_length)

# Here are the overridden dunder methods in each class:
#
# class Robot:
#     def __add__(self, value):
#         self.speed += value
#
#     def __sub__(self, value):
#         self.speed -= value
#
# class DriveBot(Robot):
#     def __add__(self, value):
#         super().__add__(value)
#         self.sensor_range += value
#
#     def __sub__(self, value):
#         super().__sub__(value)
#         self.sensor_range -= value
#
# class WalkBot(Robot):
#     def __add__(self, value):
#        super().__add__(value)
#        self.step_length += value / 2
#
# def __sub__(self, value): super().__sub__(value) self.step_length -= value / 2 The above code only shows the dunder
# methods which were added to each class. The child classes both override those operations as well. This shows how
# superclass versions of dunder methods can also be called from a child class.

'''5. Prevent A Robot Takeover Finally, we are going to make some last additions to our bipedal robot and test it 
out. Your customers are worried that your new robot model might become sentient when controlled in large numbers. To 
prevent this, program the bipedal robots so that if five WalkBots are created when there are already at least 5 
DriveBots (causing 10 or more total bots) then disable all robots. This is what you need to do: 

Create a new class variable in the WalkBot class to count the number of WalkBot instances In the constructor for the 
WalkBot, increment the counter by 1 Also, in the constructor, check if the number of total Robots (from the 
superclass) is greater than or equal to 10 and if the number of WalkBots is greater than or equal to 5. If so, 
disable all robots 

'''

# Update the WalkBot class to keep track of how many WalkBot objects are created. If the total number of robots is 10
# or above and there are at least 5 WalkBot objects created then set all_disabled to True for all robots. Use a class
# variable called walk_bot_count within the WalkBot class.

robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = DriveBot()
robot_4 = DriveBot()
robot_5 = WalkBot()
robot_6 = DriveBot()
robot_7 = DriveBot()
robot_8 = WalkBot()
robot_9 = WalkBot()
print(Robot.all_disabled)
robot_10 = WalkBot()
print(Robot.all_disabled)

# Here is the updated constructor and class variable for the WalkBot class:
#
# class WalkBot(Robot):
#     walk_bot_count = 0
#
#     def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
#         super().__init__(steps_per_minute, direction, sensor_range)
#         self.step_length = step_length
#
# WalkBot.walk_bot_count += 1 if(WalkBot.walk_bot_count >= 5 and Robot.robot_count >= 10): Robot.all_disabled = True
# This modification uses a similar method of counting from the Robot class, but it uses a separate counter to only
# track the number of WalkBots. Whenever a new WalkBot is created, the constructor is called and the two counts are
# checked. If the total number of robots is at least 10 and the number of WalkBots reaches 5 then all robots are
# disabled.
