from math_functions import *


class Solver(object):
    """class to solve the exercise"""
    def __init__(self, exercise: str):
        self.exercise = exercise
        self.priorities = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6}
        self.operators = {'+': addition, '-': subtraction, '*': multiplication, '/': division, '^': power,
                          '%': modulo, '$': minimum, '&': maximum, '@': average, '~': tilda, '!': factorial}
