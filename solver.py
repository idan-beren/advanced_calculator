from postfix import *


class Solver(object):
    """class to solve the expression"""
    def __init__(self, expression: list):
        self.expression = expression
        self.postfix = Postfix(self.expression)
        self.postfix.convert_infix_to_postfix()
        print(self.expression)

    def solve(self) -> float:
        try:
            return self.postfix.solve_postfix()
        except ValueError as error:
            print(error)
        except OverflowError as error:
            print(error)
        except ZeroDivisionError as error:
            print(error)
