# -*- coding: utf-8 -*-
import sys

def calc_double(max) :
	double1 = 0
	double2 = 0
	for num in range(1, max + 1):
		double1 += (num * num)
		double2 += num

	double2 = double2 * double2

	return double2 - double1

if __name__ == '__main__' :
	max = 100
	if len(sys.argv) > 1 and sys.argv[1].isdigit() :
		max = int(sys.argv[1])

	print calc_double(max)
