def recursive_power(number, power):
    if number == 0:
        return 1
    if power == 0:
        return number
    return number ** power


print(recursive_power(2, 10))
print(recursive_power(10, 100))
