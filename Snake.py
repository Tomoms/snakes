import math

class Snake:

	def __init__(self, length):
		self.length = length
		self.cells = list()

	def place(self, matrix, nans, row, col):
		self.cells.append((row, col))
		cur_row = row
		cur_col = col
		for i in range(self.length - 1):
			val = matrix[cur_row][cur_col + 1]
			self.cells.append((cur_row, cur_col + 1))
			if math.isnan(val):
				cur_nan_idx = nans.index((cur_row, cur_col + 1))
				next_nan_idx = (cur_nan_idx + 1) % len(nans)
				cur_row = nans[next_nan_idx][0]
				cur_col = nans[next_nan_idx][1]
			cur_col += 1

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
