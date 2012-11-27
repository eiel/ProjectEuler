# -*- coding: utf-8 -*-
import sys

def factorize_of_prime(value, factory) :
	if value / 2 <= factory :
		return value

	while value % factory == 0 :
		value = value / factory
		if value <= factory :
			return factory

	factory = factory + 1
	while factory % 2 == 0 or (factory != 3 and factory % 3 == 0) or (factory != 5 and factory % 5 == 0):
		factory = factory + 1

	return factorize_of_prime(value, factory)


if __name__ == '__main__' :
	size = 13195
	if len(sys.argv) > 1 and sys.argv[1].isdigit() :
		size = int(sys.argv[1])

	print factorize_of_prime(size, 2)
