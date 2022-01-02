def round_the_list (values):
    return [round(x) for x in values]


print(round_the_list(map(float,input().split(' '))))