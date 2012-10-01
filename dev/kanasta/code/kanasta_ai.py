# -*- coding: utf-8 -*-
#kanasta_ai
#the ai for kanasta
#currently mainly pseudocode and planning
#more will be able to be written once some of the earlier modules are complete

my_priority = #defining ai priority
target_priority = my_priority + 1 #(mod_n)
reciept_priority = my_priority - 1 #(mod_n)

def remember_discards(n):
  #remember the discards of the player the ai is throwing to for the past n turns
  #ideally different difficulty levels will have different values of this for both friendly and opposing ai
  #if setting is arbitarily high, remember discards for as long as the pile continues
  
def pick_up():
  #at most basic level
  if #can pick up pack:
    #pick up pack


#What the AI wants:
  #pick up pack if it would gain cards
  #pick up pack if there are useful cards in it
  #discard unneccessary cards
  #discard cards that target doesn't have a known pair of
  #discard cards thrown away recently by target
  #don't discard cards it has pairs of
  #throw cards it has threes of if the person throwing to it has one.
  #try to get enough points in hand to go down
  
#Throwing away formula:
  #10 for pair
  #-10 if frozen and opponent has it on table
  #-10 for canasta on table
  #50 if opponent has it in his hand
  #10 for each black 3 when frozen
  #-10 for each black 3 when the pack is arbitarily large