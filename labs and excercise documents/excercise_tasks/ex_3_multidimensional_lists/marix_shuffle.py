def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]


def read_char_list_from_input(separator=' '):
    return [x for x in input().split(separator)]


def is_valid(pos, rows, cols):
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols


def print_matrix(matrix_):
    matrix = matrix_
    for i in matrix:
        print(" ".join(map(str, i)))


(rows_count, col_count) = read_int_list_from_input(' ')
matrix = [read_char_list_from_input(' ') for _ in range(rows_count)]

command = input()
while command != 'END':
    command = command.split(' ')
    if command[0] == 'swap' and len(command) == 5:
        first_elem_pos = [int(command[1]), int(command[2])]
        sec_elem_pos = [int(command[3]), int(command[4])]
        if is_valid(first_elem_pos, rows_count, col_count) and is_valid(sec_elem_pos, rows_count, col_count):

            matrix[first_elem_pos[0]][first_elem_pos[1]], matrix[sec_elem_pos[0]][sec_elem_pos[1]] = \
                matrix[sec_elem_pos[0]][sec_elem_pos[1]], matrix[first_elem_pos[0]][first_elem_pos[1]]
            print_matrix(matrix)
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input()
