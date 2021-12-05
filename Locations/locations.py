import random
import json
import time

from utils import user_input, range_input, read_art_from_file, bcolors, clear
from Items.items import Weapon, Protection, Potion
from Character.characters import Trader, Thief, Orc, Goblin, Dragon

'''
	This class is parent to each location
'''
class BaseLocation():

	def __init__(self, name, ascii_icon, north_location=None, south_location=None, west_location=None, east_location=None):
		self.name = name
		self.ascii_icon = ascii_icon
		self.north_location = north_location
		self.south_location = south_location
		self.west_location = west_location
		self.east_location = east_location

	def entering(self):
		print(f"> You arrived to to the {self.name}")

	def changing_location(self):
		print("> Where do you wish to go ?")

	def location_event(self, character): # default
		return 0; # signals a default location event

	# https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
	def toJSON(self):
		return json.dumps(self.name)

class Plain(BaseLocation):

	def __init__(self):
		super().__init__("Plain", "P", Town)

	def entering(self):
		super().entering()
		read_art_from_file("plain.txt")
		print(f"> This is just a regular plain, you probably won't find anything interesting")

	def changing_location(self):
		super().changing_location()
		location = user_input("North")
		print(f"> You are going to the {self.north_location().name} !")
		return self.north_location()

class Town(BaseLocation):

	def __init__(self):
		super().__init__("Town", "T", BlackForest, Plain, Bar, Shop)

	def entering(self):
		super().entering()
		read_art_from_file("town.txt")
		print(f"> This is the Town!")


	def changing_location(self):
		super().changing_location()
		location = user_input("North","South","West","East")

		if (location=="North"):
			print(f"> You are going to the {self.north_location().name} !")
			return self.north_location()
		elif(location == "South"):
			print(f"> You are going to the {self.south_location().name} !")
			return self.south_location()
		elif(location == "West"):
			print(f"> You are going to the {self.west_location().name} !")
			return self.west_location()
		elif(location == "East"):
			print(f"> You are going to the {self.east_location().name} !")
			return self.east_location()

class Bar(BaseLocation):

	def __init__(self):
		super().__init__("Bar", "B", None, None, None, Town)

	def entering(self):
		super().entering()
		read_art_from_file("bar.txt")
		print(f"> Here you'll be able to buy drinks and gamble some coins")

	def changing_location(self):
		super().changing_location()
		location = user_input("East")
		print(f"> You are going to the {self.east_location().name} !")
		return self.east_location()

	def location_event(self, character):

		print("> Welcome to the bar!")
		print("> Here, you can dring, and gamble!")
		print("\n")

		print(f"> Drink - Costs {bcolors.COIN_COLOR}15 coins{bcolors.ENDC} but restores {bcolors.HEALTH_COLOR}15 HP{bcolors.ENDC}")
		print("> Gamble - 50% to double your bet, 50% chance to lose it")

		exit = False
		while (not exit):
			user_choice = user_input("Drink","Gamble", "Exit")
			if (user_choice=="Drink"):
				if (character.coins < 15):
					print("> You don't have eonugh coins to buy you a drink\n")
				else: 
					print("> You drink a fresh beer!")
					character.add_coins(-15)
					print(f"> You now have {character.restore_health(25)} HP!")

			elif (user_choice=="Gamble"):
				print("> How many coins do you wanna gamble ?")
				coins = range_input(1, character.coins, as_int=True)

				if (random.random()<0.5): # the player loses
					print(f"> You lost {coins} coins! You now have {character.add_coins(-coins)}\n")
				else : # the player wins
					print(f"> You won {coins} coins! You now have {character.add_coins(coins)}\n")

			elif(user_choice=="Exit"):
				print("> You are leaving the bar.\n")
				exit = True

