from .characters import Thief, Trader, Orc

from utils import bcolors, integer_input

def choose_charater():

	print(f"You can choose between {bcolors.BOLD}3{bcolors.ENDC} characters:\n")
	print(f"1 ▹ {bcolors.TRADER_COLOR}Trader{bcolors.ENDC}\n")
	print(f"2 ▹ {bcolors.THIEF_COLOR}Thief{bcolors.ENDC}\n")
	print(f"3 ▹ {bcolors.ORC_COLOR}Orc\n{bcolors.ENDC}\n")

	character_choice = integer_input(1,2,3)

	print("You chose: ", end="")
	if (character_choice == 1):
		print(f"{bcolors.TRADER_COLOR}Trader{bcolors.ENDC}\n")
	elif (character_choice == 2):
		print(f"2 ▹ {bcolors.THIEF_COLOR}Thief{bcolors.ENDC}\n")
	elif (character_choice == 3):
		print(f"3 ▹ {bcolors.ORC_COLOR}Orc\n{bcolors.ENDC}\n")

	print(f"Now, you need to select {bcolors.BOLD}2{bcolors.ENDC} of the three following runes:\n")
	print(f"1 ▹ {bcolors.GOLD_RUNE_COLOR}Gold Rune{bcolors.ENDC}\n")
	print(f"2 ▹ {bcolors.LIFE_RUNE_COLOR}Life Rune{bcolors.ENDC}\n")
	print(f"3 ▹ {bcolors.DAMAGE_RUNE_COLOR}Damage Rune\n{bcolors.ENDC}\n")