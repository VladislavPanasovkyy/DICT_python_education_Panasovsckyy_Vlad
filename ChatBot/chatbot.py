bot_name = "My1Bott"
birth_year = 2023

greeting = f"Hello! My name is {bot_name}.\nI was created in {birth_year}."

print(greeting)

your_name = input("Please, remind me your name: ")

if your_name:
    print(f"What a great name you have, {your_name}!")
else:
    print("You didn't provide your name.")

print("Let me guess your age.")
remainder3 = int(input("Enter remainder of dividing your age by 3: "))
remainder5 = int(input("Enter remainder of dividing your age by 5: "))
remainder7 = int(input("Enter remainder of dividing your age by 7: "))

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
number = int(input("Enter a positive number: "))

if number <= 0:
    print("Please enter a positive number.")
else:
    for i in range(number + 1):
        print(f"{i} !")

print("Let's test your programming knowledge.")
questions = [
    "Why do we use methods?",
    "1. To repeat a statement multiple times.",
    "2. To decompose a program into several small subroutines.",
    "3. To determine the execution time of a program.",
    "4. To interrupt the execution of a program."
]
correct_answer = "2"

for question in questions:
    print(question)

while True:
    user_answer = input("Enter the number of your answer: ")
    if user_answer == correct_answer:
        break
    else:
        print("Please, try again.")

print("Congratulations, have a nice day!")