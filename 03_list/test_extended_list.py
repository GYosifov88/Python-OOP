from extended_list import IntegerList

import unittest
from unittest import TestCase


class IntegerListTest(TestCase):

    def test_init__if_constructed_incorrectly(self):
        into = IntegerList(22.5, -2.3, 'aaa')
        self.assertIsNotNone([], into._IntegerList__data)

    def test_init__if_constructed_correctly(self):
        into = IntegerList(5, 10)
        self.assertIsNotNone([5, 10], into._IntegerList__data)

    def test_add__with_correct_data(self):
        into = IntegerList(6)
        into.get_data()
        self.assertEqual([6], into.get_data())
        into.add(10)
        self.assertEqual([6, 10], into.get_data())

    def test_add_with_wrong_data(self):
        into = IntegerList(6)
        with self.assertRaises(ValueError) as ex:
            into.add(10.5)
        self.assertEqual("Element is not Integer", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            into.add("aaa")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_right_index(self):
        into = IntegerList(6, 7, 10)
        result = into.remove_index(1)
        self.assertEqual(7, result)
        self.assertEqual([6, 10], into.get_data())

    def test_remove_wrong_index(self):
        into = IntegerList(6, 7, 10)
        with self.assertRaises(IndexError) as ex:
            into.remove_index(6)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_with_right_element(self):
        into = IntegerList(6, 7, 10)
        result = into.get(1)
        self.assertEqual(7, result)

    def test_get_with_wrong_element(self):
        into = IntegerList(6, 7, 10)
        into.get_data()
        self.assertEqual([6, 7, 10], into.get_data())
        with self.assertRaises(IndexError) as ex:
            into.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_with_right_data(self):
        into = IntegerList(6, 7, 10)
        result = into.insert(0, 10)
        self.assertEqual(None, result)
        self.assertEqual([10, 6, 7, 10], into.get_data())

    def test_insert_with_wrong_index_data(self):
        into = IntegerList(6, 7, 10)
        with self.assertRaises(IndexError) as ex:
            into.insert(5, 10)
        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([6, 7, 10], into.get_data())

    def test_insert_with_wrong_type_data(self):
        into = IntegerList(6, 7, 10)
        with self.assertRaises(ValueError) as ex:
            into.insert(0, "aaa")
        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual([6, 7, 10], into.get_data())

    def test_get_biggest(self):
        into = IntegerList(6, 7, 10, 200, -356, 1000, -2500)
        result = into.get_biggest()
        self.assertEqual(1000, result)

    def test_get_index(self):
        into = IntegerList(6, 7, 10, 200, -356, 1000, -2500)
        result = into.get_index(6)
        self.assertEqual(0, result)
        result = into.get_index(-2500)
        self.assertEqual(6, result)
        result = into.get_index(10)
        self.assertEqual(2, result)


if __name__ == "__main__":
    unittest.main()