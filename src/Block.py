from src.Square import Square

class Block(GameObject):
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

		self.objects = map(lambda t: createBlock(t[0], t[1]), array)

	def createBlock(self, x, y):
		return Square(self.x+x, self.y+y, self.color)

	def move(self, dt):
		for square in self.objects:
			square.update(dt)