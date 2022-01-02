def even():
    even_sum = sum(filter(lambda x: x % 2 == 0, numbers))
    # even_sum = sum([x for x in numbers if x % 2 == 0])

    return even_sum * len(numbers)


def odd():
    odd_sum = sum(filter(lambda x: x % 2 == 1, numbers))
    # odd_sum = sum([x for x in numbers if x % 2 != 0])

    return odd_sum * len(numbers)


def even_odd(command):
    if command == 'Odd':
        return (odd())
    elif command == 'Even':
        return (even())


command = input()
numbers = list(map(int, input().split()))
# numbers = [int(x) for x in input().split(' ')]

print(even_odd(command))
