import unittest
from sympy import sin, cos, symbols
from integrator.simplifier import process_expression

x = symbols('x')

class TestSimplification(unittest.TestCase):
    def test_identity(self):
        expr = sin(x)**2 + cos(x)**2
        simplified, _ = process_expression(expr)
        self.assertEqual(simplified, 1)

if __name__ == "__main__":
    unittest.main()