import random
def split_expenses():
    # Зчитуємо кількість друзів
    num_friends = int(input("Enter the number of friends joining (including you):\n"))

    # Перевіряємо коректність кількості друзів
    if num_friends <= 0:
        print("No one is joining for the party")
        return

    # Ініціалізуємо словник іменами друзів та присвоюємо їм значення 0
    friends_dict = {}
    for _ in range(num_friends):
        friend_name = input("Enter the name of every friend (including you), each on a new line:\n")
        friends_dict[friend_name] = 0

    # Зчитуємо загальну суму
    total_amount = float(input("Enter the total amount:\n"))

    # Запитуємо користувача про випадковий вибір "щасливчика"
    choose_lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")

    if choose_lucky.lower() == "yes":
        lucky_one = random.choice(list(friends_dict.keys()))
        print(f"{lucky_one} is the lucky one!")

        # Розподіляємо витрати порівну між усіма, крім "щасливчика"
        if num_friends > 1:
            per_person_share = round(total_amount / (num_friends - 1), 2)
            for friend in friends_dict:
                if friend != lucky_one:
                    friends_dict[friend] = per_person_share
    else:
        # Розподіляємо витрати порівну між усіма
        if num_friends > 0:
            per_person_share = round(total_amount / num_friends, 2)
            friends_dict = {k: per_person_share for k in friends_dict}

    # Оновлюємо значення у словнику та виводимо оновлений словник
    print(friends_dict)

# Викликаємо функцію
split_expenses()
