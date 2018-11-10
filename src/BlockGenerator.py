import src.BlockTypes as BlockTypes
from src.Block import Block
import random
import src.Colors as Colors

class BlockGenerator():
	def __init__(self):
		pass

	def generate(self, speed):
		generated_type = random.choice(BlockTypes.array)

<<<<<<< HEAD
		# Rotate - TODO
		width = max(map((lambda t: t[0]), generated_type)) + 32
		height = max(map((lambda t: t[1]), generated_type)) + 32
=======
        y = - height
>>>>>>> adb8ca3bcbfa5b81b64c7c1dc63c9e4e6317a049

		y = 0 - height

<<<<<<< HEAD
		# AI
=======
        x = random.randint(0,
                           (Config.SCREEN_WIDTH - width)
                           // Config.BLOCK_WIDTH) * Config.BLOCK_WIDTH
>>>>>>> adb8ca3bcbfa5b81b64c7c1dc63c9e4e6317a049

		x = random.randint(0, (sirka_okna-width)//32) * 32

		color = random.choice(Colors.colors)

<<<<<<< HEAD
		block = Block(x, y, width, height, generated_type, 
			          speed, True, color)

		return block

=======
        return block
>>>>>>> adb8ca3bcbfa5b81b64c7c1dc63c9e4e6317a049
