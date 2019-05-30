import sys
from challenge_oop import Fruit, Barrel



class Menu:
    def __init__(self):
        self.fruit_barrel = fruit_barrel
        self.choices = {
            "1": self.add_fruits,
            "2": self.show_fruits,
            "3": self.remove.fruits,
            "4": self.empty.fruits,
            "5": exit
        }

    def display_menu(self):
        print(
"""
Fruit Barrel Menu:
1. Add Fruit to a Barrel
2. Get Type of Fruit in Barrel
3. Remove Fruit from Barrel
4. Empty Fruit Barrel
5. Exit
"""
)

    def run(self):
        while True:
            self.display_menu()
            choice = input("What would you like to do? \n ")
            action = self.choice.get(choice)
            if action: 
                action()
            else:
                print(f"{choice} is not a valid option")

    def add_fruit(self, fruits = None):
        if not fruits:
            fruits = self.fruit_barrel.fruits
            for fruit in fruits: