import random

import src.BlockTypes as BlockTypes
import src.Colors as Colors
import src.Config as Config
from src.Block import Block
from src.StaticStore import StaticStore


class BlockGenerator():
    def __init__(self):
        pass

    @staticmethod
    def generate(speed):
        generated_type = random.choice(BlockTypes.array)

        width = max(map((lambda t: t[0]),
                        generated_type)) + Config.BLOCK_WIDTH
        height = max(map((lambda t: t[1]),
                         generated_type)) + Config.BLOCK_WIDTH

        y = -StaticStore.offset.y - height
        # print(Config.GAMEFIELD_LEFT_BORDER)
        # print(Config.GAMEFIELD_RIGHT_BORDER - width)
        x = (Config.GAMEFIELD_LEFT_BORDER +
             random.randint(0, 16 - width // Config.BLOCK_WIDTH) *
             Config.BLOCK_WIDTH)

        color = random.choice(Colors.colors)

        block = Block(float(x), float(y),
                      float(width), float(height),
                      generated_type, speed,
                      True, color)

        return block
