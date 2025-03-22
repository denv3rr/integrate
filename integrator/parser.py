from sympy.parsing.sympy_parser import parse_expr

def parse_input(expression: str):
    return parse_expr(expression)