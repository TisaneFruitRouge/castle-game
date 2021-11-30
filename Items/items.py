from utils import bcolors

class BaseItem():

	def __init__(self, name, price):

		self.name = name
		self.price = price

		self.color = bcolors.OKBLUE

	def __str__(self):
		return f"{self.color}{self.name}{bcolors.ENDC} - Price: {self.price} coins"

	def colored_name(self):
		return f"{self.color}{self.name}{bcolors.ENDC}"

class Weapon(BaseItem):

	def __init__(self, name, price, attack_damage):
		super().__init__(name, price)
		self.attack_damage = attack_damage
		self.color = bcolors.DAMAGE_COLOR

	def __str__(self):
		return super().__str__() + f" - +{self.attack_damage} DMG"


class Protection(BaseItem):

	def __init__(self, name, price, health_boost):
		super().__init__(name, price)
		self.health_boost = health_boost
		self.color = bcolors.HEALTH_COLOR

	def __str__(self):
		return super().__str__() + f" - +{self.health_boost} MAX HP"


class Potion(BaseItem):

	def __init__(self, price, amout):
		super().__init__("Potions", price)
		self.amout = amout
		self.HP = 25
		self.color = bcolors.POTION_COLOR

	def __str__(self):
		return super().__str__() + f" - {self.amout} times +25 HP"