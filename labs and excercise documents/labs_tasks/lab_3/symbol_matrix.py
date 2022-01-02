def find_symbol(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == symbol:
                return row, col

    return None


def find_symbol_list(words, symbol):
    for i in range(len(words)):
        word = words[i]
        if symbol in word:
            return i, word.index(symbol)
    return None


n = int(input())
matrix = [input() for _ in range(n)]
symbol = input()
result = find_symbol(matrix, symbol)
result_list = find_symbol_list(matrix, symbol)

if result:
    (row, col) = result
    print(f'({row}, {col})')
else:
    print(f'{symbol} does not occur in the matrix')

if result_list:
    (row, col) = result
    print(f'({row}, {col})')
else:
    print(f'{symbol} does not occur in the matrix')
