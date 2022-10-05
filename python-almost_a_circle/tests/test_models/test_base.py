#!/usr/bin/python3
""" Test Base """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """"""
    def test_to_json_string(self):
        """ Test to_json_string """
        dic = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        json_dic = Base.to_json_string([dic])
        self.assertTrue(isinstance(dic, dict))
        self.assertTrue(isinstance(json_dic, str))
        self.assertCountEqual(
            json_dic, '{["id": 1, "x": 2, "y": 3, "width": 4, "height": 5]}')
        json_d_1 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")
        err = ("to_json_string() missing 1 required positional argument: " +
               "'list_dictionaries'")
        with self.assertRaises(TypeError) as i:
            Base.to_json_string()
        self.assertEqual(err, str(i.exception))
        err = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as i:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(err, str(i.exception))

if __name__ == '__main__':
    unittest.main()
