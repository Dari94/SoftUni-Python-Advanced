from P1.line import print_line


def print_triangle(n):
    [print_line(1, x + 1) for x in range(n)]
    [print_line(1, x) for x in range(n - 2, 0, -1)]


print_triangle(4)
