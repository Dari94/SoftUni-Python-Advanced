n = int(input())
odd_set = set()
even_set = set()

for i in range(1,n+1):
    name = input()
    summed = sum([ord(ch) for ch in name])//i
    if summed % 2 == 0:
        even_set.add(summed)
    else:
        odd_set.add(summed)

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