def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]


def calculate_primary_diagonal_sum(matrix):
    primary_diagonal_sum = 0
    for i in range(len(matrix)):
        primary_diagonal_sum += matrix[i][i]
    return primary_diagonal_sum


def calculate_secondary_diagonal_sum(matrix):
    secondary_diagonal_sum = 0
    for i in range(len(matrix)):
        secondary_diagonal_sum += matrix[i][n-i-1]
    return secondary_diagonal_sum


def calculate_below_primary_diagonal_sum(matrix):
    the_sum = 0
    for row in range(len(matrix)):
        for col in range(row + 1):
            the_sum += matrix[row][col]
    return the_sum


def calculate_below_secondary_diagonal_sum(matrix):
    the_sum = 0
    for row in range(len(matrix)):
        # r=0, c= n-1
        # r=1, c= n-2
        for col in range(len(matrix) - row - 1, len(matrix)):
            the_sum += matrix[row][col]
    return the_sum


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(read_int_list_from_input(' '))

print(calculate_primary_diagonal_sum(matrix))
print(calculate_secondary_diagonal_sum(matrix))
print(calculate_below_primary_diagonal_sum(matrix))
print(calculate_below_secondary_diagonal_sum(matrix))
