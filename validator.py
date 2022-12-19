from configuration import *


class Validator(object):
    """class to validate the expression"""
    def __init__(self, expression: list):
        """initializes the validator"""
        self.expression = expression

    def validate(self):
        """calls the methods that: checks if the expression is empty, validates the chars, the brackets order,
        the beginning and ending of the expression, right operators between minuses, and the whole expression"""
        self.empty_expression()
        self.validate_chars()
        self.validate_brackets_order()
        self.validate_start_end()
        self.validate_multy_right_operator()
        self.validate_expression()

    def empty_expression(self):
        """checks if the expression is empty and raise an error if it is"""
        if len(self.expression) == 0:
            raise SyntaxError("Empty expression")

    def validate_chars(self):
        """checks if the chars in the expression are valid"""
        index = 0
        while index < len(self.expression):
            self.is_valid_char(index)
            index += 1

    def is_valid_char(self, index: int):
        """checks if the char is valid
        :param index: the index of the char in the expression"""
        char = self.expression[index]
        if not (char in VALID_CHARS or char.isdigit()):
            self.raising_error(index)

    def before_after(self, index: int) -> tuple:
        """returns the char before and after the given index
        :param index: the index of the char in the expression
        :return: the char before and after the given index"""
        return self.expression[index - 1], self.expression[index + 1]

    def validate_expression(self):
        """checks if the expression is valid by calling the validate methods of every kind of char"""
        index = 1
        while index < len(self.expression) - 1:
            before, after = self.before_after(index)
            item = self.expression[index]
            if item in OPENING_BRACKETS + CLOSING_BRACKETS:
                self.validate_brackets(index, before, after)
            elif item == MINUS:
                self.validate_minus(before, after, index)
            elif item in OPERATORS:
                self.validate_operators(index, before, after)
            elif item.isdigit():
                self.validate_operands(before, after, index)
            elif item == DOT:
                self.validate_dots(before, after, index)
            index += 1

    def validate_brackets(self, index: int, before: str, after: str):
        """calls the right method to validate the brackets according to the type of the bracket
        :param index: the index of the bracket in the expression
        :param before: the char before the bracket
        :param after: the char after the bracket"""
        if self.expression[index] in OPENING_BRACKETS:
            self.validate_opening_bracket(before, after, index)
        elif self.expression[index] in CLOSING_BRACKETS:
            self.validate_closing_bracket(before, after, index)

    def validate_opening_bracket(self, before: str, after: str, index: int):
        """validates the position of the opening brackets
        :param before: the char before the bracket
        :param after: the char after the bracket
        :param index: the index of the bracket in the expression"""
        if not (((before in OPERATORS and self.operand_side(before) != LEFT) or before in OPENING_BRACKETS) and
                (after.isdigit() or after in OPENING_BRACKETS or self.operand_side(after) == RIGHT or after == MINUS
                    or after == DOT)):
            self.raising_error(index)

    def validate_closing_bracket(self, before: str, after: str, index: int):
        """validates the position of the closing brackets
        :param before: the char before the bracket
        :param after: the char after the bracket
        :param index: the index of the bracket in the expression"""
        if not ((before.isdigit() or before in CLOSING_BRACKETS or self.operand_side(before) == LEFT or before == DOT)
                and ((after in OPERATORS and self.operand_side(after) != RIGHT) or after in CLOSING_BRACKETS)):
            self.raising_error(index)

    def validate_minus(self, before: str, after: str, index: int):
        """validates the position of the minus sign
        :param before: the char before the minus sign
        :param after: the char after the minus sign
        :param index: the index of the minus sign in the expression"""
        if not ((before.isdigit() or before in CLOSING_BRACKETS + OPENING_BRACKETS or before in OPERATORS
                or before == DOT) and (after.isdigit() or after in OPENING_BRACKETS or after == MINUS
                or self.operand_side(after) == RIGHT or after == DOT)):
            self.raising_error(index)

    def validate_operators(self, index: int, before: str, after: str):
        """calls the right method to validate the operators according to the type of the operator
        :param index: the index of the operator in the expression
        :param before: the char before the operator
        :param after: the char after the operator"""
        item = self.expression[index]
        if OPERAND_SIDE[item] == LEFT:
            self.validate_left_operator(before, after, index)
        elif OPERAND_SIDE[item] == RIGHT:
            self.validate_right_operator(before, after, index)
        elif OPERAND_SIDE[item] == BOTH:
            self.validate_both_operator(before, after, index)

    def validate_left_operator(self, before: str, after: str, index: int):
        """"validates the position of the left operators
        :param before: the char before the operator
        :param after: the char after the operator
        :param index: the index of the operator in the expression"""
        if not ((before.isdigit() or before in CLOSING_BRACKETS or self.operand_side(before) == LEFT or before == DOT)
                and ((after in OPERATORS and self.operand_side(after) != RIGHT) or after in CLOSING_BRACKETS)):
            self.raising_error(index)

    def validate_right_operator(self, before: str, after: str, index: int):
        """validates the position of the right operators
        :param before: the char before the operator
        :param after: the char after the operator
        :param index: the index of the operator in the expression"""
        if not (((before in OPERATORS and self.operand_side(before) == BOTH) or before in OPENING_BRACKETS) and
                (after.isdigit() or after in OPENING_BRACKETS or after == MINUS or after == DOT)):
            self.raising_error(index)

    def validate_both_operator(self, before: str, after: str, index: int):
        """validates the position of the both operators
        :param before: the char before the operator
        :param after: the char after the operator
        :param index: the index of the operator in the expression"""
        if not ((before in CLOSING_BRACKETS or self.operand_side(before) == LEFT or before.isdigit() or before == DOT)
                and (after in OPENING_BRACKETS or after.isdigit() or after == MINUS
                or self.operand_side(after) == RIGHT or after == DOT)):
            self.raising_error(index)

    def validate_operands(self, before: str, after: str, index: int):
        """validates the position of the operands
        :param before: the char before the operand
        :param after: the char after the operand
        :param index: the index of the operand in the expression"""
        if (before in CLOSING_BRACKETS or after in OPENING_BRACKETS) or \
                (self.operand_side(before) == LEFT or self.operand_side(after) == RIGHT):
            self.raising_error(index)

    def validate_dots(self, before: str, after: str, index: int):
        """validates the position of the dots
        :param before: the char before the dot
        :param after: the char after the dot
        :param index: the index of the dot in the expression"""
        if (before == DOT or before in CLOSING_BRACKETS or self.operand_side(before) == LEFT) \
                or (after == DOT or after in OPENING_BRACKETS or self.operand_side(after) == RIGHT):
            self.raising_error(index)

    @staticmethod
    def operand_side(operator: str) -> str:
        """
        returns the side of the operand of the given operator
        :param operator: the operator
        :return: the side of the operand
        """
        if operator in OPERATORS:
            return OPERAND_SIDE[operator]
        return NONE

    def validate_start_end(self):
        """checks if the expression contains at least one digit, starts and ends with valid chars,
        if not raise an error"""
        if not self.contain_digit():
            raise SyntaxError("The expression must contain at least one digit")
        start = self.expression[0]
        if not (start is MINUS or start is OPENING_BRACKET or start is DOT or start.isdigit()
                or self.operand_side(start) == RIGHT):
            raise SyntaxError(f"Invalid start of expression: {start}")
        end = self.expression[-1]
        if not (end is CLOSING_BRACKET or end.isdigit() or end is DOT or self.operand_side(end) == LEFT):
            raise SyntaxError(f"Invalid end of expression: {end}")

    def contain_digit(self) -> bool:
        """
        checks if the expression contain at least one digit
        :return: True if the expression contain at least one digit, False otherwise
        """
        for char in self.expression:
            if char.isdigit():
                return True
        return False

    def validate_brackets_order(self):
        """checks if the brackets are in the right order, and if there are no extra brackets.
        and raise an error if it needed"""
        brackets = []
        for char in self.expression:
            if char == OPENING_BRACKET:
                brackets.append(char)
            elif char == CLOSING_BRACKET:
                if len(brackets) == 0:
                    raise SyntaxError("Invalid brackets order")
                brackets.pop()
        if len(brackets) != 0:
            raise SyntaxError("Invalid brackets order")

    def raising_error(self, index: int):
        """raises an error with the index of the invalid char
        :param index: the index of the invalid char"""
        raise SyntaxError(f"Invalid position of the char {self.expression[index]} at index {index}")

    def validate_multy_right_operator(self):
        """checks if there are two right operators in a row between minuses, and raise an error if it needed"""
        index = 0
        while index < len(self.expression):
            if self.operand_side(self.expression[index]) == RIGHT:
                index += 1
                while index < len(self.expression) and not \
                        (self.expression[index].isdigit() or self.expression[index] == DOT
                         or self.expression[index] == OPENING_BRACKET):
                    if self.operand_side(self.expression[index]) == RIGHT:
                        self.raising_error(index)
                    index += 1
            index += 1
