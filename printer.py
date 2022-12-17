class Printer(object):
    """class to print the result"""
    def __init__(self, expression: list, result: float):
        self.expression = expression
        self.expression = "".join(self.expression)
        self.result = result

    def print_expression(self):
        """print the expression and the result"""
        print(f"Expression => Result: {self.expression} => {self.result}")
