from sympy.parsing.sympy_parser import parse_expr
from integrator.simplifier import process_expression
from integrator.integrator import integrate_expression

def main():
    expr_str = input("Enter expression: ")
    expr = parse_expr(expr_str)

    simplified_expr, steps = process_expression(expr)

    integrate_prompt = input("Integrate? (y/n): ").lower()
    if integrate_prompt == "y":
        result = integrate_expression(simplified_expr)
        print("Result:", result)

if __name__ == "__main__":
    main()