import random
import json

from utils import bcolors, read_art_from_file
from Items.items import Weapon, Protection, Potion

'''
	BaseCharacter class. Used to model some basic functionnalities that all characters have
'''
class BaseCharacter():

	def __init__(self, max_health, base_damage, coins, ability_success_rate=0.5):

		self.max_health = max_health
		self.health_points = max_health
		self.base_damage = base_damage
		self.coins = coins
		self.ability_success_rate = ability_success_rate

		self.inventory = list()

		self.color = ''
		self.name = ""

		self.unlocked_door = False
		self.dragon_defeated = False

	'''
		Applies damage to the character
	'''
	def apply_damage(self, damage):
		self.health_points = max(self.health_points-damage, 0)

	'''
		Return a boolean idicating if the special hability worked
	'''
	def special_ability(self):
		return random.random() < self.ability_success_rate

	'''
		Prints the character's statistics
	'''
	def print_stats(self):

		print(f"## {self.color}{self.name}{bcolors.ENDC} ##")

		print("> ==== STATS ====")

		print(f"> {bcolors.HEALTH_COLOR}Health:{bcolors.ENDC} {self.health_points}/{self.max_health}")
		print(f"> {bcolors.DAMAGE_COLOR}Damage:{bcolors.ENDC} {self.base_damage}")
		print(f"> {bcolors.COIN_COLOR}Coins:{bcolors.ENDC} {self.coins}\n")

	'''
		Give a certain amount of health back
	'''
	def restore_health(self, amount):
		self.health_points = min(self.health_points+amount, self.max_health)
		return self.health_points

	'''
		Loops over the inventory, returns True if there is a potion, False otherwise
	'''
	def has_potion(self):
		for item in self.inventory:
			if isinstance(item, Potion):
				return True
		return False


	'''
		Uses a potion
	'''
	def use_potion(self):
		for item in self.inventory:
			if isinstance(item, Potion):
				item.amount -= 1
				self.restore_health(25)
				return item.amount
		return 0 

	'''
		Adds coins to the character's purse
	'''
	def add_coins(self, coins):
		self.coins += coins
		return self.coins

	'''
		Adds an item to the inventory
	'''
	def add_item(self, item, free=False):
		
		if (not free):
			self.add_coins(-item.price) 	

		if (isinstance(item, Weapon)):
			self.base_damage+=item.attack_damage
		elif (isinstance(item, Protection)):
			self.max_health+=item.health_boost
			self.health_point = min(self.max_health, self.health_points+item.health_boost)
		elif (isinstance(item, Potion)):
			for i in self.inventory:
				if (isinstance(i, Potion)):
					i.amout+=item.amout
					i.price = 25*i.amount
					return
		self.inventory.append(item)

	'''
		Prints the inventory
	'''
	def show_inventory(self):
		print(f"> {bcolors.UNDERLINE}Inventory :{bcolors.ENDC}")
		
		if len(self.inventory)==0:
			print(f"    {bcolors.ITALIC}Empty..{bcolors.ENDC}")
		else:
			for (idx, item) in enumerate(self.inventory):
				print(f"{idx+1} ▹ {item}")

	'''
		Returns True if the health points are below 0
	'''
	def is_defeated(self):
		return self.health_points <= 0



'''
	Trader Character
	Passive hability: "Coins"   -> Starts with 20 more coins 
	Special hability: "Likable" -> when buying an item, has a 85% to have a 20% discount and a 15%
								  chance that the item will be 20% more expensive
'''
class Trader(BaseCharacter):

	def __init__(self, max_health, base_damage, coins):
		super().__init__(max_health, base_damage, coins+20, 0.85)
		self.name = "Trader"
		self.hability = "Likable"
		self.color = bcolors.TRADER_COLOR
		
	
'''
	Trader Character
	Passive hability: "Backstab" -> applies more damage but has less max health
	Special hability: "Steal" -> can try to steal an item. Has a 51% chance of success. If it fails,
								 the thief will be expelled temporarily from the shop
'''
class Thief(BaseCharacter):

	def __init__(self, max_health, base_damage, coins):
		super().__init__(max_health-20, base_damage+15, coins, 0.51)
		self.name = "Thief"
		self.hability = "Steal"
		self.color = bcolors.THIEF_COLOR

'''
	Orc Character
	Passive hability: "Tough"      -> Has more max health and more damage
	Special hability: "Intimidate" -> when at the shop, has a 30% chance to get a free item. If it fails,
									  prices will go up by 35%
'''
class Orc(BaseCharacter):

	def __init__(self, max_health, base_damage, coins):
		super().__init__(max_health+20, base_damage+10, coins, 0.3)	
		self.name = "Orc"
		self.color = bcolors.ORC_COLOR
		self.hability = "Intimidate"


'''
	Class for an Enemy
'''
class Enemy():

	def __init__(self, max_health, damages, coins):
		self.max_health = max_health
		self.health_points = max_health
		self.damages = damages
		self.coins = coins

		self.name = ""

	'''
		Applies damage to the enemy object
	'''
	def apply_damage(self, damage):
		self.health_points = max(self.health_points-damage, 0)

	'''
		Return a certain amount of damage
	'''
	def attack(self):
		return self.damages if random.random() > 0.2 else 1.5*self.damages # 20% chance of critical strike (+50% damage)

	'''
		Returns True if the health points are below 0
	'''
	def is_defeated(self):
		return self.health_points <= 0

	'''
		Prints the enemy's statistics
	'''
	def print_stats(self):

		read_art_from_file(f"{self.name.lower()}.txt")

		print(f"## {bcolors.DAMAGE_COLOR}{self.name}{bcolors.ENDC} ##")

		print("> ==== STATS ====")

		print(f"> {bcolors.HEALTH_COLOR}Health:{bcolors.ENDC} {self.health_points}/{self.max_health}")
		print(f"> {bcolors.DAMAGE_COLOR}Damage:{bcolors.ENDC} {self.damages}")
		print(f"> {bcolors.COIN_COLOR}Loot:{bcolors.ENDC} {self.coins} coins\n")

'''
	Goblin (encounter one goblin each time you go if the black forest)
'''
class Goblin(Enemy):

	def __init__(self, max_health, damages, coins):
		super().__init__(max_health, damages, coins)
		self.name = "Goblin"

'''
	Dragon (Final boss, inside the castle)
'''
class Dragon(Enemy):

	def __init__(self, max_health=500, damages=30, coins=0):
		super().__init__(max_health, damages, coins)
		self.name = "Dragon"