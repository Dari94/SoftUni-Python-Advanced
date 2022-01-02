from os import remove

while True:
    command = input().split("-")
    if command[0] == "End":
        break

    elif command[0] == "Create":
        file_name = command[1]
        with open(file_name, 'w') as file:
            file.write("")
    elif command[0] == "Add":
        file_name = command[1]
        content = command[2]
        with open(file_name, 'a') as file:
            file.write(content)
            file.write("\n")
    elif command[0] == "Replace":
        file_name = command[1]
        old_string = command[2]
        new_string = command[3]
        try:
            with open(file_name, 'r') as file:
                file_data = file.read()
            new_data = file_data.replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.write(new_data)

        except FileNotFoundError:
            print('An error occurred')
    elif command[0] == "Delete":
        file_name = command[1]
        try:
            remove(file_name)
        except FileNotFoundError:
            print('An error occurred')
