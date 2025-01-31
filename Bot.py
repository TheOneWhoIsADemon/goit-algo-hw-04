def parse_input(user_input):
    """Розбиває введений рядок на команду та її аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Приведення до нижнього регістру
    return cmd, *args

def add_contact(args, contacts):
    """Додає новий контакт у словник."""
    if len(args) != 2:
        return "Invalid command. Please provide both name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""
    if len(args) != 2:
        return "Invalid command. Please provide both name and new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return f"Contact with name {name} not found."

def show_phone(args, contacts):
    """Виводить номер телефону за ім'ям."""
    if len(args) != 1:
        return "Invalid command. Please provide a name."
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number: {contacts[name]}"
    return f"Contact with name {name} not found."

def show_all(contacts):
    """Виводить всі контакти та номери телефонів."""
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return "No contacts saved."

def main():
    contacts = {}  # Словник для збереження контактів
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
