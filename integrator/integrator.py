from sympy import symbols, integrate

def integrate_expression(expr, variable='x', definite=False, limits=None):
    var = symbols(variable)
    if definite and limits:
        return integrate(expr, (var, *limits))
    return integrate(expr, var)