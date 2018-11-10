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

        y = - height

        # AI

        x = random.randint(0,
                           (Config.SCREEN_WIDTH - width)
                           // Config.BLOCK_WIDTH) * Config.BLOCK_WIDTH

        color = random.choice(Colors.colors)

        block = Block(x, y, width, height, generated_type,
                      speed, "active", color)

        return block
