def read_matrix():
    rows_count = int(input())
    #return [list(map(int, input().split())) for _ in range(rows_count)]
    return [[int(x)
    for x in input().split(' ')]
    for _ in range(rows_count)]


def is_valid(i,j, n):
    return 0 <= i < n and 0 <= j < n


matrix = read_matrix()


n = len(matrix)
while True:
    tokens = input().split()
    if tokens[0] == "END":
        break
    command = tokens[0]
    i,j,value = list(map(int, tokens[1:]))
    if is_valid(i,j,n):
        if command == 'Add':
            matrix[i][j] += value
        elif command == 'Subtract':
            matrix[i][j] -= value
    else:
        print("Invalid coordinates")


[print(" ".join(map(str, row))) for row in matrix]

