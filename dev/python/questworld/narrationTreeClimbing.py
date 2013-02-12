# -*- coding: utf-8 -*-
print '''You rapidly climb the tree, which is conveniently proportioned for the purpose.
Perched high up in the branches, you survey the scene.
There appears to be a ladder leading down into the castle proper from the walls.
You crawl along a convenient overhanging branch to scramble onto the walls.
You clamber across the walls, and descend the ladder.
At the bottom of the ladder, you find a darkened room.
You light your lantern, and take a look around.
On one side of the room is a table, on which lies a necklace, along with two rings.
On the other side of the room is a chest. There is a plain door set into one wall.
You wonder what is in the chest.'''
input = int(raw_input("Do you open the chest (1) or examine the jewellery (2)? Or do you go straight through the door (3)"
if input ==1:
  print "You walk towards the chest."
  import narrationRoom1.chest
elif input ==2:
  print "You walk over to look at the necklace."
  import narrationRoom1.jewellery
elif input == 3:
  print "You approach the door."
else:
  