from .characters import Thief, Trader, Orc

from utils import bcolors, integer_input, default_values

def choose_charater():

	print(f"> You can choose between {bcolors.BOLD}3{bcolors.ENDC} characters:\n")
	print(f"1 ▹ {bcolors.TRADER_COLOR}Trader{bcolors.ENDC}\n")
	print(f"2 ▹ {bcolors.THIEF_COLOR}Thief{bcolors.ENDC}\n")
	print(f"3 ▹ {bcolors.ORC_COLOR}Orc\n{bcolors.ENDC}\n")

	character_choice = integer_input(1,2,3)

	print("> You chose: ", end="")
	if (character_choice == 1):
		print(f"{bcolors.TRADER_COLOR}Trader{bcolors.ENDC}\n")
	elif (character_choice == 2):
		print(f"2 ▹ {bcolors.THIEF_COLOR}Thief{bcolors.ENDC}\n")
	elif (character_choice == 3):
		print(f"3 ▹ {bcolors.ORC_COLOR}Orc\n{bcolors.ENDC}\n")

	print(f"> Now, you need to select {bcolors.BOLD}2{bcolors.ENDC} of the three following runes:\n")
	print(f"1 ▹ {bcolors.GOLD_RUNE_COLOR}Gold Rune{bcolors.ENDC} (+ 50 additional coins)\n")
	print(f"2 ▹ {bcolors.LIFE_RUNE_COLOR}Life Rune{bcolors.ENDC} (+ 15 maximum health)\n")
	print(f"3 ▹ {bcolors.DAMAGE_RUNE_COLOR}Damage Rune\n{bcolors.ENDC} (+10 damage)\n")

	print(f"{bcolors.UNDERLINE}NOTE:{bcolors.ENDC} choose the rune you {bcolors.BOLD}DO NOT{bcolors.ENDC} want!\n")

	rune_choice = integer_input(1,2,3)

	max_health = default_values.HEALTH
	damage = default_values.DAMAGE
	coins  = default_values.COINS

	if (rune_choice == 1):
		max_health+=15
		damage+=10
	elif(rune_choice == 2):
		coins+=50
		damage+=10
	elif(rune_choice == 3):
		max_health+=15
		damage+=10

	if (character_choice==1):
		return Trader(max_health, damage, coins)
	elif (character_choice==2):
		return Thief(max_health, damage, coins)
	elif (character_choice==3):
		return Orc(max_health, damage, coins)