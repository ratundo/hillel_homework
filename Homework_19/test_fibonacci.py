import unittest

class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.obj = Fibonacci()

    def test_correct_fib_number(self):
        self.assertEqual(self.obj(9), 34)

    def test_correct_big_number(self):
        self.assertEqual(self.obj(488), \
                         432995556774426913953123610518785740738997352293147773391602699511793756235520810632382557083997728981)

    def test_null_fib_number(self):
        self.assertEqual(self.obj(0), 0)

    def test_invalid_symbol(self):
        with self.assertRaises(ValueError):
            self.obj('a')

    def test_negative_digit(self):
        with self.assertRaises(ValueError):
            self.obj(-5)

    def test_more_arguments(self):
        with self.assertRaises(TypeError):
            self.obj(1, 2)

    def test_huge_number(self):
        with self.assertRaises(RecursionError):
            self.obj(999999999)


if __name__ == '__main__':
    unittest.main()