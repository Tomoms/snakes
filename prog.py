#!/usr/bin/env python3

import numpy as np
import sys
import math
from Snake import Snake

def parse_input(filename):
	matrix = np.loadtxt(filename, skiprows=2)
	return matrix

def find_nans(matrix):
	result = list()
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if math.isnan(matrix[row][col]):
				result.append((row, col))
	return result

if __name__ == "__main__":
	if len(sys.argv) == 1:
		filename = "input"
	else:
		filename = str(sys.argv[1])
	matrix = parse_input(filename)
	nans = find_nans(matrix)
	with open(filename, "r") as fp:
		snakes_data = np.array(fp.readlines()[1].split()).astype(np.int64)
	print(snakes_data)
	print("\n\n\n")

	snakes = [Snake(length) for length in snakes_data]
	line = 0
	for snake in snakes:
		snake.place(matrix, nans, line, 0)
		line += 1

	for snake in snakes:
		print(snake)
		print(snake.output())
	print(matrix)
