from stack import *
from configuration import *
from math_functions import *


class Postfix(object):
    """class to convert the expression to a postfix expression and then solve it"""
    def __init__(self, expression: list):
        """initializes the postfix class"""
        self.expression = expression

    def convert_infix_to_postfix(self):
        """convert the infix expression to postfix expression"""
        stack = Stack()
        result = []
        for element in self.expression:
            if element not in OPERATORS + OPENING_BRACKETS + CLOSING_BRACKETS:
                result.append(element)
            elif element in OPENING_BRACKETS:
                stack.push(OPENING_BRACKETS[0])
            elif element in CLOSING_BRACKETS:
                while not stack.is_empty() and stack.peek() not in OPENING_BRACKETS:
                    result.append(stack.pop())
                stack.pop()
            else:
                while not stack.is_empty() and stack.peek() not in OPENING_BRACKETS and \
                        OPERATOR_PRIORITY[element] <= OPERATOR_PRIORITY[stack.peek()]:
                    result.append(stack.pop())
                stack.push(element)
        while not stack.is_empty():
            result.append(stack.pop())
        self.expression = result

    def solve_postfix(self) -> float:
        """
        solve the postfix expression
        :return: the result of the expression
        """
        stack = Stack()
        for element in self.expression:
            if element not in OPERATORS:
                stack.push(element)
            else:
                result = 0
                if OPERAND_SIDE[element] == RIGHT or OPERAND_SIDE[element] == LEFT:
                    operand1 = convert_to_float(stack.pop())
                    result = OPERATOR_FUNCTION[element](operand1)
                elif OPERAND_SIDE[element] == BOTH:
                    operand1 = convert_to_float(stack.pop())
                    operand2 = convert_to_float(stack.pop())
                    result = OPERATOR_FUNCTION[element](operand2, operand1)
                stack.push(result)
        return convert_to_float(stack.pop())
