# -*- coding: utf-8 -*-
import sys

primes = []

def check_prime(val) :
	for num in primes :
		if val % num == 0 :
			return 0

	primes.append(val)
	return 1

if __name__ == '__main__' :
	
	max = 10001
	if len(sys.argv) > 1 and sys.argv[1].isdigit() :
		max = int(sys.argv[1])

	val = 2
	while 1 :
		if check_prime(val) :
			if len(primes) == max :
				print val
				break

		val += 1






