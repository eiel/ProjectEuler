# -*- coding: utf-8 -*-

def sum_of_fibonacci(a, b) :
	item = a + b
	if item > 4000000 :
		return 0

	sum_of_item = 0
	if item % 2 == 0 :
		sum_of_item = item

	return sum_of_item + sum_of_fibonacci(b, item)

if __name__ == '__main__' :
	print sum_of_fibonacci(0, 1)