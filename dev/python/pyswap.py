#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PySwap: A program to parse SiteSwap notation
#Version 1.01
# ERROR: l 158: section lines 122-167

import time
import collections

rhballs = collections.deque([])
lhballs = collections.deque([])
airballs = []
to_hand = []
b = []

def welcome():
  print "Welcome to PySwap, a text-based siteswap interpreter."
  print '''To read about siteswap, press 1. To interpret a siteswap pattern, press 2. 
For version information, press 9. To exit, press 0.'''
  choice = int(raw_input())
  if choice == 1:
    pass
    #Link to an introduction to siteswap.
  elif choice == 2:
    pattern = str(raw_input("SiteSwap pattern to interpret?"))
    start_hand = str(raw_input("Which hand should start the pattern? L or R?"))
    interpret(pattern, start_hand)
  elif choice == 9:
    version()
  elif choice == 0:
    quit()
  else:
    print "Not currently a valid option."
    quiet_welcome()
      
def quiet_welcome():
  choice = int(raw_input("Please choose another option."))
  if choice == 1:
    pass
  elif choice == 2:
    pattern = str(raw_input("SiteSwap pattern to interpret?"))
    start_hand = str(raw_input("Which hand should start the pattern? L or R?"))
    interpret(pattern, start_hand)
  elif choice == 9:
    version()
  elif choice == 0:
    quit()
  else:
    print "Not currently a valid option."
    quiet_welcome()

def takeone(n):
  return n - 1

def version():
  print '''  PySwap Version 1.01
  Most Stable Version Released 14-04-2011
  Compatible with Vanilla SiteSwap'''
  time.sleep(5)
  quiet_welcome()
  
#Checks to see whether a pattern is valid, and, if so, calculates the number of balls necessary.
def check(pattern):
  global throws
  global balls
  a = list(pattern)
  inta = []
  number = 0
  scores = []
  z = 10
  for i in a:
    i = int(i)
    inta.append(i)
    scores.append(i+number)
    number =  number + 1
  throws = collections.deque(inta)
  for i in scores:
  	if z == i:
  		print "Error. Invalid siteswap."
  		quiet_welcome()
  	else:
  		z = i
  	balls = sum(inta)/len(inta)
    
def interpret(pattern, start_hand):
  airtime = []
  if start_hand.upper() == "L":
    hand = 0
  else:
    hand = 1
  check(pattern)
#Describes starting position of balls.
  print "You are holding", balls, "balls."
  if balls % 2 == 0:
    print balls/2, "balls are in your right hand, and", balls/2, "balls are in your left."
  else:
    if hand == 1:
      print (balls/2+1), "balls are in your right hand, and", balls/2, "balls are in your left."
    elif hand == 0:
      print (balls/2+1), "balls are in your left hand, and", balls/2, "balls are in your right."
#Assigns starting positions of balls.
  if hand == 1:
    for j in range(1, balls):
      if j % 2 == 0:
        lhballs.append(j)
      else:
        rhballs.append(j)
  else:
    for j in range(1, balls):
      if j % 2 == 0:
        rhballs.append(j)
      else:
        lhballs.append(j)
    #Reads pattern and output description.
    #Calculate how many throws there are in a flash
    #convert throws to 1 flash worth
  length = len(pattern)
  i = 0
  while i < length:
    throw = throws[i]
    airtime = map(takeone, airtime)
    if 0 in airtime:
      index = airtime.index(0)
      del airtime[index]
      if to_hand[index] == 1:
        rhballs.append(airballs[index])
        del airballs[index]
        print "In your right hand, you catch ball", rhballs[-1]
      else:
        lhballs.append(airballs[index])
        del airballs[index]
        print "In your left hand, you catch ball", lhballs[-1]
      del to_hand[index]
    if throw == 1:
      if hand == 1:
        print "You pass a ball from your right hand to your left hand."
        lhballs.append(rhballs[0])
        del rhballs[0]
      else:
        print "You pass a ball from your left hand to your right hand."
      hand = abs(hand-1)
      i = i+1
    elif throw == 2:
      print "You wait."
      hand = abs(hand-1)
      i = i+1
    else:
      if hand == 1:
        print "You throw ball", rhballs[0], "from your right hand."
        airballs.append(rhballs[0])
        airtime.append((throw-1))
        if throw % 2 != 0:
          to_hand.append(abs(hand-1))
        else:
          to_hand.append(hand)
        del rhballs[0]
      else:
        print "You throw ball", lhballs[0], "from your left hand."
        airballs.append(lhballs[0])
        airtime.append((throw-1))
        if throw % 2 != 0:
          to_hand.append(abs(hand-1))
        else:
          to_hand.append(hand)
        del lhballs[0]
      hand = abs(hand-1)
      i = i+1
      
welcome()
