# -*- coding: utf-8 -*-
#A program to split a number into its prime factors
def pfact (n):
  facts = []
  while n % 2 == 0:
    n = n / 2
    facts.append(2)
  for divisor in range (3, n/2, 2):
    while n % divisor == 0:
      facts.append(divisor)
      n = n / divisor
  print facts

def primes (a):
  import math
  primes = [2]
  for n in range(3, a, 2):
    for x in range(2,int(math.sqrt(n))+1):
      if n % x == 0:
        break
    else:
      # loop fell through without finding a factor
      primes.append(n)

def big_pfact(n):
  facts = []
  primes ((int(n/2+1)))
  for divisor in primes:
    while n % divisor == 0:
      facts.append(divisor)
      n = n / divisor
  print facts
