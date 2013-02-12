# -*- coding: utf-8 -*-
#sums the multiples of 3 & 5 smaller than a
def multiples (a):
  s = 0
  while a > 0:
    if a%5 == 0:
      s = s + a
      a = a - 1
    elif a%3 == 0:
      s = s + a
      a = a - 1
    else:
      a = a - 1
  print s

#Faster version
def multiplesum(a):
  total = 0
  for i in range (3, a, 3):
    total = total + a
  for i in range (5, a, 5):
    total = total + a
  print total