# -*- coding: utf-8 -*-
#Program to find the factorial of n
def factorial (n):
	if n == 0:
		return 1
	fact = n
	while n>1:
		fact = fact*(n - 1)
		n = n - 1
	print fact
	