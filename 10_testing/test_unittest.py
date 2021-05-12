import unittest

class TestMath(unittest.TestCase):
    def test_square(self):
        def square(x):
            y = x * x * x
            return y
        x = 10
        expected_result2 = 100
        self.assertEquals(square(x), expected_result2)

class TestCube(unittest.TestCase):

    def test_check_equality(self):
        def square(x):
            y = x * x
            return y
        x = 10
        expected_result1 = 100
        self.assertEquals(square(x), expected_result1)

if __name__ == '__main__':
  unittest.main()

