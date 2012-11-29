# -*- coding: utf-8 -*-

def calc_pythagorean() :
	for a in range(1, 1000) :
		for b in range(a + 1, 1000) :
			c = 1000 - (a + b)

			if c < b : break

			if a**2 + b**2 - c**2 == 0 :
				print "a = ",
				print a,
				print ", b = ",
				print b,
				print ", c = ",
				print c
				print "a * b * c = ",
				print a * b * c
				return 0



if __name__ == '__main__' :
	calc_pythagorean()
