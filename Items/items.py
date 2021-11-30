

class BaseItem():

	def __init__(self, name, price)

		self.name = name
		self.price = price


class Weapon(BaseItem);

	def __init__(self, name, price, attack_damage):
		super().__init__(name, price)
		self.attack_damage = attack_damage


class Protection(BaseItem);

	def __init__(self, name, price, health_boost):
		super().__init__(name, price)
		self.health_boost = health_boost

class Potion(BaseItem):

	def __init__(self, name, price, amout)
		super().__init__(name, price)
		self.amout = amout
		self.HP = 25