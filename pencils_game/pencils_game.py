import random

def pencils_game():
    # Запитуємо кількість олівців та перевіряємо правильність введення
    while True:
        try:
            num_pencils = int(input("How many pencils would you like to use:\n> "))
            if num_pencils <= 0:
                print("The number of pencils should be positive")
            else:
                break
        except ValueError:
            print("The number of pencils should be numeric")

    # Запитуємо хто йде першим
    while True:
        player1 = input("Who will be the first (John, Jack):\n> ")
        if player1.lower() in ['john', 'jack']:
            break
        else:
            print("Choose between 'John' and 'Jack'")

    # Хто йде першим
    player2 = 'Jack' if player1.lower() == 'john' else 'John'
    first_player = player1

    # Виводимо рядок з олівцями
    print("|" * num_pencils)

    # Цикл гри
    while num_pencils > 0:
        # Перевірка, чи поточний гравець - бот
        if first_player.lower() == 'jack':

            if num_pencils % 4 == 0:
                taken_pencils = random.randint(1, 3)
            else:
                taken_pencils = num_pencils % 4

            print(f"{first_player}'s turn: {taken_pencils}")
        else:
            # Гравець вводить кількість олівців
            while True:
                try:
                    taken_pencils = int(input(f"{first_player}'s turn:\n> "))
                    if 1 <= taken_pencils <= 3 and taken_pencils <= num_pencils:
                        break
                    elif taken_pencils <= 0:
                        print("Possible values: '1', '2' or '3'")
                    elif taken_pencils > num_pencils:
                        print("Too many pencils were taken")
                    else:
                        print("Possible values: '1', '2' or '3'")
                except ValueError:
                    print("Possible values: '1', '2' or '3'")

        num_pencils -= taken_pencils

        print("|" * num_pencils)

        # Змінюємо гравця
        first_player = player1 if first_player == player2 else player2

    print(f"{first_player} won!")

# Викликаємо функцію гри
pencils_game()
