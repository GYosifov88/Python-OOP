import unittest
from unittest import TestCase

from project.vehicle import Vehicle

class VehicleTests(TestCase):
    FUEL = 100
    HORSE_POWER = 120
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.car = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_init__when_valid_props__expect_correct_values(self):
        self.assertEqual(self.FUEL, self.car.fuel)
        self.assertEqual(self.HORSE_POWER, self.car.horse_power)
        self.assertEqual(self.FUEL, self.car.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.car.fuel_consumption)

    def test_drive__if_fuel_amount_is_enough_for_distance__should_decrease_fuel(self):
        distance = 50
        needed = distance * self.DEFAULT_FUEL_CONSUMPTION

        self.car.drive(distance)
        expected_result = self.FUEL - needed
        self.assertEqual(expected_result, self.car.fuel)

    def test_drive__if_fuel_amount_is_not_enough_for_distance__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(200)
        self.assertEqual(self.FUEL, self.car.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive__if_fuel_amount_is_for_max_distance__should_make_it_zero(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION

        self.car.drive(distance)
        self.assertEqual(0, self.car.fuel)

    def test_refuel__if_amount_is_correct__should_increase_fuel_amount(self):
        fuel_amount = 20
        self.car.fuel -= fuel_amount
        self.car.refuel(fuel_amount)
        self.assertEqual(self.FUEL, self.car.fuel)

    def test_refuel__if_with_amount_given_total_amount_is_greater_than_capacity__should_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(61)
        # self.assertEqual(self.FUEL + 61, self.car.capacity)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str__if_correct_message_is_returned(self):
        actual_result = str(self.car)
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()