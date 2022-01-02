def read_matrix():
    rows_count = int(input())
    return [list(map(int, input().split(', '))) for _ in range(rows_count)]


def diagonals(matrix):

    rows_count = len(matrix)
    primary_diagonal = [matrix[i][i] for i in range(rows_count)]
    second_diagonal = [matrix[i][rows_count - i - 1] for i in range(rows_count)]
    print(f'First diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
    print(f'Second diagonal: {", ".join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}')


matrix = read_matrix()

diagonals(matrix)