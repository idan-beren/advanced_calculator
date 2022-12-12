class Stack(object):
    def __init__(self):
        """Initializes the stack"""
        self.data = []

    def push(self, value):
        """
        Pushes a value onto the stack
        :param value: value to be pushed onto the stack
        """
        self.data.append(value)

    def pop(self):
        """
        Pops a value off the stack
        :return: value popped off the stack
        """
        return self.data.pop()

    def is_empty(self):
        """
        Checks if the stack is empty
        :return: True if the stack is empty, False otherwise
        """
        return len(self.data) == 0

    def peek(self):
        """
        Returns the value at the top of the stack
        :return: value at the top of the stack
        """
        return self.data[-1]
