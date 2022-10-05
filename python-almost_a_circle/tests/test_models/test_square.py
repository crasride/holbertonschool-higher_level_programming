#!/usr/bin/python3
""" Test Square """
import unittest


class Testsquare(unittest.TestCase):
    """"""
    
    def test_basic(self):
        """ Basic Square """
        self.assertEqual(1, 1)
        self.assertEqual(2, 2)
        self.assertEqual(3, 3)
        self.assertEqual(4, 4)

    def test_case_2(self):
        self.skipTest('Work in progress')
        self.assertIsNotNone([])




if __name__ == '__main__':
    unittest.main()
