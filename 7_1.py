import unittest


def check_mark(mark):
    if mark >= 3:
        return True
    else:
        return False

def reverse_dict(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    return new_dict


class TestStringMethods(unittest.TestCase):

    def test_mark(self):
        self.assertTrue(check_mark(4))
        self.assertFalse(check_mark(2))

    def test_dict(self):
        d = {'house':'roof'}
        n_d = reverse_dict(d) #{'roof': 'house'}
        self.assertIn('house', list(n_d.values()))
        self.assertNotIn('house', list(n_d.keys()))


