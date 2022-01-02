phone_book = {}


def print_names(n):
    for _ in range(n):
        name = input()
        if name in phone_book:
            print(f'{name} -> {phone_book[name]}')
        else:
            print(f"Contact {name} does not exist.")


while True:
    command = input()

    if len(command) == 1:
        n = int(command)
        print_names(n)
        break

    name, phone_number = command.split('-')
    phone_book[name] = phone_number
