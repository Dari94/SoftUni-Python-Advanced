names = input().split(', ')
names_dict = {name : len(name) for name in names}


print(', '.join([f'{name} -> {length}' for name,length in names_dict.items()]))

