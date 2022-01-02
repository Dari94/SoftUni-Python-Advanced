def positive_sum():
    # positive = sum([x for x in numbers if x >= 0])
    positive = sum(filter(lambda x: x > 0, numbers))

    return positive


def negative_sum():
    # negative = sum([x for x in numbers if x < 0])
    negative = sum(filter(lambda x: x < 0, numbers))

    return negative


def bigger(negative_sum, positive_sum):
    if abs(negative_sum) > abs(positive_sum):
        return "The negatives are stronger than the positives"
    elif abs(negative_sum) < abs(positive_sum):
        return "The positives are stronger than the negatives"


# numbers = list(map(int,input().split(' ')))
numbers = [int(x) for x in input().split(' ')]

print(negative_sum())
print(positive_sum())
print(bigger(negative_sum(), positive_sum()))
