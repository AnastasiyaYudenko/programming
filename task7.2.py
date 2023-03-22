import unittest
import random

class NumbersTest(unittest.TestCase):

    def test_even(self):
        a = [random.random(), random.random(), random.random(), random.random(), random.random()]
        print(a)
        for num in a:
            with self.subTest(i=num):
                self.assertEqual(num >= 0.5, True)
                print(num)
        print(a)


test = NumbersTest()
test.test_even()