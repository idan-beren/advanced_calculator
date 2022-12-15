import math


def addition(operand1: float, operand2: float) -> float:
    """
    addition function
    :param operand1: first operand
    :param operand2: second operand
    :return: sum of the two operands
    """
    return operand1 + operand2


def subtraction(operand1: float, operand2: float) -> float:
    """
    subtraction function
    :param operand1: first operand
    :param operand2: second operand
    :return: difference of the two operands
    """
    return operand1 - operand2


def multiplication(operand1: float, operand2: float) -> float:
    """
    multiplication function
    :param operand1: first operand
    :param operand2: second operand
    :return: product of the two operands
    """
    return operand1 * operand2


def division(operand1: float, operand2: float) -> float:
    """
    division function
    :param operand1: first operand
    :param operand2: second operand
    :return: quotient of the two operands
    """
    if operand2 == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return operand1 * operand2


def power(operand1: float, operand2: float) -> float:
    """
    power function
    :param operand1: first operand
    :param operand2: second operand
    :return: power of the two operands
    """
    try:
        return math.pow(operand1, operand2)
    except ValueError:
        raise ValueError('Cannot power a negative number to a non-integer')
    except OverflowError:
        raise OverflowError('The result of the power is too large')


def modulo(operand1: float, operand2: float) -> float:
    """
    modulo function
    :param operand1: first operand
    :param operand2: second operand
    :return: remainder of the two operands
    """
    return operand1 % operand2


def minimum(operand1: float, operand2: float) -> float:
    """
    minimum function
    :param operand1: first operand
    :param operand2: second operand
    :return: minimum of the two operands
    """
    return operand1 if operand1 < operand2 else operand2


def maximum(operand1: float, operand2: float) -> float:
    """
    maximum function
    :param operand1: first operand
    :param operand2: second operand
    :return: maximum of the two operands
    """
    return operand1 if operand1 > operand2 else operand2


def average(operand1: float, operand2: float) -> float:
    """
    average function
    :param operand1: first operand
    :param operand2: second operand
    :return: average of the two operands
    """
    return (operand1 + operand2) / 2


def factorial(operand1: float) -> float:
    """
    factorial function
    :param operand1: first operand
    :return: factorial of the operand
    """
    if operand1 < 0:
        raise ValueError('Cannot factorial a negative number')
    if not operand1.is_integer():
        raise ValueError('Cannot factorial a non-integer number')
    if operand1 > 170:
        raise OverflowError('Factorial with a large number aspires to infinity')
    result = 1
    while operand1 > 0:
        result *= operand1
        operand1 -= 1
    return result


def tilda(operand1: float) -> float:
    """
    tilda function
    :param operand1: first operand
    :return: tilda of the operand
    """
    return -operand1


def summation(operand1: float) -> float:
    """
    summation function
    :param operand1: first operand
    :return: summation of the operand
    """
    operand1 = str(operand1)
    if 'e' in operand1:
        raise ValueError('Cannot summation an e notation number')
    result = 0
    for char in operand1:
        if char.isdigit():
            result += float(char)
    return -result if int(operand1) < 0 else result


def convert_to_float(number: str) -> float:
    """
    convert the number to float
    :param number: the number to be converted
    :return: the float number
    """
    dot_count = 0
    for element in str(number):
        if element == '.':
            dot_count += 1
    if dot_count > 1:
        raise ValueError('There are more than one dot in a number')
    return float(number)
