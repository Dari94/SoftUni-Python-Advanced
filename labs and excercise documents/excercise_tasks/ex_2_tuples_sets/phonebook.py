
line = input().split('-')
phone_book = {}
while len(line) != 1:
    p_name = line[0]
    number = line[1]
    phone_book[p_name] = number
    line = input().split('-')

n = (int(line[0]))

for _ in range(n):
    name = input()
    if name in phone_book:
        print(f'{name} -> {phone_book[name]}')
    else:
        print(f'Contact {name} does not exist.')