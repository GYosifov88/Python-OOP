from project.mammal import Mammal

import unittest
from unittest import TestCase


class MammalTests(TestCase):

    def test_init__if_constructed_correctly(self):
        animal = Mammal('Gosho', 'human', 'zzzz')
        self.assertEqual('Gosho', animal.name)
        self.assertEqual('human', animal.type)
        self.assertEqual('zzzz', animal.sound)
        self.assertEqual('animals', animal._Mammal__kingdom)

    def test_make_sound__if_return_correct_text(self):
        animal = Mammal('Gosho', 'human', 'zzzz')
        actual_result = animal.make_sound()
        expected_result = f"{animal.name} makes {animal.sound}"
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom__if_returning_correct_kingdom(self):
        animal = Mammal('Gosho', 'human', 'zzzz')
        actual_result = animal.get_kingdom()
        self.assertEqual(animal._Mammal__kingdom, actual_result)

    def test_info__if_returning_correct_message(self):
        animal = Mammal('Gosho', 'human', 'zzzz')
        actual_result = animal.info()
        expected_result = f"{animal.name} is of type {animal.type}"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()