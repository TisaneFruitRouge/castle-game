

class BaseLocation():

	def __init__(self, name, north_location=None, south_location=None, west_location=None, east_location=None):
		self.name = name
		self.north_location = north_location
		self.south_location = south_location
		self.west_location = west_location
		self.east_location = east_location