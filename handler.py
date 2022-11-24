class Handler(object):
    """class to check if the exercise is valid and to handle the exercise"""
    def __init__(self, exercise: str):
        # list of the operators
        self.operators = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!']
        # the exercise to handle plus the end of string character
        self.exercise = exercise + "\0"
        # check if the exercise is valid
        self.is_valid()
        # remove spaces from the exercise
        self.remove_spaces()
        # print the exercise
        print(self.exercise[:-1])

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

    def remove_spaces(self):
        """remove spaces from the exercise if in one side is an operator and in the other side is an operand"""
        index = 1
        while self.exercise[index] != "\0":
            # if the char is a space
            if self.exercise[index] == " ":
                # if the char before the space is an operator and the char after the space is an operand
                if self.is_operator(self.exercise[index - 1]) and self.is_operand(self.exercise[index + 1]):
                    self.erase_spaces(index)
                # if the char before the space is an operand and the char after the space is an operator
                elif self.is_operand(self.exercise[index - 1]) and self.is_operator(self.exercise[index + 1]):
                    self.erase_spaces(index)
                # if the char before the space is a space and the char after the space is a space
                elif self.exercise[index - 1] == " " or self.exercise[index + 1] == " ":
                    self.erase_spaces(index)
                # if the char before the space is an opening bracket and the char after the space is a closing bracket
                elif self.exercise[index - 1] == "(" or self.exercise[index + 1] == ")":
                    self.erase_spaces(index)
                else:
                    index += 1
            else:
                index += 1

    def erase_spaces(self, index: int):
        """erase the spaces from the exercise"""
        self.exercise = self.exercise[:index] + self.exercise[index + 1:]

    def is_valid(self):
        """
        check if the exercise is valid
        :return: True if the exercise is valid, False otherwise
        """
        # check if the exercise is empty
        if self.exercise == '\0':
            raise ValueError("The exercise is empty!")
        # check if the exercise contains incorrect characters
        if self.incorrect_char() is False:
            raise ValueError("The exercise contains incorrect characters!")
        # check if the exercise contains only operators
        if self.only(self.is_operator) is True:
            raise ValueError("The exercise contains only operators!")
        # check if the exercise contains only operands
        if self.only(self.is_operand) is True:
            raise ValueError("The exercise contains only operands!")
        # check if the exercise contains an operator
        if self.contains(self.is_operator) is False:
            raise ValueError("The exercise contains no operator!")
        # check if the exercise contains an operand
        if self.contains(self.is_operand) is False:
            raise ValueError("The exercise contains no operand!")
        # check if the brackets are correct
        if self.correct_brackets() is False:
            raise ValueError("The brackets are incorrect!")
        # check if the exercise ends with an operator except the factorial operator
        if self.is_operator(self.exercise[-2]) and self.exercise[-2] != '!':
            raise ValueError("The exercise ends with an operator!")
        # check if the exercise starts with an operator except the minus and tilda operators
        if self.is_operator(self.exercise[0]) and self.exercise[0] != '-' and self.exercise[0] != '~':
            raise ValueError("The exercise starts with an operator!")
        # check if the exercise contains operators in a row except the minus operator
        if self.operators_in_a_row() is True:
            raise ValueError("The exercise contains operators in a row!")
        # check if the exercise contains an empty brackets
        if self.empty_brackets() is True:
            raise ValueError("The exercise contains an empty brackets!")

    def incorrect_char(self) -> bool:
        """
        check if the exercise contains incorrect characters
        :return: True if the exercise contains incorrect characters, False otherwise
        """
        for char in self.exercise[:-1]:
            # if the char is not a digit, a space, an operator or a bracket
            if (not self.is_operator(char)) and (not self.is_operand(char)) \
                    and char != '(' and char != ')' and char != ' ':
                return False
        return True

    def contains(self, function: callable) -> bool:
        """
        check if the exercise contains something
        :param function: the function to check
        :return: True if the exercise contains something, False otherwise
        """
        for char in self.exercise[:-1]:
            if function(char):
                return True
        return False

    def only(self, function: callable) -> bool:
        """
        check if the exercise contains only something
        :param function: the function to check
        :return: True if the exercise contains only something, False otherwise
        """
        for char in self.exercise[:-1]:
            if not function(char):
                return False
        return True

    def correct_brackets(self) -> bool:
        """
        check if the brackets are correct
        :return: True if the brackets are correct, False otherwise
        """
        brackets = []
        for char in self.exercise[:-1]:
            if char == '(':
                brackets.append(char)
            elif char == ')':
                if len(brackets) == 0:
                    return False
                brackets.pop()
        return len(brackets) == 0

    def operators_in_a_row(self) -> bool:
        """
        check if the exercise contains operators in a row except the minus operator
        :return: True if the exercise contains operators in a row except the minus operator, False otherwise
        """
        index = 0
        while self.exercise[index] != "\0":
            if self.is_operator(self.exercise[index]):
                if self.is_operator(self.exercise[index + 1]) and self.exercise[index + 1] != '-':
                    return True
            index += 1
        return False

    def empty_brackets(self) -> bool:
        """
        check if the exercise contains empty brackets
        :return: True if the exercise contains empty brackets, False otherwise
        """
        index = 0
        while self.exercise[index] != "\0":
            if self.exercise[index] == '(' and self.exercise[index + 1] == ')':
                return True
            index += 1
        return False
