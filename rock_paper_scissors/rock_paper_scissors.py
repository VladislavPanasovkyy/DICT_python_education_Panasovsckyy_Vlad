import random

def get_computer_choice(options):
    return random.choice(options)

def determine_winner(user_choice, computer_choice, options_relations):
    if user_choice == computer_choice:
        return "draw", computer_choice
    elif computer_choice in options_relations[user_choice]:
        return "win", computer_choice
    else:
        return "lose", computer_choice

def update_rating(ratings, user_name, result):
    user_rating = int(ratings.get(user_name, 0))
    if result == "draw":
        ratings[user_name] = str(user_rating + 50)
    elif result == "win":
        ratings[user_name] = str(user_rating + 100)

def save_ratings(ratings):
    with open("rating.txt", "w") as file:
        for user, rating in ratings.items():
            file.write(f"{user} {rating}\n")

def load_ratings():
    try:
        with open("rating.txt", "r") as file:
            ratings = dict(line.strip().split() for line in file)
    except FileNotFoundError:
        ratings = {}

    return ratings

def play_game():
    user_name = input("Enter your name: ").strip()
    print(f"Hello, {user_name}")

    ratings = load_ratings()

    user_options_input = input("Enter options (separated by commas), or press Enter for default options (Paper, Scissors, Rock, Snake, Dragon, Gan, Air): ")
    user_options = user_options_input.split(",") if user_options_input else ['Paper', 'Scissors', 'Rock', 'Snake', 'Dragon', 'Gan', 'Air']

    options_relations = {
        'Paper': ['Rock', 'Gan', 'Air', 'Dragon'],
        'Scissors': ['Paper', 'Snake', 'Air'],
        'Rock': ['Scissors', 'Snake'],
        'Snake': ['Air', 'Paper'],
        'Dragon': ['Snake', 'Rock', 'Gan'],
        'Gan': ['Snake', 'Scissors', 'Rock'],
        'Air': ['Rock', 'Gan', 'Dragon']
    }

    print("Okay, let's start.")

    while True:
        user_choice = input(f"Enter your choice ({', '.join(user_options)}), !rating, or type !exit to quit: ").capitalize()

        if user_choice == "!exit":
            print("Bye!")
            break
        elif user_choice == "!rating":
            print(f"Your rating: {ratings.get(user_name, 0)}")
        elif user_choice in user_options:
            computer_choice = get_computer_choice(user_options)
            result, computer_choice_text = determine_winner(user_choice, computer_choice, options_relations)

            print(f"The computer chose {computer_choice}")
            print(f"You {result}. The computer chose {computer_choice_text}.")

            update_rating(ratings, user_name, result)
            save_ratings(ratings)
        else:
            print("Invalid input. Please enter a valid option !rating or type !exit.")

if __name__ == "__main__":
    play_game()

