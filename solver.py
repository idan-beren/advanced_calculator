from postfix import *


class Solver(object):
    """class to solve the expression"""
    def __init__(self, expression: list):
        self.expression = expression
        self.postfix = Postfix(self.expression)

    def solve(self):
        self.postfix.convert_infix_to_postfix()
        print(self.postfix.expression)
        print(self.postfix.solve_postfix())
