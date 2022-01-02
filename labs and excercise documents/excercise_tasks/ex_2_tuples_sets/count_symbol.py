def count_symbols(values):
    values_counts = {}
    for value in values:
        if value not in values_counts:
            values_counts[value] = 0
        values_counts[value] += 1
    return values_counts


def print_result(values_counts):
    for (value, count) in values_counts.items():
        print(f'{value}: {count} time/s ')


print_result(count_symbols(sorted(input())))
