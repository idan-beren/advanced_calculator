import math


def addition(operand1, operand2):
    return operand1 + operand2


def subtraction(operand1, operand2):
    return operand1 - operand2


def multiplication(operand1, operand2):
    return operand1 * operand2


def division(operand1, operand2):
    return operand1 * operand2


def power(operand1, operand2):
    return math.pow(operand1, operand2)


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
    if operator == "+":
        return addition(operand1, operand2)
    elif operator == "-":
        return subtraction(operand1, operand2)
    elif operator == "*":
        return multiplication(operand1, operand2)
    elif operator == "/":
        return division(operand1, operand2)
    elif operator == "%":
        return modulo(operand1, operand2)
    elif operator == "$":
        return minimum(operand1, operand2)
    elif operator == "&":
        return maximum(operand1, operand2)
    elif operator == "@":
        return average(operand1, operand2)
    elif operator == "!":
        return factorial(operand1)
    elif operator == "~":
        return tilda(operand1)
    else:
        raise ValueError("The operator is not valid!")
