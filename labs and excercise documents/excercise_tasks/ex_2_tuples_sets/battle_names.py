def input_to_list(lines_count):
    return [input() for _ in range(lines_count)]


def get_name_value(name):
    name_value = sum([ord(ch) for ch in name])
    return name_value


names = input_to_list(int(input()))

name_values = [get_name_value(names[i-1])//i for i in range(1, len(names)+1)]

even_set = set([value for value in name_values if value % 2 == 0])
odd_set = set([value for value in name_values if value % 2 != 0])

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if even_sum == odd_sum:
    union_values = even_set.union(odd_set)
    print(', '.join([str(x) for x in union_values]))
elif odd_sum > even_sum:
    different_values = odd_set.difference(even_set)
    print(', '.join([str(x) for x in different_values]))
elif even_sum > odd_sum:
    symmetric_dif_values = odd_set.symmetric_difference(even_set)
    print(', '.join([str(x) for x in symmetric_dif_values]))
