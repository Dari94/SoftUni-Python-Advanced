def flatten_lists(list_of_lists):
    result = [el for row in list_of_lists for el in row]
    print(" ".join(result))


lists = input().split('|')[::-1]
list_of_lists = [el.strip().split() for el in lists]
flatten_lists(list_of_lists)
print(list_of_lists)