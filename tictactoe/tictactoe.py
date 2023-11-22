def print_board(cells):
    print("---------")
    for i in range(6, -1, -3):
        row = "| " + " ".join(cells[i:i+3]) + " |"
        print(row)
    print("---------")

def check_winner(cells):
    # Перевірка горизонталей, вертикалей і діагоналей
    lines = [cells[:3], cells[3:6], cells[6:],  # горизонталі
             cells[0:9:3], cells[1:9:3], cells[2:9:3],  # вертикалі
             cells[0:9:4], cells[2:8:2]]  # діагоналі

    for line in lines:
        if all(symbol == "X" for symbol in line):
            return "X wins"
        elif all(symbol == "O" for symbol in line):
            return "O wins"

    # Перевірка на наявність порожніх комірок
    if " " in cells or "_" in cells:
        return "Game not finished"

    # Перевірка на нічию
    return "Draw"

def is_valid_coordinates(coordinates, cells):
    if not coordinates[0].isdigit() or not coordinates[1].isdigit():
        return False

    row, col = int(coordinates[0]), int(coordinates[1])

    if not (1 <= row <= 3) or not (1 <= col <= 3):
        return False

    index = (3 - row) * 3 + col - 1

    return cells[index] == " " or cells[index] == "_"

def play_game():
    # Початкове ігрове поле
    cells = [" " for _ in range(9)]

    # Виведення порожнього ігрового поля
    print_board(cells)

    # Ігровий цикл
    while True:
        # Хід гравця X
        while True:
            coordinates = input("Enter the coordinates for X (row column): ").split()

            if len(coordinates) != 2 or not is_valid_coordinates(coordinates, cells):
                print("Invalid coordinates! Try again.")
                continue

            row, col = int(coordinates[0]), int(coordinates[1])
            index = (3 - row) * 3 + col - 1

            if cells[index] == " " or cells[index] == "_":
                cells[index] = "X"
                break
            else:
                print("This cell is occupied! Choose another one!")

        # Виведення ігрового поля після ходу гравця X
        print_board(cells)

        # Аналіз стану гри
        game_state = check_winner(cells)
        if game_state != "Game not finished":
            print(game_state)
            break

        # Хід гравця O
        while True:
            coordinates = input("Enter the coordinates for O (row column): ").split()

            if len(coordinates) != 2 or not is_valid_coordinates(coordinates, cells):
                print("Invalid coordinates! Try again.")
                continue

            row, col = int(coordinates[0]), int(coordinates[1])
            index = (3 - row) * 3 + col - 1

            if cells[index] == " " or cells[index] == "_":
                cells[index] = "O"
                break
            else:
                print("This cell is occupied! Choose another one!")

        # Виведення ігрового поля після ходу гравця O
        print_board(cells)

        # Аналіз стану гри
        game_state = check_winner(cells)
        if game_state != "Game not finished":
            print(game_state)
            break

if __name__ == "__main__":
    play_game()