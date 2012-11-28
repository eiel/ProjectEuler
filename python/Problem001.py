# -*- coding: utf-8 -*-
import sys

def sum_multiple_of_3_or_5(max) :
	result = 0
	for i in range(1, max) :
		if i % 3 == 0 or i % 5 == 0 :
			result += i

	return result

if __name__ == '__main__' :
	max = 1000
	if len(sys.argv) > 1 and sys.argv[1].isdigit() :
		max = int(sys.argv[1])

	print sum_multiple_of_3_or_5(max)

