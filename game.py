import os

from Character.meta import choose_charater

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():

	print(f"{bcolors.OKCYAN}################ Welcome to the Castle Game ################{bcolors.ENDC}")
	print("\tFirst, you need to choose you character:")
	
	character = choose_charater()

if __name__ == "__main__":
	main()