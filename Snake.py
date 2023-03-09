import math
import numpy as np

class Snake:

	def __init__(self, length):
		self.length = length
		self.cells = list()

	def place(self, matrix, nans, row, col):
		self.cells.append((row, col))
		cur_row = row
		cur_col = col
		matrix[cur_row][cur_col] = np.NINF
		for i in range(self.length - 1):
			direction = 1 # 1 = right, 2 = down, 3 = left, 4 = up
			val = matrix[cur_row][cur_col + 1]
			if val == np.NINF:
				direction = 2
				val = matrix[cur_row + 1][cur_col]
			if not math.isnan(val):
				matrix[cur_row][cur_col + 1] = np.NINF
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
