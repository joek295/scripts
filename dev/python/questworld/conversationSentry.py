# -*- coding: utf-8 -*-
def approach():
  print '''The Sentry blocks your way.
'You shall not pass!' says he.
'Oh, that line is so overused,' you reply.
'I can only let you in if you solve the riddle of the sentry.' he says.
You hope it's the same as the riddle of the sphinx. You never were good at this kind of thing.
'Alright,' you sigh, 'let's hear it, then...''''
#Riddle  
  
def caught():
  print "'Where are you going?' he shouts, drawing his sword."
  input = int(raw_input("Do you try to lie your way out (0), tell the truth (1), or run away (2)")
  if input == 0:
    print "'I was just going for a walk,' you say."
    print "The sentry doesn't look convinced. 'Go away. The master doesn't appreciate people like you.'"
    print "Defeated, you turn as if to go. Exploring the rest of the wall it is, then."
    import narrationCastleWall
  elif input == 1:
    print "'I wanted to come into the castle,' you tell him."