"""Basta Fazoolin' You’ve started position as the lead programmer for the family-style Italian restaurant Basta
Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been
hired to keep things organized.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get
Unstuck“ to see a project walkthrough video.

"""

# At Basta Fazoolin’ with my Heart our motto is simple: when you’re here with family, that’s great! We have four
# different menus: brunch, early-bird, dinner, and kids.
#
# Create a Menu class .
# Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
import datetime
import time


class Menu():
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this
    # representation when the menu is available.
    def __repr__(self):
        return self.name + " menu is available from " + str(self.start_time) + " to " + str(self.end_time)

    # Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names of
    # purchased items.
    #
    # Have calculate_bill return the total price of a purchase consisiting of all the items in purchased_items.

    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            total += self.items[item]
        return total


# Let’s create our first menu: brunch. Brunch is served from 11am to 4pm. The following items are sold during brunch:
#
# { 'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
# 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50 }

brunch = Menu("brunch", {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, datetime.time(hour=11), datetime.time(hour=16))

# Let’s create our second menu item early_bird. Early-bird Dinners are served from 3pm to 6pm. The following items
# are available during the early-bird menu:
#
# { 'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi':
# 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00, }

early_bird = Menu("early_bird", {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, datetime.time(hour=15), datetime.time(hour=18))

# Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm. The following items are available for dinner:
#
# { 'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
# 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00, }

dinner = Menu("dinner", {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, datetime.time(hour=17), datetime.time(hour=23))

# And let’s create our last menu, kids. The kids menu is available from 11am until 9pm. The following items are
# available on the kids menu.
#
# {
#   'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
# }

kids = Menu("kids", {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, datetime.time(hour=11), datetime.time(hour=21))

print(brunch)
print(early_bird)
print(dinner)
print(kids)

# Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries,
# and one coffee. Pass that into brunch.calculate_bill() and print out the price.

print("Brunch costs ", brunch.calculate_bill(["pancakes", "home fries", "coffee"]))

# What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli.
# Calculate the bill with .calculate_bill().

print("Early Bird costs ", early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))


# Basta Fazoolin’ with my Heart has seen tremendous success with the family market, which is fantastic because when
# you’re at Basta Fazoolin’ with my Heart with family, that’s great!
#
# We’ve decided to create more than one restaurant to offer our fantastic menus, services, and ambience around the
# country.
#
# First, let’s create a Franchise class. Give the Franchise class a constructor. Take in an address, and assign it to
# self.address. Also take in a list of menus and assign it to self.menus.

class Franchise():
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # Give our Franchises a string representation so that we’ll be able to tell them apart. If we print out a
    # Franchise it should tell us the address of the restaurant.
    def __repr__(self):
        return self.address

    # Let’s tell our customers what they can order! Give Franchise an .available_menus() method that takes in a time
    # parameter and returns a list of the Menu objects that are available at that time.
    def available_menus(self, time):
        temp_list = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                temp_list.append(menu)
        return temp_list


# Let’s create our first two franchises! Our flagship store is located at "1232 West End Road" and our new
# installment is located at "12 East Mulberry Street". Pass in all four menus along with these addresses to define
# flagship_store and new_installment.

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print("Flagship Store is located at", flagship_store)
print("New Installment is located at", new_installment)

print("The following menus are availalbe at Noon: ", flagship_store.available_menus(datetime.time(hour=12)))
print("The following menus are availalbe at at five ", flagship_store.available_menus(datetime.time(hour=17)))


#
# Since we’ve been so successful building out a branded chain of restaurants, we’ve decided to diversify. We’re going
# to create a restaurant that sells arepas!

# First let’s define a Business class.

# Give Business a constructor. A Business needs a name and a list of franchises.

class Business():
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# Let’s create our first Business. The name is "Basta Fazoolin' with my Heart" and the two franchises are
# flagship_store and new_installment.



# Before we create our new business, we’ll need a Franchise and before our Franchise we’ll need a menu. The items for
# our Take a’ Arepa available from 10am until 8pm are the following:
#
# {
#   'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
# }
# Save this to a variable called arepas_menu.

arepas_menu = Menu("Take a Arepa", {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, datetime.time(hour=10), datetime.time(hour=20))

# Next let’s create our first Take a’ Arepa franchise! Our new restaurant is located at "189 Fitzgerald Avenue". Save
# the Franchise object to a variable called arepas_place.

arepas_place = Franchise("189 Fitzgerald Ave", [arepas_menu])

# Now let’s make our new Business! The business is called "Take a' Arepa"!
first_business = Business("Basta Fazoolin' with my Heart", [arepas_place])