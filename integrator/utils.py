# Helpers here - such as detecting dominant trig functions, etc.
def is_trig_expression(expr):
    return any(func in str(expr) for func in ['sin', 'cos', 'tan', 'sec', 'csc', 'cot'])