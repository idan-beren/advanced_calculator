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

    def validate(self) -> bool:
        """
        validate the exercise according to the rules at the bottom of the file
        :return: True if the exercise is valid, False otherwise
        """
        index = 1
        while self.exercise[index + 1] != "\0":
            before = self.exercise[index - 1]
            after = self.exercise[index + 1]
            # check if the char is a valid char or an operand
            char = self.exercise[index]
            if (char not in self.valid_chars) and (not self.is_operand(char)):
                return False
            # check if the char is a dot and the char before and after the dot is an operand
            if char == ".":
                if not (self.is_operand(before) and self.is_operand(after)):
                    return False
            # calls the validate_same_before_after function if the char is in the same_before_after list
            if char in self.same_before_after:
                if not self.validate_same_before_after(before, after):
                    return False
            # calls the validate_different_before_after function if the char is in the different_before_after list
            if char in self.different_before_after:
                if not self.validate_different_before_after(index, before, after):
                    return False
            # calls the validate_brackets function if the char is a bracket
            if char in self.brackets:
                if not self.validate_brackets(index, before, after):
                    return False
            # calls the validate_operand function if the char is an operand
            if self.is_operand(char):
                if not self.validate_operand(before, after):
                    return False
            index += 1
        return True

    def validate_operand(self, before: str, after: str) -> bool:
        """
        validate the exercise if the char is an operand
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char after the index is an opening bracket or a tilda
        if after == "(" or after == "~":
            return False
        # check if the char before the index is a closing bracket or a factorial
        if before == ")" or before == "!":
            return False
        return True

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

    def validate_tilda(self, before: str, after: str) -> bool:
        # tilda: after: operand, (, - before: operator (except factorial and tilda)
        """
        validate the exercise if the char is a tilda
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before the index is an operator except factorial and tilda
        if self.is_operator(before) and before != "!" and before != "~":
            # check if the char after the index is an operand or a bracket or a minus
            if self.is_operand(after) or after == "(" or after == "-":
                return True
        return False

    def validate_factorial(self, before: str, after: str) -> bool:
        # factorial: after: operator (except tilda) before: operand, factorial, )
        """
        validate the exercise if the char is a factorial
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before the index is an operand or a closing bracket or a factorial
        if self.is_operand(before) or before == ")" or before == "!":
            # check if the char after the index is an operator except tilda
            if self.is_operator(after) and after != '~':
                return True
        return False

    def validate_minus(self, before: str, after: str) -> bool:
        # subtraction: after: operand, (, -, ~ before: operand, operator, (, )
        """
        validate the exercise if the char is a minus
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before the index is an operator or a bracket or an operand
        if self.is_operand(before) or before in self.brackets or self.is_operator(before):
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

    def validate_closing_bracket(self, before: str, after: str) -> bool:
        # closing bracket: after: operator (except tilda), ) before: ), operand, factorial
        """
        validate the exercise if the char is a closing bracket
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before the index is an operand or a closing bracket or a factorial
        if self.is_operand(before) or before == ")" or before == "!":
            # check if the char after the index is an operator (except tilda) or a closing bracket
            if (self.is_operator(after) and after != "~") or after == ")":
                return True
        return False

    def validate_opening_bracket(self, before: str, after: str) -> bool:
        # opening bracket: after: operand, (, ~, - before: operator (except factorial), (
        """
        validate the exercise if the char is an opening bracket
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before the index is an operator (except factorial) or an opening bracket
        if (self.is_operator(before) and before != "!") or before == "(":
            # check if the char after the index is an operand or an opening bracket or a tilda or a minus
            if self.is_operand(after) or after == "(" or after == "~" or after == "-":
                return True
        return False

    def validate_same_before_after(self, before: str, after: str) -> bool:
        # same_before_after: after: operand, (, -, ~ before: operand,), factorial
        """
        validate the exercise if the char is in the same_before_after list
        and the char before and after the index is an operand or a bracket or a factorial
        :param before: the char before the index
        :param after: the char after the index
        :return: True if the exercise is valid, False otherwise
        """
        # check if the char before the index is an operand or a closing bracket or a factorial
        if before == ")" or before == "!" or self.is_operand(before):
            # check if the char after the index is an operand or an opening bracket or minus or tilda
            if after == "(" or self.is_operand(after) or after == '-' or after == '~':
                return True
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

# rules of validation: (V) - means valid
# -----------------------
# (V) addition: after: operand, (, -, ~ before: operand, ), factorial
# (V) subtraction: after: operand, (, -, ~ before: operand, operator, (, )
# (V) multiplication: after: operand, (, -, ~ before: operand, ), factorial
# (V) division: after: operand, (, -, ~ before: operand, ), factorial
# (V) power: after: operand, (, -, ~ before: operand, ), factorial
# (V) modulo: after: operand, (, -, ~ before: operand, ), factorial
# (V) min: after: operand, (, -, ~ before: operand, ), factorial
# (V) max: after: operand, (, -, ~ before: operand, ), factorial
# (V) average: after: operand, (, -, ~ before: operand, ), factorial
# (V) tilda: after: operand, (, - before: operator (except factorial and tilda)
# (V) factorial: after: operator (except tilda) before: operand, factorial, )
# (V) opening bracket: after: operand, (, ~, - before: operator (except factorial), (
# (V) closing bracket: after: operator (except tilda), ) before: ), operand, factorial
# (V) dot: after: operand before: operand
# (V) operand: after: operand, ), operator (except tilda), dot before: operand, (, operator (except factorial), dot
