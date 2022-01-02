from fibonacci.sequence import locate,create_sequence

while True:
    command = input().split(" ")
    if command[0] == "Stop":
        break
    elif command[0] == "Create":
        num = int(command[2])
        create_sequence(num)
    elif command[0] == "Locate":
        locate(int(command[1]))