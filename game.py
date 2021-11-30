import os

from Character.meta import choose_charater
from utils import bcolors

def main():

	print(f"{bcolors.OKCYAN}################ Welcome to the Castle Game ################{bcolors.ENDC}")
	print("\tFirst, you need to choose you character:")
	
	character_choice = choose_charater()

if __name__ == "__main__":
	main()