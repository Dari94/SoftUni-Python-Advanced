

def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]


(rows_count, columns_count) = read_int_list_from_input(', ')
matrix = []
for _ in range(rows_count):
    matrix.append(read_int_list_from_input())

columns_sum = [0] * columns_count

for row in range(rows_count):
    for column in range(columns_count):
        columns_sum[column] += matrix[row][column]
[print(int(x)) for x in columns_sum]
