from car_manager import Car

import unittest
from unittest import TestCase


class CarTests(TestCase):
    MAKE = 'VW'
    MODEL = 'Passat'
    FUEL_CONSUMPTION = 5
    FUEL_CAPACITY = 60
    FUEL_AMOUNT = 0

    def setUp(self) -> None:
        self.car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)

    def test_init__when_valid_props__expect_correct_values(self):
        self.assertEqual(self.MAKE, self.car.make)
        self.assertEqual(self.MODEL, self.car.model)
        self.assertEqual(self.FUEL_CONSUMPTION, self.car.fuel_consumption)
        self.assertEqual(self.FUEL_CAPACITY, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_init__if_make_given_is_empty__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))
        self.assertIsNotNone(ex)

    def test_init__if_model_given_is_empty__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))
        self.assertIsNotNone(ex)

    def test_init__if_fuel_consumption_given_is_negative__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
        self.assertIsNotNone(ex)

    def test_init__if_fuel_consumption_given_is_zero__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
        self.assertIsNotNone(ex)

    def test_init__if_fuel_capacity_given_is_negative__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))
        self.assertIsNotNone(ex)

    def test_init__if_fuel_capacity_given_is_zero__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))
        self.assertIsNotNone(ex)

    def test_init__if_fuel_amount_given_is_negative__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))
        self.assertIsNotNone(ex)

    def test_refuel__if_amount_given_is_negative__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-5)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertIsNotNone(ex)


    def test_refuel__if_amount_is_correct__should_increase_fuel_amount(self):
        self.car.refuel(5)
        self.assertEqual(self.FUEL_AMOUNT+5, self.car.fuel_amount)


    def test_refuel__if_with_amount_given_total_amount_is_greater_than_capacity__should_set_amount_to_capacity(self):
        self.car.refuel(61)
        self.assertEqual(self.FUEL_AMOUNT + 61, self.car.fuel_capacity)

    def test_drive__if_fuel_amount_is_enough_for_distance__should_decrease_fuel(self):
        distance = 100
        needed = (100 / 100) * self.FUEL_CONSUMPTION

        self.car.drive(distance)
        expected_result = self.FUEL_AMOUNT - needed
        self.assertEqual(expected_result, self.car.fuel_amount)

    def test_drive__if_fuel_amount_is_not_enough_for_distance__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(200)
        self.assertEqual(self.FUEL_AMOUNT, self.car.fuel_amount)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive__if_fuel_amount_is_for_max_distance__should_make_it_zero(self):
        distance = self.FUEL_AMOUNT / self.FUEL_CONSUMPTION

        self.car.drive(distance)
        self.assertEqual(0, self.car.fuel_amount)

if __name__ == '__main__':
    unittest.main()