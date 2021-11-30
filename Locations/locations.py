from utils import user_input, read_art_from_file


class BaseLocation():

	def __init__(self, name, ascii_icon, north_location=None, south_location=None, west_location=None, east_location=None):
		self.name = name
		self.ascii_icon = ascii_icon
		self.north_location = north_location
		self.south_location = south_location
		self.west_location = west_location
		self.east_location = east_location

	def entering(self):
		print(f"> You arrived to to the {self.name}")

	def changing_location(self):
		print("> Where do you wish to go ?")


class Plain(BaseLocation):

	def __init__(self):
		super().__init__("Plain", "P", Town)

	def entering(self):
		super().entering()
		read_art_from_file("plain.txt")
		print(f"> This is just a regular plain, you probably won't find anything interesting")

	def changing_location(self):
		super().changing_location()
		location = user_input("North")
		print(f"> You are going to the {self.north_location().name} !")
		return self.north_location()

class Town(BaseLocation):

	def __init__(self):
		super().__init__("Town Square", "T", BlackForest, Plain, Bar, Shop)

	def entering(self):
		super().entering()
		read_art_from_file("town.txt")
		print(f"> This is the Town Square!")


	def changing_location(self):
		super().changing_location()
		location = user_input("North","South","West","East")

		if (location=="North"):
			print(f"> You are going to the {self.north_location().name} !")
			return self.north_location()
		elif(location == "South"):
			print(f"> You are going to the {self.south_location().name} !")
			return self.south_location()
		elif(location == "West"):
			print(f"> You are going to the {self.west_location().name} !")
			return self.west_location()
		elif(location == "East"):
			print(f"> You are going to the {self.east_location().name} !")
			return self.east_location()



class Bar(BaseLocation):

	def __init__(self):
		super().__init__("Bar", "B", None, None, None, Town)

	def entering(self):
		super().entering()
		read_art_from_file("bar.txt")
		print(f"> Here you'll be able to buy drinks and gamble some coins")

	def changing_location(self):
		super().changing_location()
		location = user_input("East")
		print(f"> You are going to the {self.east_location().name} !")
		return self.east_location()

class Shop(BaseLocation):

	def __init__(self):
		super().__init__("Shop", "S", None, None, Town, None)

	def entering(self):
		super().entering()
		read_art_from_file("shop.txt")
		print(f"> You'll find everyting you need in this shop!")

	def changing_location(self):
		super().changing_location()
		location = user_input("West")
		print(f"> You are going to the {self.west_location().name} !")
		return self.west_location()


class BlackForest(BaseLocation):

	def __init__(self):
		super().__init__("Black Forest", "F", Castle, Town)

	def entering(self):
		super().entering()
		read_art_from_file("black_forest.txt")
		print(f"> This is a dangerous forest, you might encounter some mighty creatures")

	def changing_location(self):
		super().changing_location()
		location = user_input("North","South")

		if (location=="North"):
			print(f"> You are going to the {self.north_location().name} !")
			return self.north_location()
		elif(location == "South"):
			print(f"> You are going to the {self.south_location().name} !")
			return self.south_location()


class Castle(BaseLocation):

	def __init__(self):
		super().__init__("Castle", "C", None, BlackForest)

	def entering(self):
		super().entering()
		read_art_from_file("castle.txt")
		print(f"> This is the great Castle! Some say there is a treasure inside it...")

	def changing_location(self):
		super().changing_location()
		location = user_input("South")

		print(f"> You are going to the {self.south_location().name} !")
		return self.south_location()

'''
############# // town square map example
#     C     #
#     |     #
#B <-You-> S#
#     |     #
#     P     #
#############
'''
def print_map(location):

	n = "Ø" if location.north_location==None else location.north_location().ascii_icon
	s = "Ø" if location.south_location==None else location.south_location().ascii_icon
	w = "Ø" if location.west_location==None else location.west_location().ascii_icon
	e = "Ø" if location.east_location==None else location.east_location().ascii_icon

	print(">      MAP     ")
	print("> #############")
	print(f"> #     {n}     #")
	print("> #     |     #")
	print(f"> #{w} <-You-> {e}#")
	print("> #     |     #")
	print(f"> #     {s}     #")
	print("> #############")