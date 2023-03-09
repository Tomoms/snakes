class Snake:

	def __init__(self, length):
		self.length = length
		self.cells = list()

	def place(self, row, col):
		for i in range(self.length):
			self.cells.append((row, col + i))

	def __str__(self):
		string = "This snake has length {} ".format(self.length)
		string += "Positions: "
		for cell in self.cells:
			string += str(cell) + "; "
		return string

	def output(self):
		string = "{} {} ".format(self.cells[0][1], self.cells[0][0])
		for i in range(self.length - 1):
			string += "R "
		string.strip()
		return string
