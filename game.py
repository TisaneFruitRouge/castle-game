import os

from Character.meta import choose_charater
from Locations.locations import Plain, TownSquare, Bar, Shop, BlackForest, Castle 
from Locations.locations import print_map

from utils import bcolors, clear

'''
	Exit function (also used to save the infos in a file)
'''
def exit():
	return

'''
	Function where the game loops exists
'''
def main():

	print(f"{bcolors.OKCYAN}################ Welcome to the Castle Game ################{bcolors.ENDC}")
	print("> First, you need to choose you character:")
	
	character = choose_charater()
	location = Plain()

	exit = False

	print("> Welcome, adventurer...")

	while (not exit):

		location.entering()
		print_map(location)
		location = location.changing_location()



		clear()

if __name__ == "__main__":
	main()