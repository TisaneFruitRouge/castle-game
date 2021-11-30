import random
from utils import bcolors

'''
	BaseCharacter class. Used to model some basic functionnalities that all characters have
'''
class BaseCharacter():

	def __init__(self, max_health, base_damage, coins, ability_success_rate=0.5):

		self.max_health = max_health
		self.health_point = max_health
		self.base_damage = base_damage
		self.coins = coins
		self.ability_success_rate = ability_success_rate

	def apply_damage(self, damage):
		self.health_point -= base_damage

	def heal(self, healing):
		self.health_point += healing

	def special_ability(self):
		return random.randrange() < self.ability_success_rate

	def print_stats(self):

		print(f"> {bcolors.HEALTH_COLOR}Health:{bcolors.ENDC}: {self.health_point}/{self.max_health}")
		print(f"> {bcolors.DAMAGE_COLOR}Damage:{bcolors.ENDC}: {self.base_damage}")
		print(f"> {bcolors.COIN_COLOR}Coins:{bcolors.ENDC}: {self.coins}")


'''
	Trader Character
	Passive hability: "Coins"   -> Starts with 20 more coins 
	Special hability: "Likable" -> when buying an item, has a 85% to have a 20% discount and a 15%
								  chance that the item will be 20% more expensive
'''
class Trader(BaseCharacter):

	def __init__(self, max_health, base_damage, coins):
		super().__init__(max_health, base_damage, coins+20, 0.85)


	def print_stats(self):
		print(f"## {bcolors.TRADER_COLOR}Trader{bcolors.ENDC} ##")
		super().print_stats()
	
'''
	Trader Character
	Passive hability: "Backstab" -> applies more damage but has less max health
	Special hability: "Steal" -> can try to steal an item. Has a 51% chance of success. If it fails,
								 the thief will be expelled temporarily from the shop
'''
class Thief(BaseCharacter):

	def __init__(self, max_health, base_damage, coins):
		super().__init__(max_health-20, base_damage+15, coins, 0.51)


	def print_stats(self):
		print(f"## {bcolors.THIEF_COLOR}Thief{bcolors.ENDC} ##")
		super().print_stats()

'''
	Orc Character
	Passive hability: "Tough"      -> Has more max health and more damage
	Special hability: "Intimidate" -> when at the shop, has a 30% chance to get a free item. If it fails,
									  prices will go up by 20%
'''
class Orc(BaseCharacter):

	def __init__(self, max_health, base_damage, coins):
		super().__init__(max_health+20, base_damage+20, coins, 0.3)	

	def print_stats(self):
		print(f"## {bcolors.ORC_COLOR}Orc{bcolors.ENDC} ##")
		super().print_stats()