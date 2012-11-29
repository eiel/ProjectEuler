# -*- coding: utf-8 -*-
import sys
import math

def is_prime(val) :
	if val == 1 : return 0
	if val == 2 : return val
	if val == 3 : return val
	if val % 2 == 0 : return 0

	for i in range(3, int(math.sqrt(val)) + 1, 2) :
		if val % i == 0 : return 0

	return val


if __name__ == '__main__' :
	max = 2000000
	if len(sys.argv) > 1 and sys.argv[1].isdigit() :
		max = int(sys.argv[1])

	print sum(is_prime(i) for i in range(1, max + 1))
