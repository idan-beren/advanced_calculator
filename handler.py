from validator import *
from configuration import *


class Handler(object):
    """class to check if the expression is valid and to handle the expression"""
    def __init__(self, expression: str):
        self.expression = list(expression)
        self.validate = Validator(self.expression)
        self.validate.validate()
        self.remove_spaces()
        self.empty_expression()
        self.validate.expression = self.expression
        self.validate.validate_expression()
        self.merge_operands()
        print(self.expression)

    def before_after(self, index: int):
        """return the char before and after the given index"""
        return self.expression[index - 1], self.expression[index + 1]

    def empty_expression(self):
        """check if the expression is empty"""
        if len(self.expression) == 0:
            raise ValueError("Empty expression")

    def remove_spaces(self):
        """remove spaces from the expression"""
        index = 1
        while index < len(self.expression) - 1:
            before, after = self.before_after(index)
            if self.expression[index] == SPACE:
                if not (before.isdigit() and after.isdigit()):
                    del self.expression[index]
                else:
                    raise ValueError("Invalid expression")
            else:
                index += 1
        self.expression = [index for index in self.expression if index != SPACE]

    def merge_operands(self):
        new_expression = [""]
        index = 0
        while index < len(self.expression):
            if self.expression[index].isdigit() or self.expression[index] == DOT:
                new_expression[-1] += self.expression[index]
            else:
                new_expression.append(self.expression[index])
                new_expression.append("")
            index += 1
        new_expression = list(filter(lambda x: x != "", new_expression))
        self.expression = new_expression
