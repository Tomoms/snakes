#!/usr/bin/env python3

import numpy as np
import sys
from Snake import Snake

def parse_input(filename):
	matrix = np.loadtxt(filename, skiprows=2)
	print(matrix)

if __name__ == "__main__":
	if len(sys.argv) == 1:
		filename = "input"
	else:
		filename = str(sys.argv[1])
	parse_input(filename)
	with open(filename, "r") as fp:
		snakes_data = np.array(fp.readlines()[1].split()).astype(np.int64)
	print(snakes_data)
	print("\n\n\n")

	snakes = [Snake(length) for length in snakes_data]
	line = 0
	for snake in snakes:
		snake.place(line, 0)
		line += 1

	for snake in snakes:
		print(snake)
		print(snake.output())
