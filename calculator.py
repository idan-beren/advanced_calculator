from scanner import *
from handler import *
from solver import *
from printer import *


class Calculator(object):
    def __init__(self):
        self.scanner = Scanner()
        self.handler = Handler(self.scanner.expression)
        self.solver = Solver(self.handler.expression)
        self.result = self.solver.solve()
        self.printer = Printer(self.result)
        self.printer.print_expression()
