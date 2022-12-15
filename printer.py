class Printer(object):
    """class to print the result"""
    def __init__(self, result: float):
        self.result = result

    def print_expression(self):
        print(self.result)
