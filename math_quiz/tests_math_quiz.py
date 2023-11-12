import unittest
from math_quiz import randomNumGenerator, randomOperatorGenerator, printResult


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomNumGenerator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        operators = set()
        for _ in range(1000):  # Test a large number of random values
            rand_operator = randomOperatorGenerator()
            operators.add(rand_operator)
        self.assertEqual(len(operators), 3)

    def test_function_C(self):
        test_cases = [
        (5, 2, '+', '5 + 2', 7),
        (8, 3, '-', '8 - 3', 5),
        (4, 6, '*', '4 * 6', 24)]

            
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            with self.subTest(num1=num1, num2=num2, operator=operator):
                problem, answer = printResult(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
