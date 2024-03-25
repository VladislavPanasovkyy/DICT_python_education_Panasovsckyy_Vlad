import requests

# Словник для зберігання кешу обмінних курсів
exchange_cache = {}


def get_exchange_rate(currency_code):
    if currency_code in exchange_cache:
        print("Checking the cache...")
        return exchange_cache[currency_code]
    else:
        print("Retrieving data from FloatRates...")
        url = f"http://www.floatrates.com/daily/{currency_code}.json"
        response = requests.get(url)
        data = response.json()
        exchange_cache[currency_code] = data
        return data


def convert_currency(from_currency, to_currency, amount):
    data = get_exchange_rate(from_currency)

    if to_currency.lower() in data:
        rate = data[to_currency.lower()]['rate']
        converted_amount = amount * rate
        print(f"You received {converted_amount:.2f} {to_currency.upper()}.")
    else:
        print("Sorry, but it is not in the cache!")


def main():
    from_currency = input("Enter the currency code you have: ").strip().upper()
    amount = input("Enter the amount you have: ")

    # Перевірка чи введене значення є числом
    while not amount.replace('.', '', 1).isdigit():
        print("Please enter a valid number.")
        amount = input("Enter the amount you have: ")
    amount = float(amount)

    while True:
        to_currency = input(
            "Enter the currency code you want to convert to (or press Enter to finish): ").strip().upper()
        if not to_currency:
            break
        convert_currency(from_currency, to_currency, amount)


if __name__ == "__main__":
    main()
