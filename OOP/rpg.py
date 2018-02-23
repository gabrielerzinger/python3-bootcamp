class Character:
	@property
	def name(self):
		return self._name

	@property
	def hp(self):
		return self._hp

	@property
	def level(self):
		return self._level
		
	def __init__(self, name, hp, level):
		self._name = name
		if hp >= 0 and level >= 0:
			self._hp = hp
			self._level = level
		else:
			raise ValueError("Hp and level must be greater than 0")


class NPC(Character):
	def __init__(self, name, hp, level):
		super().__init__(name, hp, level)

	def speak(self):
		print("I heard there were monsters running around last night!")


villager = NPC("Bob", 10, 12)
villager.name  # Bob
villager.hp  # 100
villager.level  # 12
villager.speak()  # "I heard there were monsters running around last night!".