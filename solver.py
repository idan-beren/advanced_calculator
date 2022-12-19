from postfix import *


class Solver(object):
    """class to solve the expression by using the postfix class"""
    def __init__(self, expression: list):
        """initializes the solver"""
        self.expression = expression
        self.postfix = Postfix(self.expression)
        self.postfix.convert_infix_to_postfix()

    def solve(self) -> float:
        """calls the solve_postfix method that calculates the result
        :return: the result of the expression
        """
        try:
            return self.postfix.solve_postfix()
        except ValueError as error:
            print(error)
        except OverflowError as error:
            print(error)
        except ZeroDivisionError as error:
            print(error)
