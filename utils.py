import os
import time

# Found it here : https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
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

    TRADER_COLOR = '\033[92m'
    THIEF_COLOR = '\033[93m'
    ORC_COLOR = '\033[91m'

    COIN_COLOR   = '\033[93m'
    HEALTH_COLOR = '\033[95m'
    DAMAGE_COLOR = '\033[91m'


# Found it here : https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console?page=1&tab=votes#tab-top
def clear(timeout=0):
    time.sleep(timeout)
    os.system('cls' if os.name=='nt' else 'clear')

def read_art_from_file(filename):
    file = open(f'ascii_arts/{filename}', 'r')
    art = file.read()
    print(art)
    file.close()


class default_values:

    HEALTH = 100
    DAMAGE = 20
    COINS = 100

def user_input(*options, is_int=False):

    print("> You may choose one of these options", end=": ")
    for option in options:
        print(option, end=" ")
    print("\n")
    raw_user_input = input("> Your choice: ")

    try:
        if is_int:
            the_user_input = int(raw_user_input)
            assert the_user_input in options
        else:
            the_user_input = raw_user_input
            assert the_user_input.lower() in [option.lower() for option in options] 
            # we lower everything to avoid problems with capital letters
    
    except (ValueError, TypeError, AssertionError):
        print("> Bad input, try again")
        the_user_input = user_input(*options, is_int=is_int)
    else:
        return the_user_input    

    
