from collections import deque


def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]


(rows_count, cols_count) = read_int_list_from_input(' ')
snake = deque(input())
matrix = []
for row in range(rows_count):
    matrix.append([])
    for col in range(cols_count):
        matrix[row].append("")

for row in range(rows_count):
    for col in range(cols_count):
        current_col = col
        current_char = snake.popleft()
        if row % 2 != 0:
            current_col = cols_count - 1 - col
        matrix[row][current_col] = current_char
        snake.append(current_char)

for row in matrix:
    print(''.join(row))