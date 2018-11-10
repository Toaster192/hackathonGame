from src.Square import Square


class Block(GameObject):
<<<<<<< HEAD
	def __init__(self, x, y, width, height, array, speed, falling, color):
		GameObject.__init__(self, x, y, width, height, speed)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.array = array
		self.speed = speed
		self.falling = falling
		self.color = color
=======
    def __init__(self, x, y, width, height, array, speed, state, color):
        GameObject.__init__(self, x, y, width, height, speed)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.array = array
        self.speed = speed
        self.state = state
        self.color = color
>>>>>>> 0e6bbc0cfb125b7712d095c63ff3065e9230d79d

        self.objects = map(lambda t: createBlock(t[0], t[1]), array)

    def createBlock(self, x, y):
        return Square(self.x+x, self.y+y, self.color)

<<<<<<< HEAD
	def move(self, dt):
		for square in self.objects:
			if !square.detects_collision():
				square.update(dt)
			elif square.detects_collision() && self.falling == True:
				self.falling = False
				self.speed = self.speed / 2
				square.update(dt)
			else square.detects_collision() && self.falling == False:
				square.update(dt)


				




=======
    def move(self, dt):
        for square in self.objects:
            square.update(dt)
>>>>>>> 0e6bbc0cfb125b7712d095c63ff3065e9230d79d
