import streamlit as st
from sympy.parsing.sympy_parser import parse_expr
from integrator.simplifier import process_expression
from integrator.integrator import integrate_expression

st.title("📐 Trig Integral Simplifier")

expr_input = st.text_input("Enter your expression", "sin(x)**2 + cos(x)**2")

if st.button("Simplify and Integrate"):
    expr = parse_expr(expr_input)
    simplified_expr, _ = process_expression(expr)
    result = integrate_expression(simplified_expr)
    
    st.write("**Simplified Expression:**", simplified_expr)
    st.write("**Integral Result:**", result)