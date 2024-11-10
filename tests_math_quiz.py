import unittest
from math_quiz import function_A, function_B, function_C

class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of times for randomness
            op = function_B()
            self.assertIn(op, operators)

    def test_function_C(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_C(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
