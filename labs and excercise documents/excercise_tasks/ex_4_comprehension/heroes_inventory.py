heroes = {name: {} for name in input().split(', ')}
command = input()

while command != 'End':
    (name, item,third) = command.split('-')
    cost = int(third)
    if item not in heroes[name]:
        heroes[name][item] = cost

    command = input()

[print(f"{name} -> Items: {len(heroes[name])}, Cost: {sum(heroes[name].values())}") for name in heroes]