class Tank(object):

	def __init__(self, name):
		self.name = name
		self.alive = True
		self.armour = 60
		self.ammo = 5

	def __str__(self):
		if self.alive:
			return "%s (%i armour %i shells)" % (self.name, self.armour, self.ammo)
		else:
			return "%s is dead" % (self.name)

	def fire_at(self, enemy):
		if self.ammo >= 1:
			self.ammo -= 1
			print(self.name, "fires on", enemy.name)
			enemy.hit()

	def hit(self):
		self.armour -= 20
		print(self.name, "is hit!")
		if self.armour <= 0:
			self.explode()

	def explode(self):
		self.alive = False
		print(self.name,"explodes")