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
    if name in contacts:
        raise ValueError(f"Contact {name} already exists.")
    else:
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
    command_functions = {
        "hello": lambda: print("How can I help you?"),
        "add": lambda name, phone: print(add_contact(name, phone)) if len(command) == 3 else print("Invalid command. Please try again."),
        "change": lambda name, new_phone: print(change_phone(name, new_phone)) if len(command) == 3 else print("Invalid command. Please try again."),
        "phone": lambda *args: print(get_phone(*args)) if len(args) == 1 else print("Invalid command. Please try again."),
        "show": lambda *args: print(show_all_contacts()) if len(args) == 1 and args[0] == "all" else print("Invalid command. Please try again."),
        "goodbye": lambda: print("Goodbye!") or exit(),
        "close": lambda: print("Goodbye!") or exit(),
        "exit": lambda: print("Goodbye!") or exit(),
        ".": lambda: print("Goodbye!") or exit(),
    }

    while True:
        command = input("Enter a command: ").lower().split()

        if not command:
            print("Invalid command. Please try again.")
            continue

        action = command[0]

        if action in command_functions:
            command_functions[action](*command[1:])
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()