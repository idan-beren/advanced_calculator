from configuration import *


class Validator(object):
    """class to validate the expression"""
    def __init__(self, expression: list):
        self.expression = expression

    def validate(self):
        """validate the chars, the brackets order, and the beginning and ending of the expression."""
        self.vlidate_chars()
        self.validate_brackets_order()
        self.validate_start_end()

    def vlidate_chars(self):
        """check if the chars in the expression are valid"""
        index = 0
        while index < len(self.expression):
            self.is_valid_char(index)
            index += 1

    def is_valid_char(self, index: int):
        """check if the char is valid"""
        char = self.expression[index]
        if not (char in VALID_CHARS or char.isdigit()):
            self.raising_error(index)

    def before_after(self, index: int):
        """return the char before and after the given index"""
        return self.expression[index - 1], self.expression[index + 1]

    def validate_expression(self):
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
        if self.expression[index] in OPENING_BRACKETS:
            self.validate_opening_bracket(before, after, index)
        elif self.expression[index] in CLOSING_BRACKETS:
            self.validate_closing_bracket(before, after, index)

    def validate_opening_bracket(self, before: str, after: str, index: int):
        if (before in OPERATORS and self.check_operand_side(before) != LEFT) or before in OPENING_BRACKETS:
            if after.isdigit() or after in OPENING_BRACKETS or self.check_operand_side(after) == RIGHT or after == MINUS:
                return
        self.raising_error(index)

    def validate_closing_bracket(self, before: str, after: str, index: int):
        if before.isdigit() or before in CLOSING_BRACKETS or self.check_operand_side(before) == LEFT:
            if (after in OPERATORS and self.check_operand_side(after) != RIGHT) or after in CLOSING_BRACKETS:
                return
        self.raising_error(index)

    def validate_minus(self, before: str, after: str, index: int):
        if before.isdigit() or before in CLOSING_BRACKETS + OPENING_BRACKETS or before in OPERATORS or before == DOT:
            if after.isdigit() or after in OPENING_BRACKETS or after == MINUS or self.check_operand_side(after) == RIGHT or after == DOT:
                return
        self.raising_error(index)
        # TODO: fixing the minuses validation.

    def validate_operators(self, index: int, before: str, after: str):
        item = self.expression[index]
        if OPERAND_SIDE[item] == LEFT:
            self.validate_left_operator(before, after, index)
        elif OPERAND_SIDE[item] == RIGHT:
            self.validate_right_operator(before, after, index)
        elif OPERAND_SIDE[item] == BOTH:
            self.validate_both_operator(before, after, index)

    def validate_left_operator(self, before: str, after: str, index: int):
        if before.isdigit() or before in CLOSING_BRACKETS or self.check_operand_side(before) == LEFT:
            if (after in OPERATORS and self.check_operand_side(after) != RIGHT) or after in CLOSING_BRACKETS:
                return
        self.raising_error(index)

    def validate_right_operator(self, before: str, after: str, index: int):
        if (before in OPERATORS and self.check_operand_side(before) != RIGHT and self.check_operand_side(before) != LEFT) or before in OPENING_BRACKETS:
            if after.isdigit() or after in OPENING_BRACKETS or after == MINUS:
                return
        self.raising_error(index)

    def validate_both_operator(self, before: str, after: str, index: int):
        if before in CLOSING_BRACKETS or self.check_operand_side(before) == LEFT or before.isdigit() or before == DOT:
            if after in OPENING_BRACKETS or after.isdigit() or after == MINUS or self.check_operand_side(after) == RIGHT or after == DOT:
                return
        self.raising_error(index)

    def validate_operands(self, before: str, after: str, index: int):
        if before in CLOSING_BRACKETS or after in OPENING_BRACKETS:
            self.raising_error(index)
        if self.check_operand_side(before) == LEFT or self.check_operand_side(after) == RIGHT:
            self.raising_error(index)

    def validate_dots(self, before: str, after: str, index: int):
        if not before.isdigit() and before != DOT and not after.isdigit() and after != DOT:
            self.raising_error(index)

    def check_operand_side(self, operator: str) -> str:
        if operator in OPERATORS:
            return OPERAND_SIDE[operator]
        return NONE

    def validate_start_end(self):
        """check if the expression contains at least one digit, start and end with valid chars, if not raise an error"""
        if not self.contain_digit():
            raise ValueError("The expression must contain at least one digit")
        char = self.expression[0]
        if char is MINUS or char is OPENING_BRACKET or char is DOT or char.isdigit() or self.check_operand_side(char) == RIGHT:
            char = self.expression[-1]
            if char is CLOSING_BRACKET or char.isdigit() or char is DOT or self.check_operand_side(char) == LEFT:
                return
        raise ValueError("the char at the start or end of the expression is invalid")

    def contain_digit(self) -> bool:
        """
        check if the expression contain at least one digit
        :return: True if the expression contain at least one digit, False otherwise
        """
        for char in self.expression:
            if char.isdigit():
                return True
        return False

    def validate_brackets_order(self):
        """check if the brackets are in the right order, and if there are no extra brackets.
        and raise an error if it needed"""
        brackets = []
        for char in self.expression:
            if char == OPENING_BRACKET:
                brackets.append(char)
            elif char == CLOSING_BRACKET:
                if len(brackets) == 0:
                    raise ValueError("Invalid brackets order")
                brackets.pop()
        if len(brackets) != 0:
            raise ValueError("Invalid brackets order")

    def raising_error(self, index: int):
        raise ValueError(f"Invalid char {self.expression[index]} at index {index}")
