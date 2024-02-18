import random

def arithmetic_test_stage3():
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")

    while True:
        try:
            level = int(input("> "))
            if level not in [1, 2]:
                raise ValueError("Invalid level. Enter 1 or 2.")
            break
        except ValueError as e:
            print(f"Incorrect format. {e}")

    correct_answers = 0
    level_description = ""

    if level == 1:
        level_description = "simple operations with numbers 2-9"
    elif level == 2:
        level_description = "integral squares of 11-29"

    for _ in range(5):
        if level == 1:
            num1 = random.randint(2, 9)
            num2 = random.randint(2, 9)
            operator = random.choice(['+', '-', '*'])
            question = f"{num1} {operator} {num2}"
        elif level == 2:
            num1 = random.randint(11, 29)
            question = f"{num1}^2"

        while True:
            try:
                user_answer = input(f"{question}\n> ")

                if level == 1:
                    user_answer = int(user_answer)
                    correct_answer = eval(question)
                elif level == 2:
                    user_answer = int(user_answer) ** 2
                    correct_answer = num1 ** 2

                if user_answer == correct_answer:
                    print("Right!")
                    correct_answers += 1
                else:
                    print(f"Wrong! Correct answer: {correct_answer}")
                break
            except (ValueError, SyntaxError):
                print("Incorrect format. Enter a valid number.")

    print(f"Your mark is {correct_answers}/5.")

    # Запитуємо, чи користувач хоче зберегти результати
    save_result = input("Would you like to save your result to the file? Enter yes or no.\n> ").lower()

    # Якщо користувач погоджується, то зберігаємо результат у файл
    if save_result in ["yes", "y"]:
        name = input("What is your name?\n> ")
        with open("results.txt", "a") as file:
            file.write(f"{name}: {correct_answers}/5 in level {level} ({level_description}).\n")
        print("The results are saved in \"results.txt\".")
    else:
        print("Goodbye!")

# Викликаємо функцію для виконання тесту
arithmetic_test_stage3()
