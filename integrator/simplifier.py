from sympy import simplify, expand_trig, factor
from .identity_log import log_step

def process_expression(expr):
    steps = []

    simplified = simplify(expr)
    log_step(expr, simplified, "General simplification")
    steps.append(("simplify", simplified))

    expanded = expand_trig(simplified)
    log_step(simplified, expanded, "Trig expansion")
    steps.append(("expand_trig", expanded))

    factored = factor(expanded)
    log_step(expanded, factored, "Factoring trig expression")
    steps.append(("factor", factored))

    return factored, steps