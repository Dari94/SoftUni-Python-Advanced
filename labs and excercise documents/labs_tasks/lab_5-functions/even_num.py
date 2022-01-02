#def even_numbers(values):
  #  return [x for x in values if x % 2 == 0]


#print(even_numbers(map(int,input().split(' '))))

#************************


def is_even(x):
    return x % 2 == 0


numbers = [int(x) for x in input().split(' ')]
print(list(filter(is_even,numbers)))
#print([x for x in numbers if x % 2 == 0])