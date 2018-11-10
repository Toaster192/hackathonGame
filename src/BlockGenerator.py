import src.BlockTypes as BlockTypes
from src.Block import Block
import random
import src.Colors as Colors
import src.Config as Config


class BlockGenerator():
    def __init__(self):
        pass

    def generate(self, speed):
        generated_type = random.choice(BlockTypes.array)

        # Rotate - TODO
        width = max(map((lambda t: t[0]),
                        generated_type)) + Config.BLOCK_WIDTH
        height = max(map((lambda t: t[1]),
                         generated_type)) + Config.BLOCK_WIDTH

<<<<<<< HEAD
		# Rotate - TODO
		width = max(map((lambda t: t[0]), generated_type)) + 32
		height = max(map((lambda t: t[1]), generated_type)) + 32
=======
        y = - height
>>>>>>> 0e6bbc0cfb125b7712d095c63ff3065e9230d79d

        # AI

<<<<<<< HEAD
		# AI
=======
        x = random.randint(0,
                           (Config.SCREEN_WIDTH - width)
                           // Config.BLOCK_WIDTH) * Config.BLOCK_WIDTH
>>>>>>> 0e6bbc0cfb125b7712d095c63ff3065e9230d79d

        color = random.choice(Colors.colors)

        block = Block(x, y, width, height, generated_type,
                      speed, "active", color)

<<<<<<< HEAD
		block = Block(x, y, width, height, generated_type, 
			          speed, "falling", color)

		return block

=======
        return block
>>>>>>> 0e6bbc0cfb125b7712d095c63ff3065e9230d79d
