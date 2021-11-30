from utils import integer_input


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
		print("> 1: North - 2: South - 3: West - 4: East")


class Plain(BaseLocation):

	def __init__(self):
		super().__init__("Plain", "P", TownSquare)

	def entering(self):
		super().entering()
		print(f"> This is just a regular plain, you probably won't find anything interesting")

	def changing_location(self):
		super().changing_location()
		location = integer_input(1)
		print(f"> You are going to the {self.north_location().name} !")
		return self.north_location()

class TownSquare(BaseLocation):

	def __init__(self):
		super().__init__("Town Square", "T", BlackForest, Plain, Bar, Shop)

	def entering(self):
		super().entering()
		print(f"> This is the Town Square!")


	def changing_location(self):
		super().changing_location()
		location = integer_input(1,2,3,4)

		if (location==1):
			print(f"> You are going to the {self.north_location().name} !")
			return self.north_location()
		elif(location == 2):
			print(f"> You are going to the {self.south_location().name} !")
			return self.south_location()
		elif(location == 3):
			print(f"> You are going to the {self.west_location().name} !")
			return self.west_location()
		elif(location == 4):
			print(f"> You are going to the {self.east_location().name} !")
			return self.east_location()



class Bar(BaseLocation):

	def __init__(self):
		super().__init__("Bar", "B", None, None, None, TownSquare)

	def entering(self):
		super().entering()
		print(f"> Here you'll be able to buy drinks and gamble some coins")

	def changing_location(self):
		super().changing_location()
		location = integer_input(4)
		print(f"> You are going to the {self.east_location().name} !")
		return self.east_location()

class Shop(BaseLocation):

	def __init__(self):
		super().__init__("Shop", "S", None, None, TownSquare, None)

	def entering(self):
		super().entering()
		print(f"> You'll find everyting you need in this shop!")

	def changing_location(self):
		super().changing_location()
		location = integer_input(3)
		print(f"> You are going to the {self.west_location().name} !")
		return self.west_location()


class BlackForest(BaseLocation):

	def __init__(self):
		super().__init__("Black Forest", "F", Castle, TownSquare)

	def entering(self):
		super().entering()
		print(f"> This is a dangerous forest, you might encounter some mighty creatures")

	def changing_location(self):
		super().changing_location()
		location = integer_input(1,2)

		if (location==1):
			print(f"> You are going to the {self.north_location().name} !")
			return self.north_location()
		elif(location == 2):
			print(f"> You are going to the {self.south_location().name} !")
			return self.south_location()


class Castle(BaseLocation):

	def __init__(self):
		super().__init__("Castle", "C", None, BlackForest)

	def entering(self):
		super().entering()
		print(f"> This is the great Castle! Some say there is a treasure inside it...")

	def changing_location(self):
		super().changing_location()
		location = integer_input(1,2,3,4)

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