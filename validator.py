from configuration import *


class Validator(object):
    def __init__(self, expression: list):
        self.expression = expression

    def validate(self):
        """check if the expression is valid"""
        self.vlidate_chars()

    def vlidate_chars(self):
        """check if the chars are valid"""
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

    def raising_error(self, index: int):
        raise ValueError(f"Invalid char {self.expression[index]} at index {index}")
