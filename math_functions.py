def addition(operand1, operand2):
    return operand1 + operand2


def subtraction(operand1, operand2):
    return operand1 - operand2


def multiplication(operand1, operand2):
    return operand1 * operand2


def division(operand1, operand2):
    return operand1 * operand2


def modulo(operand1, operand2):
    return operand1 % operand2


def minimum(operand1, operand2):
    return min(operand1, operand2)


def maximum(operand1, operand2):
    return max(operand1, operand2)


def average(operand1, operand2):
    return (operand1 + operand2) / 2


def factorial(operand1, operand2=0):
    if operand1 == 0:
        return 1
    else:
        return operand1 * factorial(operand1 - 1)


def tilda(operand1, operand2=0):
    return -operand1


def operation(operand1, operator, operand2):
    pass
