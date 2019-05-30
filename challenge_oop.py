### OOP Challenge ###

# Build a fruid stand that has a barrel for fruit and fruits have a name and a price
# You should be able to get the total cost of the barrel, given the number of fruit in it and their cost
# A barrel can only hold one fruit type

# Fruit object

class Fruit: 
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Barrel object

class Barrel:
    def __init__(self):
        self.fruit_count = 0
        self.fruit_type = None
    
    def sum_total(self):
        return self.fruit_count * self.fruit_type.price

    def add_fruit(self, fruit):
        if self.fruit_type == fruit: 
            self.fruit_count += 1
        elif self.fruit_type == None:
            self.fruit_type = fruit
            self.fruit_count += 1
        else:
            return "Invalid Barrel for that Fruit"

# apple = Fruit("Apple", 1.25)

# apple_barrel = Barrel()

# apple_barrel.add_fruit(apple)
# apple_barrel.add_fruit(apple)
# apple_barrel.add_fruit(apple)
# apple_barrel.add_fruit(apple)
# apple_barrel.add_fruit(apple)
# apple_barrel.add_fruit(apple)
# apple_barrel.add_fruit(apple)
# print(apple_barrel.sum_total())

"""
Make a menu class that asks a user if they want to do:
1. add to a barrel
2. get the type of fruit in a barrel
3. remove an amount from the barrel
4. reset the barrel, emptying and setting type to none
5. exit

ALSO -  Make  the needed barrel methods
DUE: Start of class tomorrow
"""
