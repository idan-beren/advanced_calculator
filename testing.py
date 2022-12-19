from handler import *
from postfix import *

"""file of the tests"""

# dictionary of valid expressions
valid_expressions = {
    "1.1+2!": 3.1,
    "22#-2": 2.0,
    "2^2^2": 16.0,
    "110/11-1!": 9.0,
    "-2.2#": -4.0,
    "-~1!": 1.0,
    "1-~44#": 9.0,
    "22%22": 0.0,
    "99@9+9": 63.0,
    "22#$3": 4.0,
    "44&2!": 2.0,
    "(980#!#%4^3^3)/(33$33$33)@(33*3^2)": 119.2909090909091,
    "--1!+-1.123#+~-(22.2$2.22+-~(55/5-8))": 19.2,
    "---~--2.22#+--1!-((3!--1)#$(3.3^3.3))": -44.415729444066585,
    "(--~-2+-2.2+(3.3+3.7)!--((8.8&44)#))": 5055.8,
    "-~-((2^-~2.2^-~2)--~-(.22*(1.^4.))^.1%1.)": -21.971619422126384,
    "((11/11)*(22^1))/((33%100)/(44$55))%((66&77)%(11@99))": 36.66666666666667,
    "(--~---1!!--2!!)*(12-6*(5-2))+-~3+~-3": -12.0,
    "(22.22*100)##/(13.11-11.11)!": 4.0,
    "(44$2.2-5.55&99-~-2.@.2)+-(~2-2)": 41.35,
    "(44/44/44/44*22$55)+(55^1.5-11^.3)%3": 0.8661894675117568,
    "66*--~-(2+2-1)*-~--(1-555)+-~-(2+88)/--~(1+1)": -109647.0,
    "-~-((5---~-99+-~---(2+--33)+-~88))": 41.0,
    "--~-( ~-.99^-~-( 9.^.9 ) ) / ( -~-77.# -~.1 $ 6.5)": -0.05245422022800017,
    "(-~- 44%-~-( 433#+-~-( 3.33 +- .33) -- 1))##": -4.0,
    "(-(~ 4)! +~-8!--( ~-33 )!)/( -(~4 )!+~-8!--( ~-33 )!)": 1.0,
    "( ~-(-~ 2!)! )!*-(-~- ( 5 ))!/~-( 4% 66)": 60.0,
}

# list of invalid expressions
invalid_expressions = [
    ""
    "            "
    "          \t"
    "hello-world!"
    "(-1+1))"
    "-~-3!"
    "1.1!"
    "11/0"
    "22%0"
    "-~-~3"
    "1.1.1"
    "1**2"
    "!3"
    "3~"
]


def helper(expression: str) -> float:
    """function to solve the expression"""
    handler = Handler(expression)
    postfix = Postfix(handler.expression)
    postfix.convert_infix_to_postfix()
    return postfix.solve_postfix()


def test_valid_expressions():
    """function to test the valid expressions"""
    for valid_expression in valid_expressions:
        assert valid_expressions[valid_expression] == helper(valid_expression)


def test_invalid_expressions():
    """function to test the invalid expressions"""
    for invalid_expression in invalid_expressions:
        try:
            helper(invalid_expression)
            assert False
        except SyntaxError:
            assert True
        except ValueError:
            assert True
        except OverflowError:
            assert True
        except ZeroDivisionError:
            assert True
