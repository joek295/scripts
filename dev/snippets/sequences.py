# -*- coding: utf-8 -*-
#Sequences
def triangle(n):
  triangles = []
  for x in range (1,n):
    triangle.append((x**2+x)/2)
  return triangles
    
#specific fibonnaci sequence
def fib(n):
  fibo = [1, 1]
  for i in range (1, n):
    fibo.append(fibo[-1] + fibo[-2])
  print fibo

#general fibonnaci
def genfib (a, b, n):
  fibo = [a, b]
  for i in range (1, n):
    fibo.append(fibo[-1] + fibo[-2])
  print fibo
    
