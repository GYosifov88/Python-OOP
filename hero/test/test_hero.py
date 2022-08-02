import unittest
from unittest import TestCase

from project.hero import Hero


class HeroTests(TestCase):
    USERNAME = 'Gosho'
    LEVEL = 10
    HEALTH = 100
    DAMAGE = 75

    BATTLE_LEVEL_INCREMENT = 1
    BATTLE_HEALTH_INCREMENT = 5
    BATTLE_DAMAGE_INCREMENT = 5

    def setUp(self) -> None:
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test_init__if_constructed_correctly(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test_battle__if_trying_to_battle_self__should_raise_error(self):
        enemy = Hero(self.USERNAME, 5, 20, 30)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle__if_hero_health_is_equal_or_lees_than_zero__should_raise_error(self):
        enemy = Hero('Pesho', 5, 20, 30)
        health_decreasement = 100
        self.hero.health -= health_decreasement
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle__if_enemy_hero_health_is_equal_or_lees_than_zero__should_raise_error(self):
        enemy = Hero('Pesho', 5, 20, 30)
        health_decreasement = 30
        enemy.health -= health_decreasement
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception))

    def test_battle__when_both_enemy_and_hero_healths_become_less_or_equal_to_zero_returns_draw(self):
        enemy = Hero('Pesho', self.LEVEL, self.HEALTH, self.DAMAGE)

        result = self.hero.battle(enemy)
        expected_health = self.HEALTH - (self.LEVEL * self.DAMAGE)
        self.assertEqual('Draw', result)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_health, enemy.health)

    def test_battle_when_hero_wins__should_increase_level_health_damage_and_return_you_win(self):
        enemy_level, enemy_health, enemy_damage = 1, 20, 30
        enemy = Hero('Pesho', enemy_level, enemy_health, enemy_damage)
        result = self.hero.battle(enemy)
        current_health = self.HEALTH - (enemy.level * enemy.damage)
        enemy_expected_health = enemy_health - (self.LEVEL * self.DAMAGE)
        self.assertEqual(enemy_expected_health, enemy.health)
        self.assertEqual(self.LEVEL + self.BATTLE_LEVEL_INCREMENT, self.hero.level)
        self.assertEqual(self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT, self.hero.damage)
        self.assertEqual(current_health + self.BATTLE_HEALTH_INCREMENT, self.hero.health)
        self.assertEqual('You win', result)

    def test_battle_when_enemy_wins__should_increase_level_health_damage_and_return_you_lose(self):
        enemy_level, enemy_health, enemy_damage = 5, 1000, 30
        enemy = Hero('Pesho', enemy_level, enemy_health, enemy_damage)
        result = self.hero.battle(enemy)
        expected_hero_health = self.HEALTH - (enemy_level * enemy_damage)
        expected_enemy_health = enemy_health - (self.hero.level * self.hero.damage)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(enemy_level + self.BATTLE_LEVEL_INCREMENT, enemy.level)
        self.assertEqual(enemy_damage + self.BATTLE_DAMAGE_INCREMENT, enemy.damage)
        self.assertEqual(expected_enemy_health + self.BATTLE_HEALTH_INCREMENT, enemy.health)
        self.assertEqual('You lose', result)

    def test_str__representation_works_correctly(self):
        actual_result = str(self.hero)
        expected_result = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
               f"Health: {self.HEALTH}\n" \
               f"Damage: {self.DAMAGE}\n"
        self.assertEqual(expected_result, actual_result)



if __name__ == '__main__':
    unittest.main()