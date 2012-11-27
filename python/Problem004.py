# -*- coding: utf-8 -*-

def calc_palindrome(val, max) :
	if val * 999 < max :
		return max

	result = -1
	for i in range(999, 99, -1) :
		num = val * i
		if str(num) == str(num)[::-1] :
			result = num
			break;

	if result < max :
		result = max

	if val == 100 :
		return result

	return calc_palindrome(val - 1, result)

if __name__ == '__main__' :
	print calc_palindrome(999, -1)
