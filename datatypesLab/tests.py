""" tests for data_type function"""
import unittest
from datatypeslab import data_type

class Datatype(unittest.TestCase):
    """Unit test cases for data_type function"""
    def testargumentnone(self):
        """ test Should return no value for no arg"""
        self.assertEqual(data_type(None), 'no value',
                         msg='Should return no value for no arg')

    def testargumentstring(self):
        """ test Should return string length for strings"""
        self.assertEqual(data_type('hi'), 2,
                         msg='Should return string length for strings')

    def testargumentbool(self):
        """ test Should return function arg for bool types"""
        self.assertEqual(data_type(True), True,
                         msg='Should return function arg for bool types')
    def testargumentlessthan100(self):
        """ test Should return less than 100"""
        self.assertEqual(data_type(5), 'less than 100',
                         msg='Should return les than 100')

    def test_argument_more_than_100(self):
        """ test Should return more than 100"""
        self.assertEqual(data_type(115), 'more than 100',
                         msg='Should return more than 100')

    def test_argument_equal_to_100(self):
        """ test Should return equal to 100"""
        self.assertEqual(data_type(100), 'equal to 100',
                         msg='Should return equal to 100')

    def test_list_arg(self):
        """ test should return third value for list"""
        self.assertEqual(data_type([1, 2, 3, 4, 5]), 3,
                         msg='Should return third value for list')

    def test_small_list_arg(self):
        """ test Should return None for small lists"""
        self.assertEqual(data_type([1, 2]), None,
                         msg='Should return None for small lists')

    def test_function_arg(self):
        """ test Should return True for function args"""
        def hello(*arg):
            """sample function"""
            pass
        self.assertTrue(data_type(hello()),
                        msg='Should return True for function args')


if __name__ == '__main__':
    unittest.main()
