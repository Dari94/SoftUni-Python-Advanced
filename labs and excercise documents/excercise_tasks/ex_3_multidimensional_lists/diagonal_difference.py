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


n = int(input())
matrix = [read_int_list_from_input(' ') for _ in range(n)]

difference = abs(calculate_primary_diagonal_sum(matrix) - calculate_secondary_diagonal_sum(matrix))
print(difference)
