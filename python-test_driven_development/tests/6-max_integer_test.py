#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ tests max_integer """

    def test_negative(self):
        """Test with list negative values return the max"""
        list_negative = [-2, -6, -1]
        result = max_integer(list_negative)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
