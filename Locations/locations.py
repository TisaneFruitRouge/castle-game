import random

from utils import user_input, range_input, read_art_from_file, bcolors
from Items.items import Weapon, Protection, Potion

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
		super().__init__("Town Square", "T", BlackForest, Plain, Bar, Shop)

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

		print("Here are the available items :")
		print(f"1 ▹ {weapon}")
		print(f"2 ▹ {protection}")
		print(f"3 ▹ {potions}\n")
		print("4 ▹ Exit")

		leaving = False

		available_inputs = [1,2,3,4]

		while (not leaving):
			item_choice = user_input(*available_inputs, is_int=True)
			if (item_choice == 4):
				print("> You are leaving the shop")
				leaving = True

			else:
				if (character.coins >= list_item[item_choice-1].price):

					available_inputs.remove(item_choice)

					print(f"> You bought the {list_item[item_choice-1].colored_name()}!")
					character.add_item(list_item[item_choice-1])
					continue
				else: 
					print("> You don't have enough coins to buy this item")

		return 1 # signals a location event


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