class Shop(BaseLocation):

	def __init__(self):
		super().__init__("Shop", "S", None, None, Town)

	def entering(self):
		super().entering()
		read_art_from_file("shop.txt")
		print(f"> You'll find everyting you need in this shop!")

	def changing_location(self):
		super().changing_location()
		location = user_input("West")
		print(f"> You are going to the {self.west_location().name} !")
		return self.west_location()

	# Shop's location event: Buying items
	def location_event(self, character):
		
		weapon_names     = ["Sword", "Battleaxe", "Spear", "Bow & Arrows"]
		protection_names = ["Shield", "Helmet", "Boots", "Chestplate"]
		pre_adjective    = ["Mighty ", "Fiery ", "Shiny ", "Lucky "]
		post_adjective   = [" Of the Dragon", " from Hell", " Of the damned"]

		weapon_name     = random.choice(weapon_names)
		protection_name = random.choice(protection_names)

		full_weapon     = random.choice(pre_adjective)+weapon_name+random.choice(post_adjective)
		full_protection = random.choice(pre_adjective)+protection_name+random.choice(post_adjective)


		weapon_price     = random.randint(50, 75)
		protection_price = random.randint(50, 75)

		weapon 	   = Weapon(full_weapon, weapon_price, 30)
		protection = Protection(full_protection, protection_price, 25)
		potions    = Potion(75, 3)

		list_item = (weapon, protection, potions)

		leaving = False

		available_inputs = [1,2,3,4,5]

		while (not leaving):

			self.print_items(list_item, character, available_inputs)

			item_choice = user_input(*available_inputs, is_int=True)
			if (item_choice == 5):
				print("> You are leaving the shop")
				leaving = True
			
			elif(item_choice == 4):
				available_inputs.remove(4)
				if (isinstance(character, Trader)):
					if (character.special_ability()):
						for item in list_item:
							item.price = int(0.8*item.price)
						print("> The prices went down by 20%!")
					else:
						for item in list_item:
							item.price = int(1.2*item.price)
						print("> The prices went up by 20%!")
				elif (isinstance(character, Thief)):
					if (character.special_ability() and (1 in available_inputs or 2 in available_inputs or 3 in available_inputs)):
						item = 0
						while item not in available_inputs:	
							item = random.randint(1,3)
						
						available_inputs.remove(item)
						character.add_item(list_item[item-1], free=True)
					
						print(f"> You stole the {list_item[item-1]}.")

					else:
						print("> You can't steal here, leave!")
						leaving = True
				elif (isinstance(character, Orc)):
					if (character.special_ability()):
						item = random.randint(1,3)
						available_inputs.remove(item)
						character.add_item(list_item[item-1], free=True)

						print(f"> You got the {list_item[item-1]} for free.")

					else:
						for item in list_item:
							item.price = int(1.3*item.price)
						print("> The prices went up by 30%!")
			else:
				if (character.coins >= list_item[item_choice-1].price):

					available_inputs.remove(item_choice)

					print(f"> You bought the {list_item[item_choice-1].colored_name()}!")
					character.add_item(list_item[item_choice-1])
					continue
				else: 
					print("> You don't have enough coins to buy this item")

		return 1 # signals a location event

	def print_items(self, list_item, character, available_inputs):

		print("Here are the available items :")
		for i in range(1, len(list_item)+1):
			if not (i in available_inputs):
				print(f"{bcolors.STRIKETHROUGH}{i} ▹ {list_item[i-1]}{bcolors.ENDC}")
			else:
				print(f"{i} ▹ {list_item[i-1]}")

		hability_string = f"4 ▹ {bcolors.SPECIAL_COLOR}Special hability{bcolors.ENDC} - {character.color}{character.hability}{bcolors.ENDC}"

		if (4 not in available_inputs):
			hability_string = f"{bcolors.STRIKETHROUGH}" + hability_string + f"{bcolors.ENDC}"
		print(hability_string)
		
		print("5 ▹ Exit\n")

class BlackForest(BaseLocation):

	def __init__(self):
		super().__init__("Black Forest", "F", Castle, Town)

	def entering(self):
		super().entering()
		read_art_from_file("black_forest.txt")
		print(f"> This is a dangerous forest, you might encounter some {bcolors.DAMAGE_COLOR}dangerous{bcolors.ENDC} creatures.")

	def changing_location(self):
		super().changing_location()
		location = user_input("North","South")

		if (location=="North"):
			print(f"> You are going to the {self.north_location().name} !")
			return self.north_location()
		elif(location == "South"):
			print(f"> You are going to the {self.south_location().name} !")
			return self.south_location()

	def location_event(self, character):
		
		print("> You are facing a Goblin !")

		goblin = Goblin(100, 20, 35)

		ran = False

		while (not goblin.is_defeated() and not character.is_defeated() and not ran):

			clear()
			ran = fight(character, goblin)

		if (goblin.is_defeated()):
			print("> Congratulations! You defeated the Goblin!")
			character.add_coins(goblin.coins)

		time.sleep(1)
		return 1



