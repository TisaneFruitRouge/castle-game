import os, sys

from Character.meta import choose_charater
from Locations.locations import Plain, Town, Bar, Shop, BlackForest, Castle 
from Locations.locations import print_map

from utils import bcolors, clear, read_art_from_file

from save.save import save_data, read_save

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
	
	print("What is you name ?", end=" ")
	name = input() 

	if (os.path.isfile(f'save/{name}.txt') and not os.stat(f'save/{name}.txt').st_size == 0):
		character, location = read_save(name)
		print(f"> Welcome back, {name}...")
		clear(1.5)
	else: 
		character = choose_charater(name)
		location = Plain()
		print(f"> Welcome, {character.username}...")
		clear(1.5)
	
	exit = False

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
		save_data(character, location, character.username)
		clear()

if __name__ == "__main__":
	main()