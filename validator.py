class Validator:
    def __init__(self, exercise: str):
        # the exercise to validate
        self.exercise = exercise
        # the valid chars
        self.valid_chars = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '(', ')', '.']
        # the operators with the same char before and after
        self.same_before_after = ['+', '*', '/', '^', '%', '$', '&', '@']
        # the operators with the different char before and after
        self.different_before_after = ['-', '~', '!']
        # brackets
        self.brackets = ['(', ')']
        # the operators
        self.operators = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!']

    def validate(self):
        """
        validate the exercise according to the rules at the bottom of the file
        :return: True if the exercise is valid, False otherwise
        """
        index = 1
        while self.exercise[index] != "\0":
            before = self.exercise[index - 1]
            after = self.exercise[index + 1]
            # check if the char is a valid char
            if self.exercise[index] not in self.valid_chars:
                return False
            # check if the char is a dot and the char before and after the dot is an operand
            if self.exercise[index] == ".":
                return self.is_operand(before) and self.is_operand(after)
            # calls the validate_same_before_after function if the char is in the same_before_after list
            if self.exercise[index] in self.same_before_after:
                self.validate_same_before_after(before, after)
            # calls the validate_different_before_after function if the char is in the different_before_after list
            if self.exercise[index] in self.different_before_after:
                self.validate_different_before_after(index, before, after)
            # calls the validate_brackets function if the char is a bracket
            if self.exercise[index] == "(" or self.exercise[index] == ")":
                self.validate_brackets(index, before, after)

    def validate_different_before_after(self, index: int, before: str, after: str) -> bool:
        """
        validate the exercise if the char is in the different_before_after list
        :param index: the index of the char
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # if the char is a factorial
        if self.exercise[index] == "!":
            return self.validate_factorial(before, after)
        # if the char is a minus
        if self.exercise[index] == "-":
            return self.validate_minus(before, after)
        # if the char is a tilda
        if self.exercise[index] == "~":
            return self.validate_tilda(before, after)
        # otherwise, the exercise is not valid
        return False

    def validate_tilda(self, before: str, after: str) -> bool:
        """
        validate the exercise if the char is a tilda
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before the index is an operator except factorial
        if self.is_operand(before) and before != "!" and before != "~":
            return True
        # check if the char after the index is an operand or a bracket or a minus
        if self.is_operand(after) or after == "(" or after == "-":
            return True
        return False

    def validate_factorial(self, before: str, after: str) -> bool:
        """
        validate the exercise if the char is a factorial
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before the index is an operand or a bracket or a factorial
        if self.is_operand(before) or before == ")" or before == "!":
            return True
        # check if the char after the index is an operator
        if self.is_operator(after):
            return True
        return False

    def validate_minus(self, before: str, after: str) -> bool:
        """
        validate the exercise if the char is a minus
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before the index is an operator or a bracket or a factorial or a minus
        if self.is_operand(before) or before == ")" or before == "!" or before == "-":
            return True
        # check if the char after the index is an operand or a bracket or a minus or a tilda
        if self.is_operand(after) or after == "(" or after == "-" or after == "~":
            return True
        return False

    def validate_brackets(self, index: int, before: str, after: str) -> bool:
        """
        validate the exercise if the char is a bracket
        :param index: the index of the char
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # if the char is an opening bracket
        if self.exercise[index] == "(":
            return self.validate_opening_bracket(before, after)
        # if the char is a closing bracket
        if self.exercise[index] == ")":
            return self.validate_closing_bracket(before, after)
        return False

    def validate_closing_bracket(self, before: str, after: str) -> bool:
        """
        validate the exercise if the char is a closing bracket
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before the index is an operand or a closing bracket or a factorial
        if self.is_operand(before) or before == ")" or before == "!":
            return True
        # check if the char after the index is in the valid chars list
        if after in self.valid_chars:
            return True
        return False

    def validate_opening_bracket(self, before: str, after: str) -> bool:
        """
        validate the exercise if the char is an opening bracket
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before the index is an operator or an opening bracket and not a factorial
        if (self.is_operator(before) and before != "!") or before == "(":
            return True
        # check if the char after the index is an operand or an opening bracket or a tilda
        if self.is_operand(after) or after == "(" or after == "~":
            return True
        return False

    def validate_same_before_after(self, before: str, after: str) -> bool:
        """
        validate the exercise if the char is in the same_before_after list
        and the char before and after the index is an operand or a bracket or a factorial
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before and after the index is an operand
        if self.is_operand(before) or self.is_operand(after):
            return True
        # check if the char before and after the index is a bracket
        if before == ")" and after == "(":
            return True
        # check if the char before and after the index is a factorial
        if before == "!":
            return True
        # otherwise, the exercise is not valid
        return False

    def is_operator(self, char: str) -> bool:
        """
        check if the char is an operator
        :param char: the char to check
        :return: True if the char is an operator, False otherwise
        """
        return char in self.operators

    def is_operand(self, string: str) -> bool:
        """
        check if the string is an operand
        :param string: the string to check
        :return: True if the string is an operand, False otherwise
        """
        return string.isnumeric()

# rules for the exercise:
# -----------------------
# addition: after: operand, (, -, ~ before: operand, ), factorial
# subtraction: after: operand, (, -, ~ before: -, operand, ), factorial
# multiplication: after: operand, (, -, ~ before: operand, ), factorial
# division: after: operand, (, -, ~ before: operand, ), factorial
# power: after: operand, (, -, ~ before: operand, ), factorial
# modulo: after: operand, (, -, ~ before: operand, ), factorial
# min: after: operand, (, -, ~ before: operand, ), factorial
# max: after: operand, (, -, ~ before: operand, ), factorial
# average: after: operand, (, -, ~ before: operand, ), factorial
# tilda: after: operand, (, - before: operator (except factorial and tilda)
# factorial: after: operator before: operand, factorial, )
# opening bracket: after: operand, (, ~ before: operator (except factorial), (
# closing bracket: after: every valid char before: ), operand, factorial
# dot: after: operand before: operand
