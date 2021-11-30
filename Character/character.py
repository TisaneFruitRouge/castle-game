import random


'''
	BaseCharacter class. Used to model some basic functionnalities that all characters have
'''
class BaseCharacter():

	def __init__(self, health_point, base_damage, coins, ability_success_rate=0.5):

		self.health_point = health_point
		self.base_damage = base_damage
		self.coins = coins
		self.ability_success_rate = ability_success_rate

	def apply_damage(self, damage):
		self.health_point -= base_damage

	def heal(self, healing):
		self.health_point += healing

	def special_ability(self):
		return random.randrange() < self.ability_success_rate


'''
	Trader Character
	Passive hability: "Coins"   -> Starts with 20 more coins 
	Special hability: "Likable" -> when buying an item, has a 85% to have a 20% discount and a 15%
								  chance that the item will be 20% more expensive
'''
class Trader(BaseCharacter):

	def __init__(self, health_point, base_damage, coins):
		super().__init__(health_point, base_damage, coins+20, 0.85)

	
'''
	Trader Character
	Passive hability: "Backstab" -> applies more damage but has less health
	Special hability: "Steal" -> can try to steal an item. Has a 51% chance of success. If it fails,
								 the thief will be expelled temporarily from the shop
'''
class Thief(BaseCharacter):

	def __init__(self, health_point, base_damage, coins):
		super().__init__(health_point-20, base_damage+15, coins, 0.51)


'''
	Orc Character
	Passive hability: "Tough"      -> Has more health and more damage
	Special hability: "Intimidate" -> when at the shop, has a 30% chance to get a free item. If it fails,
									  prices will go up by 20%
'''
class Orc(BaseCharacter):

	def __init__(self, health_point, base_damage, coins):
		super().__init__(health_point+20, base_damage+20, coins, 0.3)