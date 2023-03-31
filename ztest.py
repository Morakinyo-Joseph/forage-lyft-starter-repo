import unittest


def add(a, b):
    return a + b


class SumTest(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 20

    def test_sum_1(self):
        result = add(self.a, self.b)
        self.assertEqual(result, self.a + self.b)

    def test_sum_2(self):
        result = add(self.a, self.b)
        self.assertEqual(result, self.a + self.b)


if __name__ == "__main__":
    unittest.main()
