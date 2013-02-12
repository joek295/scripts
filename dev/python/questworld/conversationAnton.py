# -*- coding: utf-8 -*-
def talk():
  print "Anton: Hello", name
  print '''...I was looking for you. I have an old crossbow that might be useful to you.
...I'll sell it to you for one gold piece.



Do you want to buy the crossbow from Anton?'''
  input = int(raw_input("Type 0 if you don't want the crossbow, or 1 if you will accept the terms."))
  if input == 1:
    coins_gold = coins_gold - 1
    Crossbow = 1
  elif input == 0:
    print "You politely decline Anton's offer, thinking that a crossbow will just weigh you down."
  else:
    print "Anton: No,", name, ", I'm not *giving* it to you. Give me the money or leave."
    print ""
    print "Having angered your old friend, you leave the market."
    import narrationCastle
    
def ignore():
  print "Anton: Hello", name
  print '''...I was looking for you.




You tell Anton that you are in a hurry.'''