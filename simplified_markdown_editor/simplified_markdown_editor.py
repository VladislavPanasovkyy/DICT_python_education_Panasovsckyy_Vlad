def display_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list line-break")
    print("Special commands: !help !done")


def get_list_input():
    while True:
        try:
            num_rows = int(input("Number of rows: > "))
            if num_rows > 0:
                break
            else:
                print("The number of rows should be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    rows = []
    for i in range(1, num_rows + 1):
        row_input = input(f"Row #{i}: > ")
        rows.append(row_input)

    return rows


def save_to_file(text):
    with open("output.md", "w") as file:
        file.write(text)


def main():
    formatted_text = ""

    while True:
        user_input = input("Choose a formatter: > ")

        if user_input == "!help":
            display_help()
        elif user_input == "!done":
            save_to_file(formatted_text)
            break
        elif user_input in ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list",
                            "unordered-list", "line-break"]:
            if user_input == "plain":
                text_input = input("Text: > ")
                formatted_text += f"{text_input}\n"
            elif user_input == "header":
                level = int(input("Level: > "))
                if 1 <= level <= 6:
                    text_input = input("Text: > ")
                    formatted_text += f"{'#' * level} {text_input}\n"
                else:
                    print("The level should be within the range of 1 to 6.")
            elif user_input == "link":
                label_input = input("Label: > ")
                url_input = input("URL: > ")
                formatted_text += f"[{label_input}]({url_input})\n"
            elif user_input == "line-break":
                formatted_text += "\n"
            elif user_input == "ordered-list" or user_input == "unordered-list":
                rows = get_list_input()
                if user_input == "ordered-list":
                    for i, row in enumerate(rows, start=1):
                        formatted_text += f"{i}. {row}\n"
                elif user_input == "unordered-list":
                    for row in rows:
                        formatted_text += f"* {row}\n"

            print(formatted_text)
        else:
            print("Unknown formatting type or command")

    print("Your formatted text:")
    print(formatted_text)


if __name__ == "__main__":
    main()
