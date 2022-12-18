from scanner import *
from handler import *
from solver import *
from printer import *


class Calculator(object):
    def __init__(self):
        """initializes the calculator"""
        print("Welcome to the calculator! Please enter the expression you want to solve. or type 'exit' to quit.")
        while True:
            self.calculate()

    @staticmethod
    def calculate():
        """calling the methods to handle, validate, solve and print the expression"""
        scanner = Scanner()
        try:
            handler = Handler(scanner.expression)
        except SyntaxError as error:
            print(error)
            return
        solver = Solver(handler.expression)
        result = solver.solve()
        if result is not None:
            printer = Printer(handler.raw_expression, result)
            printer.print_expression()
