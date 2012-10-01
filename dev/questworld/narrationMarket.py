# -*- coding: utf-8 -*-
import conversationAnton
print "You enter the market, and see your friend Anton."
print "Anton approaches you."
input = int(raw_input("Type 0 to ignore Anton, or 1 to talk to him."))
if input == 1:
  conversationAnton.talk()
elif input == 0:
  conversationAnton.ignore()
else:
  print '''You walk past Anton, ignoring your old friend and crushing his self esteem.
He calls after you, but you no longer care about the people you grew up with.'''