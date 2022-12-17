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
        self.merge_operands()
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
        """count of the minuses in a row starting from the given index (inclusive)
        :param index: index of the first minus
        :return: count of the minuses in a row
        """
        count = 0
        while index < len(self.expression) and self.expression[index] == MINUS:
            count += 1
            index += 1
        return count

    def delete_minuses(self, index1: int, index2: int):
        """remove the minuses from the expression between the given indexes (not inclusive)
        :param index1: index of the first minus
        :param index2: index of the last minus"""
        del self.expression[index1:index2]

    def operand_before(self, index: int, count: int):
        """handle the minuses before an operand, if the count is even, replace the minuses with a plus,
            if the count is odd, replace the minuses with a minus
            :param index: index of the first minus
            :param count: count of the minuses in a row"""
        if count % 2 == 0 and count != 0:
            self.expression[index] = PLUS
        elif count % 2 != 0:
            self.expression[index] = MINUS
        self.delete_minuses(index + 1, index + count)

    def operator_before(self, index: int, count: int):
        """handle the minuses before an operator, remove the minuses
        if the count is odd: the next operand needs to change sign
        :param index: index of the first minus
        :param count: count of the minuses in a row"""
        self.delete_minuses(index, index + count)
        if count % 2 != 0:
            if self.is_number(self.expression[index]):
                self.expression[index] = MINUS + self.expression[index]
            elif self.expression[index] == OPENING_BRACKET:
                self.expression.insert(index, "*")
                self.expression.insert(index, "-1")
                self.expression.insert(index, OPENING_BRACKET)
                closing_index = self.find_matching_closing_brackets(index + 3)
                self.expression.insert(closing_index, CLOSING_BRACKET)
            elif self.validate.operand_side(self.expression[index]) == RIGHT:
                if self.expression[index - 1] == PLUS:
                    self.expression[index - 1] = MINUS
                else:
                    self.expression.insert(index + 1, MINUS)

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
            elif self.is_number(self.expression[index - 1]) or self.expression[index - 1] == CLOSING_BRACKET\
                    or self.validate.operand_side(self.expression[index - 1]) == LEFT:
                self.operand_before(index, count)
            else:
                self.operator_before(index, count)
            index += 1

    def find_matching_closing_brackets(self, index: int) -> int:
        """find the matching closing bracket for the opening bracket in the given index
        :param index: index of the opening bracket
        :return: index of the matching closing bracket
        """
        count = 1
        while count != 0:
            index += 1
            if self.expression[index] == OPENING_BRACKET:
                count += 1
            elif self.expression[index] == CLOSING_BRACKET:
                count -= 1
        return index

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
