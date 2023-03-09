#!/usr/bin/env python3

import numpy as np
import sys

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
		snakes = str(fp[1]).split()
	print(snakes)
