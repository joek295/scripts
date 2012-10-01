# -*- coding: utf-8 -*-
import dicecoin
print "Welcome, adventurer."
print "You have entered QuestWorld."
print "First, tell me your name."
name = str(raw_input())
print name, "your quest is to travel to the Castle of Evil."
print '''There you will find the MacGuffin, which you must return to its rightful place, here, in your village.
Before you set out on your quest, you must equip yourself.
You pick up your bag.
You pick up your knife.
You pick up your purse.
You have five gold coins and ten silver coins in your purse.
You check inside your bag.
In your bag, there is a lantern, a length of rope, and two healing potions.'''
Lantern = 1
Rope = 1
potion_heal = 2
coins_gold = 5
coins_silver = 10
Knife = 1
print "You leave your house, and try to decide whether to visit the market before leaving on your quest."
input = int(raw_input("Type 1 to go to the market, or 0 to go straight to the castle.")
if input == 1:
  import narrationMarket
elif input == 0:
  print "If you insist. You never know what you might have found at the market."
  import narrationCastle
else:
  print "You cannot go there, the road leads in but two directions."
  print "You decide to go to the market."
  import narrationMarket