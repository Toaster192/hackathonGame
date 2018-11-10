import src.BlockTypes as BlockTypes
from src.Block import Block
import random
import src.Colors as Colors

class BlockGenerator():
	def __init__(self):
		pass

	def generate(self, speed):
		generated_type = random.choice(BlockTypes.array)

		# Rotate - TODO
		width = max(map((lambda t: t[0]), generated_type)) + 32
		height = max(map((lambda t: t[1]), generated_type)) + 32

		y = 0 - height

		# AI

		x = random.randint(0, (sirka_okna-width)//32) * 32

		color = random.choice(Colors.colors)

		block = Block(x, y, width, height, generated_type, 
			          speed, "falling", color)

		return block

