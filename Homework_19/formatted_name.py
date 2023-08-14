import unittest


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


class TestFormattedName(unittest.TestCase):

    def test_no_middle_name(self):
        self.assertEqual(formatted_name('Taras', \
                                        'Shevchenko'), \
                         'Taras Shevchenko')

    def test_fullname(self):
        self.assertEqual(formatted_name('Taras', 'Shevchenko', \
                                        'Hryhorovych'), \
                         'Taras Hryhorovych Shevchenko')

    def test_title(self):
        self.assertEqual(formatted_name('TARAS', 'sHeVCHENko', \
                                        'HRyhoRoVyCh'), 'Taras Hryhorovych Shevchenko')

    def test_empty_string(self):
        with self.assertRaises(TypeError):
            formatted_name('')

    def test_invalid_symbols(self):
        with self.assertRaises(TypeError):
            formatted_name(1, 2)

    def test_more_arguments(self):
        with self.assertRaises(TypeError):
            formatted_name('a', 'b', 'c', 'd')
