def read_matrix():
    rows_count = int(input())
    return [map(int, input().split(', ')) for _ in range(rows_count)]
matrix = read_matrix()
flattened = []
for sublist in matrix:
    [flattened.append(x) for x in sublist]
   #  for num in sublist:
   #     flattened.append(num)

print(flattened)
print(matrix)
