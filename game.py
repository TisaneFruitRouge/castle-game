import os, sys

from Character.meta import choose_charater
from Locations.locations import Plain, Town, Bar, Shop, BlackForest, Castle 
from Locations.locations import print_map

from utils import bcolors, clear, read_art_from_file

from save.save import save_data, read_character, read_location

### All the ASCII Art comes from www.asciiart.eu

'''
	Exit function (also used to save the infos in a file)
'''
def exit():
	return


def resume(character, location):
	location.entering() # entering the location
	print('\n')
	print_map(location) # printing the map
	print('\n')
	character.print_stats()
	print('\n')
	character.show_inventory()
	print('\n')
'''
	Function where the game loops exists
'''
def main():

	print(f"{bcolors.OKCYAN}################ Welcome to Treasure Hunt in Castle ################{bcolors.ENDC}")
	
	if (os.path.isfile('save/character.json')):
		character = read_character()
	else: 
		character = choose_charater()
	
	if (os.path.isfile('save/location.json')):
		location = read_location()
	else: 
		location = Plain()

	exit = False

	print("> Welcome, adventurer...")
	clear(2)

	while (not exit):
		if (character.is_defeated()):
			read_art_from_file("death.txt")
			print(f"{bcolors.DAMAGE_COLOR}###############################YOU DIED###############################{bcolors.ENDC}")
			sys.exit(0)

		resume(character, location)

		if (location.location_event(character)): # triggering a location event
			clear()
			resume(character, location)
		else: 
			...

		location = location.changing_location()
		save_data(character, location)
		clear()

if __name__ == "__main__":
	main()