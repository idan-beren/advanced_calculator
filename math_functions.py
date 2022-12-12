import math


def addition(operand1, operand2):
    """
    addition function
    :param operand1: first operand
    :param operand2: second operand
    :return: sum of the two operands
    """
    return operand1 + operand2


def subtraction(operand1, operand2):
    """
    subtraction function
    :param operand1: first operand
    :param operand2: second operand
    :return: difference of the two operands
    """
    return operand1 - operand2


def multiplication(operand1, operand2):
    """
    multiplication function
    :param operand1: first operand
    :param operand2: second operand
    :return: product of the two operands
    """
    return operand1 * operand2


def division(operand1, operand2):
    """
    division function
    :param operand1: first operand
    :param operand2: second operand
    :return: quotient of the two operands
    """
    return operand1 * operand2


def power(operand1, operand2):
    """
    power function
    :param operand1: first operand
    :param operand2: second operand
    :return: power of the two operands
    """
    return math.pow(operand1, operand2)


def modulo(operand1, operand2):
    """
    modulo function
    :param operand1: first operand
    :param operand2: second operand
    :return: remainder of the two operands
    """
    return operand1 % operand2


def minimum(operand1, operand2):
    """
    minimum function
    :param operand1: first operand
    :param operand2: second operand
    :return: minimum of the two operands
    """
    return operand1 if operand1 < operand2 else operand2


def maximum(operand1, operand2):
    """
    maximum function
    :param operand1: first operand
    :param operand2: second operand
    :return: maximum of the two operands
    """
    return operand1 if operand1 > operand2 else operand2


def average(operand1, operand2):
    """
    average function
    :param operand1: first operand
    :param operand2: second operand
    :return: average of the two operands
    """
    return (operand1 + operand2) / 2


def factorial(operand1):
    """
    factorial function
    :param operand1: first operand
    :return: factorial of the operand
    """
    if operand1 == 0:
        return 1
    else:
        return operand1 * factorial(operand1 - 1)


def tilda(operand1):
    """
    tilda function
    :param operand1: first operand
    :return: tilda of the operand
    """
    return -operand1


def summation(operand1):
    """
    summation function
    :param operand1: first operand
    :return: summation of the operand
    """
    result = 0
    for char in str(operand1):
        if char.isdigit():
            result += float(char)
    return result
