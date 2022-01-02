n = int(input())
longest_intersection = set()
best_length = 0
for _ in range(n):
    (part_1, part_2) = input().split('-')
    (start_1, end_1) = part_1.split(',')
    (start_2, end_2) = part_2.split(',')
    set_1 = set([int(x) for x in range(int(start_1), int(end_1) + 1)])
    set_2 = set([int(x) for x in range(int(start_2), int(end_2) + 1)])
    intersection = set_1.intersection(set_2)

    if len(intersection) > best_length:
        best_length = len(intersection)
        longest_intersection = intersection
converted = [str(x) for x in longest_intersection]
# print(f"Longest intersection is [{', '.join(converted)}] with length {len(longest_intersection)}")
print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
