class Handler(object):
    """class to check if the exercise is valid and to handle the exercise"""
    def __init__(self, exercise):
        self.operators = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!']
        self.exercise = exercise + "\0"
        self.remove_spaces()

    def is_operator(self, char):
        """
        check if the char is an operator
        :param char: the char to check
        :return: True if the char is an operator, False otherwise
        """
        return char in self.operators

    def is_operand(self, string):
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
            if self.exercise[index] == " ":
                if self.is_operator(self.exercise[index - 1]) and self.is_operand(self.exercise[index + 1]):
                    self.erase_spaces(index)
                elif self.is_operand(self.exercise[index - 1]) and self.is_operator(self.exercise[index + 1]):
                    self.erase_spaces(index)
                elif self.exercise[index - 1] == " " or self.exercise[index + 1] == " ":
                    self.erase_spaces(index)
                else:
                    index += 1
            else:
                index += 1

    def erase_spaces(self, index):
        """erase the spaces from the exercise"""
        self.exercise = self.exercise[:index] + self.exercise[index + 1:]
