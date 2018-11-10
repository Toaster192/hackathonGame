import src.Config as Config

L = ((0, 0), (1*Config.BLOCK_WIDTH, 0), (2*Config.BLOCK_WIDTH, 0), (0, 1*Config.BLOCK_WIDTH))
O = ((0, 0), (0, 1*Config.BLOCK_WIDTH), (1*Config.BLOCK_WIDTH, 0), (1*Config.BLOCK_WIDTH, 1*Config.BLOCK_WIDTH))
Z = ((0, 0), (0, 1*Config.BLOCK_WIDTH), (1*Config.BLOCK_WIDTH, 1*Config.BLOCK_WIDTH), (1*Config.BLOCK_WIDTH, 2*Config.BLOCK_WIDTH))
I = ((0, 0), (0, 1*Config.BLOCK_WIDTH), (0, 2*Config.BLOCK_WIDTH), (0, 3*Config.BLOCK_WIDTH))
T = ((0, 0), (0, 1*Config.BLOCK_WIDTH), (0, 2*Config.BLOCK_WIDTH), (1*Config.BLOCK_WIDTH, 1*Config.BLOCK_WIDTH))

array = (L, O, Z, I, T)
