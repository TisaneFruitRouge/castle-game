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

    GOLD_RUNE_COLOR = '\033[93m'
    LIFE_RUNE_COLOR = '\033[95m'
    DAMAGE_RUNE_COLOR = '\033[91m'


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

    
