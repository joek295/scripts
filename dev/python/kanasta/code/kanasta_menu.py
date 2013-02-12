# -*- coding: utf-8 -*-
#kanastamenu
#the startup menu when playing a game of kanasta 

menu ():
  print '''Welcome to Kanasta, a canasta client written in Python.
Options:
  1: Play Kanasta
  2: How to Play
  3: Help
  0: About Kanasta'''
  option = int(raw_input())
  if option == 1:
    players = int(raw_input("How many players?"))
    deal(players)
  elif option == 2:
    #write intro to canasta
    pass
  elif option == 3:
    help()
  elif option == 0:
    about()
  else:
    #error message
    
    
def about():
  print '''Kanasta is a canasta client, written in python. It began in June 2011.
Latest version: 0.01
Stability: Incomplete
Most stable version: 0.01'''

def help():
  #write this
  pass