# -*- coding: utf-8 -*-
import math
#A module implementing simple statistical analysis of numerical data
#All these functions are now complete (pending testing)
def mean (data):
  number = len(data)
  sigma_x = sum(data)
  xbar = number / sigma_x
  print xbar
  
def median (data):
  number = len(data)
  data1 = data.sort
  if number%2 = 0:
    middle1 = data1.pop(n/2)
    middle2 = data1.pop(n/2+1)
    median = (middle1+middle2)/2.0
  else:
    middle = data1.pop(number/2+1)
    median = middle
  print median

def mode (data):
  a = 0
  for i in data:
    b = count i
    if b > a:
      b = a
      current_mode = [i, b]
  return current_mode
  
def datarange (data):
  number = len(data)
  data1 = data.sort
  Range = data1.pop(number+1) - data1.pop(0)
  print Range
  
def midrange (data):
  midrange = ( max (data) + min (data) ) /2
  print midrange
  
def sxx (data):
  listsqr = [n**2 for n in data]
  sxx = sum(listsqr) - len(data) * mean(data)**2
  print sxx
  
def standarddev (data):
  sigma = math.sqrt(sxx(data))/(len(data)-1)
  print sigma
  
def variance (data):
  v = sxx(data)/(len(data)-1)
  print v
  
def msd (data):
  msd = sxx(data)/len(data)
  print msd
  
def rmsd (data):
  rmsd = math.sqrt(msd(data))
  print rmsd

def bin_equal(n, p, r):
  nCr = (math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
  X = nCr*(p**r)*((1-p)**(n-r))
  return X

def bin_less (n,p,r):
  while n + 1 > 0:
      nCr = (math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
      X = nCr*(p**r)*((1-p)**(n-r))
      P = p+X
  return P

def bin_more (n, p, r):
  P_more = 1 - bin_less(n,p,r)
  return P_more

#To be coded:
#Chi-Squared, Poisson Distribution, Normal Distribution, PMCC, Spearman's Rank