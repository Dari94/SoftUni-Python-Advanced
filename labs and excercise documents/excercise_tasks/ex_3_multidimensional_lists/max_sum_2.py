import sys


def read_matrix():
    (rows_count, columns_count) = [int(x) for x in input().split()]
    matrix = []
    for _ in range(rows_count):
        line = [int(x) for x in input().split()]
        matrix.append(line)
    return matrix


def get_submatrix_sum(matrix, row, col, size):
    the_sum = 0
    for r in range(row, row + size):
        for c in range(col, col + size):
            the_sum += matrix[r][c]
    return the_sum


def print_summatrix(matrix, row, col, size):
    for r in range(row, row + size):
        for c in range(col, col + size):
            print(matrix[r][c], end=' ')
        print()


size = 3
matrix = read_matrix()
best_position = None
best_value = -sys.maxsize - 1

for row in range(len(matrix) - size + 1):
    for col in range(len(matrix[row]) - size + 1):
        current_value = get_submatrix_sum(matrix, row, col, size)
        if best_value < current_value:
            best_value = current_value
            best_position = (row, col)

print(f'Sum = {best_value}')
(best_row, best_col) = best_position
print_summatrix(matrix, best_row, best_col, size)
