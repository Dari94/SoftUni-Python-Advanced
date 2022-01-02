def reverse_num(text):

    reverse_nums = []

    for n in range(len(text)):

        reverse_nums.append(text.pop())
    return ' '.join(reverse_nums)


numbers = input().split()
print(reverse_num(numbers))

