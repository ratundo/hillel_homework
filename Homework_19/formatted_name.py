import unittest


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


class TestFormattedName(unittest.TestCase):

    def test_correct_cases(self):
        self.assertEqual(formatted_name('a', 'b'), 'A B')
        self.assertEqual(formatted_name('a', 'b', 'c'), 'A C B')
        self.assertEqual(formatted_name('ABC', 'AbC', 'ABC'), 'Abc Abc Abc')

    def test_errors(self):
        with self.assertRaises(TypeError):
            formatted_name('')
        with self.assertRaises(TypeError):
            formatted_name(1, 2)
        with self.assertRaises(TypeError):
            formatted_name('a', 'b', 'c', 'd')
