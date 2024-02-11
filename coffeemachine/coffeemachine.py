class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def display_resources(self):
        print(f"The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.money} of money")

    def buy_coffee(self, coffee_type):
        espresso_requirements = {'water': 250, 'milk': 0, 'coffee_beans': 16, 'cost': 4}
        latte_requirements = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'cost': 7}
        cappuccino_requirements = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'cost': 6}

        if coffee_type == 1:  # Espresso
            self.make_coffee(espresso_requirements)
        elif coffee_type == 2:  # Latte
            self.make_coffee(latte_requirements)
        elif coffee_type == 3:  # Cappuccino
            self.make_coffee(cappuccino_requirements)

    def make_coffee(self, requirements):
        if self.water < requirements['water']:
            print("Sorry, not enough water!")
        elif self.milk < requirements['milk']:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < requirements['coffee_beans']:
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= requirements['water']
            self.milk -= requirements['milk']
            self.coffee_beans -= requirements['coffee_beans']
            self.disposable_cups -= 1
            self.money += requirements['cost']

    def fill_resources(self, added_water, added_milk, added_coffee_beans, added_disposable_cups):
        self.water += added_water
        self.milk += added_milk
        self.coffee_beans += added_coffee_beans
        self.disposable_cups += added_disposable_cups

    def take_money(self):
        print(f"I gave you {self.money}")
        self.money = 0

# Створення об'єкту CoffeeMachine з початковими значеннями
coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")

    if action == "buy":
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:\n")
        if coffee_type == "back":
            continue
        else:
            coffee_machine.buy_coffee(int(coffee_type))
    elif action == "fill":
        added_water = int(input("Write how many ml of water do you want to add:\n"))
        added_milk = int(input("Write how many ml of milk do you want to add:\n"))
        added_coffee_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        added_disposable_cups = int(input("Write how many disposable coffee cups do you want to add:\n"))
        coffee_machine.fill_resources(added_water, added_milk, added_coffee_beans, added_disposable_cups)
    elif action == "take":
        coffee_machine.take_money()
    elif action == "remaining":
        coffee_machine.display_resources()
    elif action == "exit":
        break