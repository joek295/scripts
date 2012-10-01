# -*- coding: utf-8 -*-
#finds difference between sum of squares and square of sums
def sumsq (x):
  a = 0
  b = 0
  while x > 0:
    a = a + x**2
    b = b + x
    x = x - 1
  b = b**2
  print b - a
