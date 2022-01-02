
def is_number_valid(number):
    return len([True for d in range(2,11) if number % d == 0]) > 0


start = int(input())
end = int(input())
list_1  = [x for x in range(start, end +1)
         if any ([x % d ==0 for d in range(2,11)])]

list_2 = [x for x in range(start, end +1)
        if len([True for d in range(2,11) if x % d == 0]) >0]

list_3 = [x for x in range(start,end +1) if is_number_valid(x)]
print(list_1)
print(list_2)
print(list_3)
