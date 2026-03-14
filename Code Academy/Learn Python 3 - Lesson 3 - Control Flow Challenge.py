'''

Create a function named large_power() that takes two parameters named base and exponent.

If base raised to the exponent is greater than 5000, return True, otherwise return False

'''


def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False


print(large_power(2, 13))
print(large_power(2, 12))

try:
    base_number = float(input("Please enter the base #: "))
    exponent_number = float(input("Please enter the exponent #: "))
except:
    print("you fucked up again")

try:
    if large_power(base_number, exponent_number):
        print("Its true - the base number of " + str(base_number) + " with an exponent of " + str(
            exponent_number) + " is greater than 5000")
    else:
        print("Its false - the base number of " + str(base_number) + " with an exponent of " + str(
            exponent_number) + " is less than 5000")

except:
    print("you fucked up")

'''
Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent.

The function should return True if budget is less than the sum of the other four parameters — you’ve gone over budget! Return False otherwise.

'''


def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < (food_bill + electricity_bill + internet_bill + rent):
        return True
    else:
        return False


print(over_budget(100, 20, 30, 10, 40))
print(over_budget(80, 20, 30, 10, 40))

'''
Create a function named twice_as_large() that has two parameters named num1 and num2.

Return True if num1 is more than double num2. Return False otherwise.

'''


def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False


print(twice_as_large(10, 5))
print(twice_as_large(11, 5))

'''
Create a function called divisible_by_ten() that has one parameter named num.

The function should return True if num is divisible by 10, and False otherwise. Consider using modulo (%) to check for divisibility.

'''


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False


'''
Create a function named not_sum_to_ten() that has two parameters named num1 and num2.

Return True if num1 and num2 do not sum to 10. Return False otherwise.

'''


def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False


# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5, 5))
# should print False
