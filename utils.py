import os

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
def clear():
    os.system('cls' if os.name=='nt' else 'clear')



class default_values:

    HEALTH = 100
    DAMAGE = 20
    COINS = 100

def integer_input(*options):

    print("> You may choose one of these options", end=": ")
    for option in options:
        print(option, end=" ")
    print("\n")

    raw_user_input = input("> Your choice: ")

    try:
        user_input = int(raw_user_input)
        assert user_input in options
    except (ValueError, TypeError, AssertionError):
        print("> Bad input, try again")
        user_input = integer_input(*options)
    else:
        return user_input    

    
