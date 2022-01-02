
def matrix_1 (row):
    return [f"{chr(row)}{chr(row+col)}{chr(row)}" for col in range(columns)]

#(rows,columns) =map(int, input().split(' '))
rows, columns = [int(x) for x in input().split(' ')]

matrix = [matrix_1(row) for row in range(97, 97 + rows)]

# matrix = [[f"{chr(row)}{chr(row+col)}{chr(row)}" for col in range(columns)] for row in range(97, 97 + row)]

#for row in matrix:
#    print(" ".join(row))

[print(' '.join(row)) for row in matrix]