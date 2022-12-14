class Printer(object):
    """class to print the result of the expression"""
    def __init__(self, expression: list, result: float):
        """initializes the printer"""
        self.expression = expression
        self.expression = "".join(self.expression)
        self.result = result

    def print_expression(self):
        """prints the expression and the result"""
        print(f"Expression => Result: {self.expression} => {self.result}")
