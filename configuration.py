from math_functions import *


"""
configuration file: contains all the configuration variables
"""

# all the valid characters
VALID_CHARS = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#', '(', ')', '.', ' ']
# all the valid operators
OPERATORS = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#']
# side of the operands near to the operator
OPERAND_SIDE = {'+': "both", '-': "both", '*': "both", '/': "both", '^': "both", '%': "both", '$': "both", '&': "both",
                '@': "both", '~': "right", '!': "left", '#': "left"}
# priority of the operators
OPERATOR_PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6, '#': 6}
# function of the operators
OPERATOR_FUNCTION = {'+': addition, '-': subtraction, '*': multiplication, '/': division, '^': power, '%': modulo,
                     '$': minimum, '&': maximum, '@': average, '~': tilda, '!': factorial, '#': summation}
# all the valid brackets
CLOSING_BRACKETS = [')']
OPENING_BRACKETS = ['(']

# constants
RIGHT = "right"
LEFT = "left"
BOTH = "both"
SPACE = ' '
DOT = '.'
MINUS = '-'
PLUS = '+'
NONE = "none"

OPENING_BRACKET = '('
CLOSING_BRACKET = ')'
BRACKETS = OPENING_BRACKET + CLOSING_BRACKET
