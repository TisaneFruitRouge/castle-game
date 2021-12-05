from utils import bcolors

from Character.characters import Trader, Thief, Orc
from Locations.locations import Plain, Town, Bar, Shop, BlackForest, Castle
from Items.items import Weapon, Protection, Potion

# https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
def save_data(character, location):
    
    with open('c:\\Users\\wrsah\Downloads\\game\\castle-game\\save\\character.txt', 'w') as character_save:
        char_dict = dict(character.__dict__)
        char_dict["inventory"] = []
        for item in character.inventory:
            char_dict["inventory"].append(dict(item.__dict__))
        character_save.write(str(char_dict))

    with open('c:\\Users\\wrsah\Downloads\\game\\castle-game\\save\\location.txt', 'w') as location_save:
        location_save.write(location.name)

def read_character():
    with open('c:\\Users\\wrsah\Downloads\\game\\castle-game\\save\\character.txt') as character_data:
        data = eval(character_data.read())

        items_data = data["inventory"]
        items = []
        
        for item in items_data:

            if (item["color"] == bcolors.DAMAGE_COLOR):
                items.append(Weapon(item["name"],item["price"],item["attack_damage"]))
            elif (item["color"] == bcolors.HEALTH_COLOR):
                items.append(Protection(item["name"],item["price"],item["health_boost"]))
            elif (item["color"] == bcolors.POTION_COLOR):
                items.append(Potion(item["price"],item["amount"]))

        data["inventory"] = items 

        if (data["name"] == "Thief"):   
            character = Thief(data["max_health"]+20, data["base_damage"]-15, data["coins"]-20)
        elif (data["name"] == "Trader"):
            character = Trader(data["max_health"], data["base_damage"], data["coins"])
        elif (data["name"] == "Orc"):
            character = Orc(data["max_health"]-20, data["base_damage"]-10, data["coins"])

        character.inventory = data["inventory"]

        character.unlocked_door = data["unlocked_door"]
        character.dragon_defeated = data["dragon_defeated"]

        return character

def read_location():
    location_dict = {"Plain": Plain,
                     "Town": Town,
                     "Bar": Bar,
                     "Shop": Shop,
                     "BlackForest": BlackForest,
                     "Castle": Castle}

    with open('c:\\Users\\wrsah\Downloads\\game\\castle-game\\save\\location.txt') as location_data:
        data = eval(location_data.read())
        return location_dict[data]()