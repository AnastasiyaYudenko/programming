import unittest
import os
import shutil


def file_dir_test(directory):
    os.makedirs(directory)
    with open(directory + r'\text.txt', 'w') as file:
        some_text = 'Hello, world!'
        file.write(some_text)


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        file_dir_test(r'C:\Users\79088\PycharmProjects\programming\kek')
        with open(r'C:\Users\79088\PycharmProjects\programming\kek\text.txt', 'r') as file:
            text = file.read()
            self.assertTrue(text)
            self.assertEqual('Hello, world!', text)

    def tearDown(self):
        shutil.rmtree(r'C:\Users\79088\PycharmProjects\programming\kek')


test = TestStringMethods()
test.setUp()
test.tearDown()