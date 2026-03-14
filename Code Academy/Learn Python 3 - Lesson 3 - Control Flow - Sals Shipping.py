"""
Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:
Flat charge: $125.00

Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

"""

flat_charge = 20
premium_shipping_charge = 125


def ground_shipping_cost_normal(weight):
    if weight <= 2:
        return (1.50 * weight) + flat_charge
    elif 2 < weight <= 6:
        return (3.00 * weight) + flat_charge
    elif weight > 6 and weight <= 10:
        return (4.00 * weight) + flat_charge
    elif weight > 10:
        return (4.75 * weight) + flat_charge
    else:
        return "Error in weight submitted"


print(ground_shipping_cost_normal(8.4))


def drone_shipping_cost_normal(weight):
    if weight <= 2:
        return 4.50 * weight
    elif 2 < weight <= 6:
        return 9.00 * weight
    elif weight > 6 and weight <= 10:
        return 12.00 * weight
    elif weight > 10:
        return 14.25 * weight
    else:
        return "Error in weight submitted"


print(drone_shipping_cost_normal(1.5))


def check_shipping_cost(weight):
    ground_cost = ground_shipping_cost_normal(weight)
    drone_cost = drone_shipping_cost_normal(weight)
    if ground_cost < drone_cost and ground_cost < premium_shipping_charge:
        print("Ground shipping is cheaper at $" + str(ground_cost))
    elif drone_cost < ground_cost and drone_cost < premium_shipping_charge:
        print("Drone shipping is less expensive at $" + str(drone_cost))
    elif premium_shipping_charge < ground_cost and premium_shipping_charge < drone_cost:
        print("Premium shipping is less expensive at $" + str(premium_shipping_charge))
    else:
        print("you screwed up")


try:
    check_shipping_cost(float(input("Enter shipping weight: ")))
except:
    print("idiot")
