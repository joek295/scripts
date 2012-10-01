# -*- coding: utf-8 -*-
print "As the sun dips below the horizon, you climb the narrow, winding path to the castle."
print "You can see the towers sillhouetted against the red sky."
print "According to local legend, you remember, the castle is inhabited by vampires."
print "You slowly approach the main gate. It is solid oak, and guarded by a sentry."
input = int(raw_input("If you wish to enter through the main gates, press 1. To search for another entrance, press 0."))
if input == 1:
  import conversationSentry
  print "Slowly, you approach the sentry."
  print "'Hello there,' you say, 'would you be good enough to allow me entry into the castle?'"
  conversationSentry.approach()
elif input == 0:
  import narrationCastleWall
else:
  import conversationSentry
  print "You stand paralyzed with indecision. Suddenly, the sentry sees you and gives a shout."
  conversationSentry.caught()