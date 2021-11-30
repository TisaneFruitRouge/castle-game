from .characters import Thief, Trader, Orc

from utils import bcolors, user_input, default_values

def choose_charater():

	print(f"> You can choose between {bcolors.BOLD}3{bcolors.ENDC} characters:\n")
	print(f"1 ▹ {bcolors.TRADER_COLOR}Trader{bcolors.ENDC}")
	print(f"2 ▹ {bcolors.THIEF_COLOR}Thief{bcolors.ENDC}")
	print(f"3 ▹ {bcolors.ORC_COLOR}Orc\n{bcolors.ENDC}\n")

	character_choice = user_input(1,2,3, is_int=True)

	print("> You chose: ", end="")
	if (character_choice == 1):
		print(f"{bcolors.TRADER_COLOR}Trader{bcolors.ENDC}\n")
	elif (character_choice == 2):
		print(f"2 ▹ {bcolors.THIEF_COLOR}Thief{bcolors.ENDC}\n")
	elif (character_choice == 3):
		print(f"3 ▹ {bcolors.ORC_COLOR}Orc{bcolors.ENDC}\n")

	print(f"> Now, you need to select {bcolors.BOLD}2{bcolors.ENDC} of the three following runes:\n")
	print(f"1 ▹ {bcolors.COIN_COLOR}Gold Rune{bcolors.ENDC} (+ 50 additional coins)")
	print(f"2 ▹ {bcolors.HEALTH_COLOR}Life Rune{bcolors.ENDC} (+ 15 maximum health)")
	print(f"3 ▹ {bcolors.DAMAGE_COLOR}Damage Rune{bcolors.ENDC} (+10 damage)\n")

	print(f"{bcolors.UNDERLINE}NOTE:{bcolors.ENDC} choose the rune you {bcolors.BOLD}DO NOT{bcolors.ENDC} want!\n")

	rune_choice = user_input(1,2,3, is_int=True)

	print("> You didn't choose the ", end="")
	if (rune_choice == 1):
		print(f"{bcolors.COIN_COLOR}Gold Rune{bcolors.ENDC}\n")
	elif (rune_choice == 2):
		print(f"2 ▹ {bcolors.HEALTH_COLOR}Life Rune{bcolors.ENDC}\n")
	elif (rune_choice == 3):
		print(f"3 ▹ {bcolors.DAMAGE_COLOR}Damage Rune{bcolors.ENDC}\n")

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