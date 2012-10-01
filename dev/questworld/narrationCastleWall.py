# -*- coding: utf-8 -*-
print "You slowly circle the castle wall, looking for any kind of entrance."
print "You find a tree that comes close to the castle wall. It looks like it might be possible to climb it."
print "You also find a stream full of sewage which goes under the castle wall."
print "It would be unpleasant, but possible, to enter through it."
print "They are the only two possibilities that you can find."
input = int(raw_input("Press 0 to climb the tree, 1 to enter the sewage drain, or 2 to return to the sentry."))
if input == 0:
  import narrationTreeClimbing
elif input == 1:
  import narrationSewage
elif input == 2:
  import conversationSentry.approach()
else:
  print "You flip a coin to decide which way to go."
  dicecoin.coin (1)
  if toss == 1:
    print "The tree it is!"
    import narrationTreeClimbing
  elif toss == 2:
    print "I guess I'll go through the sewers, then."
    import narrationSewage
