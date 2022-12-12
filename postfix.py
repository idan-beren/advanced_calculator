from stack import *
from configuration import *


class Postfix(object):
    def __init__(self, expression: list):
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

    def solve_postfix(self):
        stack = Stack()
        for element in self.expression:
            if element not in OPERATORS:
                stack.push(element)
            else:
                result = 0
                if OPERAND_SIDE[element] == RIGHT or OPERAND_SIDE[element] == LEFT:
                    operand1 = float(stack.pop())
                    result = OPERATOR_FUNCTION[element](operand1)
                elif OPERAND_SIDE[element] == BOTH:
                    operand1 = float(stack.pop())
                    operand2 = float(stack.pop())
                    result = OPERATOR_FUNCTION[element](operand2, operand1)
                stack.push(result)
        return stack.pop()
        # TODO: (-2)$4
