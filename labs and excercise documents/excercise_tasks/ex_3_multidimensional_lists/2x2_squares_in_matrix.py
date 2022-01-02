def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]


def red_char_list_from_input(separator=' '):
    return [x for x in input().split(separator)]


def is_equal_square(indexes, matrix):
    i, j = indexes
    return matrix[i][j] == matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1]


(rows_count, col_count) = read_int_list_from_input(' ')
matrix = [red_char_list_from_input(' ') for _ in range(rows_count)]

count = 0
for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        if is_equal_square((row, col), matrix):
            count += 1
print(count)
