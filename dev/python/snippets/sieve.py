# -*- coding: utf-8 -*-
#Sieve of Erastothanes
def sieve (n):
  multiples = []
  primes = []
  for i in range (2, n+1):
    if i not in multiples:
      primes.append(i)
      for j in xrange (i*i, n+1, i):
        multiples.append(j)
      i = i + 1
    else:
      i = i + 1
  return primes

#An alternative sieve implementation: uglier but more efficient
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
  print(primes)