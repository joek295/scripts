# -*- coding: utf-8 -*-
#Program to find sum of even fibonacci numbers < n
def fibo (n):
  s = 0
  a, b = 0, 1
  while a < n:
    if a % 2 == 0:
      s = s + a
    a, b = b, a+b
  print s
