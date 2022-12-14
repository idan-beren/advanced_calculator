from validator import *
from configuration import *


class Handler(object):
    """class to check if the expression is valid and to handle the expression"""
    def __init__(self, expression: str):
        self.expression = list(expression)
        self.remove_spaces()
        self.empty_expression()
        self.validate = Validator(self.expression)
        self.validate.validate()
        # TODO: handle minuses
        self.validate.expression = self.expression
        self.validate.validate_expression()
        self.merge_operands()
        print(self.expression)

    def empty_expression(self):
        """check if the expression is empty and raise an error if it is"""
        if len(self.expression) == 0:
            raise ValueError("Empty expression")

    def remove_spaces(self):
        """remove spaces and tabs from the whole expression"""
        self.expression = [index for index in self.expression if index not in [SPACE, TAB]]

    def merge_operands(self):
        """merge the operands, stick digits and dots together to the same item in the list"""
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
