# -*- coding: utf-8 -*-
import sys

def factorize_of_prime(num, list) :
	for val in list :
		if num % val == 0 :
			num = num / val;

	if num != 1 :
		list.append(num)

if __name__ == '__main__':
	max = 20
	if len(sys.argv) > 1 and sys.argv[1].isdigit() :
		max = int(sys.argv[1])

	list = [1]
	for i in range(1, max + 1) :
		factorize_of_prime(i, list)

	val = 1
	for num in list :
		val *= num

	print val


