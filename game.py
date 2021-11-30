import os

from Character.meta import choose_charater
from utils import bcolors

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
	
	character_choice = choose_charater()

	exit = False

	print("> Welcome, adventurer...")

	while (not exit):

		
		


if __name__ == "__main__":
	main()