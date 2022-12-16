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
        self.validate.expression = self.expression
        self.validate.validate_expression()
        self.merge_operands()
        print(self.expression)
        self.handle_minuses()

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

    def count_minuses(self, index: int) -> int:
        """count the minuses after the given index and return the count
        :param index: index of the minus
        :return: count of the minuses
        """
        count = 0
        while index < len(self.expression) and self.expression[index] == MINUS:
            count += 1
            index += 1
        return count

    def delete_minuses(self, index1: int, index2: int):
        """remove the minuses from the expression between the given indexes (not inclusive)"""
        del self.expression[index1:index2]

    def handle_minuses(self):
        """handle the minuses, iterate through the expression, and call the appropriate function
        to remove or replace the minuses"""
        index = 0
        while index < len(self.expression):
            count = 0
            if self.expression[index] == MINUS:
                count = self.count_minuses(index)
            if index == 0:
                self.operator_before(index, count)
            elif self.is_number(self.expression[index - 1]) or self.expression[index - 1] == DOT or \
                    self.expression[index - 1] == CLOSING_BRACKET \
                    or self.validate.operand_side(self.expression[index - 1]) == LEFT:
                self.operand_before(index, count)
            else:
                self.operator_before(index, count)
            index += 1

    def operand_before(self, index: int, count: int):
        """if before the minuses there is an operand, then replace the minuses. if the count is odd replace with minus,
        if the count is even replace with plus"""
        if count % 2 == 0 and count != 0:
            self.expression[index] = PLUS
            self.delete_minuses(index + 1, index + count)
        elif count % 2 != 0:
            self.expression[index] = MINUS
            self.delete_minuses(index + 1, index + count)

    def operator_before(self, index: int, count: int):
        """if before the minuses there is an operator, then replace the minuses. if the count is odd
        stick a minus to the next operand, if the count is even remove the minuses"""
        if count % 2 == 0 and count != 0:
            self.delete_minuses(index, index + count)
        elif count % 2 != 0:
            if self.is_number(self.expression[index + count]):
                self.expression[index + count] = MINUS + self.expression[index + count]
                self.delete_minuses(index, index + count)
            elif self.validate.operand_side(self.expression[index + count]) == RIGHT \
                    or self.expression[index + count] == OPENING_BRACKET:
                self.expression.insert(index + count, "-1")
                self.expression.insert(index + count + 1, "*")
                self.delete_minuses(index, index + count)

    @staticmethod
    def is_number(item: str) -> bool:
        """check if the item is a number
        :param item: item to check
        :return: True if the item is a number, False otherwise
        """
        try:
            float(item)
            return True
        except ValueError:
            return False
