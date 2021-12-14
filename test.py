import unittest

from Character.characters import BaseCharacter
from Items.items import Potion

class CharacterClassTest(unittest.TestCase):

	def setUp(self):
		self.character = BaseCharacter(100, 20, 100, 0.5)

	def tearDown(self):
		self.character = None
	
	def test_apply_damage(self):
		self.character.apply_damage(20)
		self.assertEqual(self.character.health_points, 80)

	def test_restore_health(self):
		self.character.restore_health(20)
		self.assertEqual(self.character.health_points, 100)
		self.character.restore_health(20) # health should not be superior to 100
		self.assertEqual(self.character.health_points, 100)

	def test_add_coins(self):
		self.character.add_coins(20)
		self.assertEqual(self.character.coins, 120)
	
	def test_remove_coins(self):
		self.character.add_coins(-20)
		self.assertEqual(self.character.coins, 80)


	def test_if_deafeated(self):
		self.character.apply_damage(100)
		self.assertTrue(self.character.is_defeated())

	def test_add_potion(self):
		self.character.add_item(Potion(75, 3))
		self.assertTrue(self.character.has_potion())

	def use_potion(self):
		self.character.add_item(Potion(75, 3))
		self.character.use_potion()
		self.assertFalse(self.character.has_potion())

if __name__ == '__main__':
    unittest.main()