class Castle(BaseLocation):

	def __init__(self):
		super().__init__("Castle", "C", None, BlackForest)

	def entering(self):
		super().entering()
		read_art_from_file("castle.txt")
		print(f"> This is the great Castle! Some say there is a treasure inside it...")

	def changing_location(self):
		super().changing_location()
		location = user_input("South")

		print(f"> You are going to the {self.south_location().name} !")
		return self.south_location()


	def location_event(self, character):

		print(">The door is locked, you need a hundred coins to enter...")

		leave = False;

		while (not leave):

			if (not character.unlocked_door and not character.dragon_defeated):
				print(f"1 ▹ {bcolors.COIN_COLOR}Pay 100 coins{bcolors.ENDC}")
				print(f"2 ▹ Leave")

				choice = user_input("Pay", "Leave")

				if (choice == "Pay"):
					if (character.coins < 100):
						print("> You don't have enough coins.")
					else:
						print("> You unlocked the door...")
						character.unlocked_door = True
						time.sleep(1)
				elif (choice == "Leave"):
					print("> You are leaving the castle")
					time.sleep(1)
					leave = True

			elif (not character.dragon_defeated):
				dragon = Dragon()
				print("> You are facing the mighty dragon who keeps the treasure.")

				ran = False

				while (not dragon.is_defeated() and not character.is_defeated() and not ran):
					clear()
					ran = fight(character, dragon)

				if (dragon.is_defeated()):
					print("> Congratulations! You defeated the Great Dragon!")
					print("> A great treasure awaits you")
					character.dragon_defeated = True

				if (ran):
					leave = True
			else :

				print("> This is the great treasure, take as many coins as you wish!")
				print(f"1 ▹ {bcolors.COIN_COLOR}Take 100 coins{bcolors.ENDC}")
				print(f"2 ▹ Leave")

				choice = user_input("Take", "Leave")

				if (choice == "Take"):
					print("> You take 100 coins !")
					character.add_coins(100)
				elif (choice == "Leave"):
					print("> You are leaving the castle")
					leave = True
	time.sleep(1)
				


'''
############# // town square map example
#     C     #
#     |     #
#B <-You-> S#
#     |     #
#     P     #
#############
'''
def print_map(location):

	n = "Ø" if location.north_location==None else location.north_location().ascii_icon
	s = "Ø" if location.south_location==None else location.south_location().ascii_icon
	w = "Ø" if location.west_location==None else location.west_location().ascii_icon
	e = "Ø" if location.east_location==None else location.east_location().ascii_icon

	print(">      MAP     ")
	print("> #############")
	print(f"> #     {n}     #")
	print("> #     |     #")
	print(f"> #{w} <-You-> {e}#")
	print("> #     |     #")
	print(f"> #     {s}     #")
	print("> #############")




def fight(character, enemy):

	ran = False

	enemy.print_stats()

	print("##############################\n")

	character.print_stats()

	print("> What do you wish to do ?")
	print(f"1 ▹ {bcolors.DAMAGE_COLOR}Attack{bcolors.ENDC}")
	print(f"2 ▹ {bcolors.HEALTH_COLOR}Use a potion{bcolors.ENDC}")
	print(f"3 ▹ Run")

	user_choice = user_input("Attack","Potion", "Run")

	if (user_choice == "Attack"):
		print(f"> You attack the {enemy.name} and apply {character.base_damage} DMG to it!")
		enemy.apply_damage(character.base_damage)
	elif(user_choice=="Potion"):
		if character.has_potion():
			print(f"> You use a potion !")
			print(f"You have now {character.use_potion()} potions!")
		else:
			print("> You don't have any potions !")
	elif(user_choice=="Run"):
		print("> You try to run")
		if (random.random() < 0.75):
			print("> You failed")
		else:
			print("> You managed to run away")

			ran = True

	time.sleep(0.5)

	damages = enemy.attack()

	print(f"> The {enemy.name} attacks you and deals {damages} damages!")
	character.apply_damage(damages)	
	time.sleep(1)

	return ran