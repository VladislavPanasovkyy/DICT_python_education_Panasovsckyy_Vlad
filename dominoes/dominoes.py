import random


class DominoGame:
    def __init__(self):
        self.stock = []
        self.computer_pieces = []
        self.player_pieces = []
        self.snake = []

    def start_game(self):
        self.create_stock()
        self.deal_pieces()
        self.set_initial_snake()
        self.play_game()

    def create_stock(self):
        for i in range(7):
            for j in range(i, 7):
                self.stock.append([i, j])

    def deal_pieces(self):
        random.shuffle(self.stock)
        self.computer_pieces = self.stock[:7]
        self.player_pieces = self.stock[7:14]
        self.stock = self.stock[14:]

    def set_initial_snake(self):
        max_double = max(self.computer_pieces + self.player_pieces, key=lambda x: sum(x))
        self.snake.append(max_double)
        if max_double in self.computer_pieces:
            self.computer_pieces.remove(max_double)
        else:
            self.player_pieces.remove(max_double)

    def display_snake(self):
        print("Domino snake:", end=" ")
        for piece in self.snake:
            print(f"[{piece[0]}, {piece[1]}]", end="")
        print()

    def display_status(self, player):
        if player == "computer":
            print("Computer pieces:", end=" ")
            for idx, piece in enumerate(self.computer_pieces):
                print(f"{idx + 1}:[{piece[0]}, {piece[1]}] ", end="")
            print()
        elif player == "player":
            print("Your pieces:", end=" ")
            for idx, piece in enumerate(self.player_pieces):
                print(f"{idx + 1}:[{piece[0]}, {piece[1]}] ", end="")
            print()
        print("Status:", end=" ")
        if len(self.stock) > 0:
            print("Game in progress...")
        else:
            print("Game over! No more pieces left.")

    def play_game(self):
        while True:
            self.display_snake()
            self.display_status("player")
            player_has_move = self.check_possible_move(self.player_pieces)
            if not player_has_move:
                print("No possible move. You lose!")
                break
            move = input("Enter your command: ")
            if move.isdigit() and 0 < int(move) <= len(self.player_pieces):
                piece = self.player_pieces[int(move) - 1]
                if self.is_valid_move(piece):
                    self.player_pieces.remove(piece)
                    if piece[0] == self.snake[0][0]:
                        self.snake.insert(0, piece[::-1])
                    elif piece[1] == self.snake[0][0]:
                        self.snake.insert(0, piece)
                    elif piece[0] == self.snake[-1][1]:
                        self.snake.append(piece)
                    elif piece[1] == self.snake[-1][1]:
                        self.snake.append(piece[::-1])
                    if len(self.player_pieces) == 0:
                        print("You won! Congratulations!")
                        break
                    computer_has_move = self.check_possible_move(self.computer_pieces)
                    if not computer_has_move:
                        print("No possible move. You win!")
                        break
                    self.play_computer_turn()
                else:
                    print("Illegal move. Please try again.")
            else:
                print("Invalid input. Please enter the number of the piece you want to play.")

    def is_valid_move(self, piece):
        if piece[0] in [self.snake[0][0], self.snake[-1][1]] or \
                piece[1] in [self.snake[0][0], self.snake[-1][1]]:
            return True
        return False

    def check_possible_move(self, pieces):
        for piece in pieces:
            if self.is_valid_move(piece):
                return True
        return False

    def play_computer_turn(self):
        print("=" * 60)
        print("Stock size:", len(self.stock))
        print("Computer pieces:", len(self.computer_pieces))
        self.display_snake()
        self.display_status("computer")
        input("Press Enter to continue...")
        computer_has_move = self.check_possible_move(self.computer_pieces)
        if not computer_has_move:
            print("No possible move. You win!")
            return
        possible_moves = []

        # Створення словника для підрахунку кількості чисел на кістках
        counts = {i: 0 for i in range(7)}
        for piece in self.snake + self.computer_pieces:
            counts[piece[0]] += 1
            counts[piece[1]] += 1

        # Розрахунок оцінок для кожної кістки
        for piece in self.computer_pieces:
            score = counts[piece[0]] + counts[piece[1]]
            possible_moves.append((piece, score))

        # Сортування кісточок за оцінками
        possible_moves.sort(key=lambda x: x[1], reverse=True)

        # Пошук найбільш вигідної кістки, яку можна застосувати
        for move in possible_moves:
            piece, _ = move
            if piece[0] == self.snake[0][0]:
                self.snake.insert(0, piece[::-1])
                self.computer_pieces.remove(piece)
                print("Computer placed a piece.")
                break
            elif piece[1] == self.snake[0][0]:
                self.snake.insert(0, piece)
                self.computer_pieces.remove(piece)
                print("Computer placed a piece.")
                break
            elif piece[0] == self.snake[-1][1]:
                self.snake.append(piece)
                self.computer_pieces.remove(piece)
                print("Computer placed a piece.")
                break
            elif piece[1] == self.snake[-1][1]:
                self.snake.append(piece[::-1])
                self.computer_pieces.remove(piece)

                print("Computer placed a piece.")
                break
        else:
            if len(self.stock) > 0:
                print("Computer drew a piece from the stock.")
                self.computer_pieces.append(self.stock.pop())
            else:
                print("Computer passes.")
        input("Press Enter to continue...")

# Запуск гри
game = DominoGame()
game.start_game()
