def operate(operator, *numbers):
    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    def divide(*args):
        result = 1
        for x in args:
            result /= x
        return result

    def subtract(*args):
        result = 0
        for x in args:
            result -= x
        return result

    #  def get_initial_value(operator):
    #     if operator in ('+', '-'):
    #        return 0
    #     else:
    #        return 1
   # result = get_initial_value(operator)
    if operator == '+':
        return sum(numbers)
    elif operator == '*':
        return multiply(*numbers)
    elif operator == '/':
        return divide(*numbers)
    elif operator == '-':
        return subtract(*numbers)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
