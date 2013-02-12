# -*- coding: utf-8 -*-
#KanastaScore
#Automatically calculates the scores of each player in Kanasta.
#To do this I need:
  #A way of registering which cards a joker is associated with
  #Regular expressions for concision
  #A count of clean and dirty canastas for each team/player
  
def score (players):
  player1_table = 0
  player1_hand = 0
  player1_bonus = 0
  player2_table = 0
  player2_hand = 0
  player2_bonus = 0
  if players == 2:
    length = len(player1)
    for i in (0, length-1):
      card = player1.pop()
      player1_hand = player1_hand + card[0]
    length = len(player2)
    for i in (0, length-1):
      card = player2.pop()
      player2_hand = player2_hand + card[0]
    pass
  elif players == 3:
    player3_table = 0
    player3_hand = 0
    player3_bonus = 0
    pass
  elif players == 4:
    player3_hand = 0
    player4_hand = 0
    pass