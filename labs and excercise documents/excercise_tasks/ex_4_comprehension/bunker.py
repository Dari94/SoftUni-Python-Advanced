bunker = {category: {} for category in input().split(', ')}
number = int(input())

for _ in range(number):
    tokens = input().split(' - ')
    category = tokens[0]
    item = tokens[1]
    quantity_and_quality = tokens[2].split(";")
    quantity = int(quantity_and_quality[0].split(':')[1])
    quality = int(quantity_and_quality[1].split(':')[1])
    bunker[category][item] = (quantity, quality)
    #bunker[category].update({item: [quantity, quality]})

#count_items = sum([sum([x[0] for x in list(bunker[category].values())]) for category in bunker])
#avg_value = sum([sum([x[1] for x in list(bunker[category].values())]) for category in bunker]) / (len(bunker))
count_items = sum([v[0] for item in bunker.values() for v in item.values()])
print(f'Count of items: {count_items}')
avg_value = sum([v[1] for item in bunker.values() for v in item.values()])/ len(bunker.values())
print(f'Average quality: {avg_value:.2f}')
[print(f'{category} -> {", ".join([item for item in items])}') for category, items in bunker.items()]