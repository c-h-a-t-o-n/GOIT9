def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Error: Contact not found - {str(e)}"
        except ValueError as e:
            return f"Error: Invalid input - {str(e)}"
        except IndexError as e:
            return f"Error: Index error - {str(e)}"
    return wrapper


contacts = {}

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} added successfully."

@input_error
def change_phone(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} updated successfully."
    else:
        raise KeyError(name)

@input_error
def get_phone(name):
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."
    else:
        raise KeyError(name)

@input_error
def show_all_contacts():
    if contacts:
        result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return result
    else:
        return "No contacts found."


def main():
    while True:
        command = input("Enter a command: ").lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            _, name, phone = command.split()
            print(add_contact(name, phone))
        elif command.startswith("change"):
            _, name, new_phone = command.split()
            print(change_phone(name, new_phone))
        elif command.startswith("phone"):
            _, name = command.split()
            print(get_phone(name))
        elif command == "show all":
            print(show_all_contacts())
        elif command in ["good bye", "close", "exit", "."]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()