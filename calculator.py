from scanner import *
from handler import *
from solver import *


class Calculator(object):
    def __init__(self):
        self.scanner = Scanner()
        self.handler = Handler(self.scanner.expression)
        self.solver = Solver(self.handler.expression)
        self.answer = self.solver.solve()
        print(self.answer)
