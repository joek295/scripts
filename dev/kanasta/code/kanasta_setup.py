# -*- coding: utf-8 -*-
#Sets up the game of Kanasta:
#Automatically plays and draws for red threes, then turns over first card of deck for discards
#Dealing the cards

def deal (players):
  print "Shuffling the Deck"
  random.shuffle(deck)
  global player1
  global player2
  player1 = []
  player2 = []
  if players == 2:
    print "Dealing 15 cards to each player"
    for i in range(1,15):
      card = deck.pop()
      player1.append(card)
      card = deck.pop()
      player2.append(card)
  elif players == 3:
    print "Dealing 13 cards to each player"
    global player3
    global team3
    player3 = []
    team3 = []
    for i in range(1,13):
      card = deck.pop()
      player1.append(card)
      card = deck.pop()
      player2.append(card)
      card = deck.pop()
      player3.append(card)
  elif players == 4:
    print "Dealing 11 cards to each player"
    global player3
    global player4
    player3 = []
    player4 = []
    for i in range(1,15):
      card = deck.pop()
      player1.append(card)
      card = deck.pop()
      player2.append(card)
      card = deck.pop()
      player3.append(card)
      card = deck.pop()
      player4.append(card)
  else:
    print "Sorry, Kanasta is only playable with 2-4 players."

def play(players):
  #Differentiate between number of players
  if players = 2:
    #check hands for red threes
    while player1.count("3H") != 0:
      index player1.index("3H")
      player1.pop(index)
      team1.append("3H")
      card = deck.pop()
      player1.append(card)
    while player1.count("3D") != 0:
      index player1.index("3D")
      player1.pop(index)
      team1.append("3D")
      card = deck.pop()
      player1.append(card)
    while player2.count("3H") != 0:
      index player2.index("3H")
      player2.pop(index)
      team2.append("3H")
      card = deck.pop()
      player2.append(card)
    while player2.count("3D") != 0:
      index player2.index("3D")
      player2.pop(index)
      team2.append("3H")
      card = deck.pop()
      player2.append(card)
    card = deck.pop()
    discards.append(card)
    kanasta_play.play2p()
  elif players = 3:
    while player1.count("3H") != 0:
      index = player1.index("3H")
      player1.pop(index)
      team1.append("3H")
      card = deck.pop()
      player1.append(card)
    while player1.count("3D") != 0:
      index = player1.index("3D")
      player1.pop(index)
      team1.append("3D")
      card = deck.pop()
      player1.append(card)
    while player2.count("3H") != 0:
      index = player2.index("3H")
      player2.pop(index)
      team2.append("3H")
      card = deck.pop()
      player2.append(card)
    while player2.count("3D") != 0:
      index = player2.index("3D")
      player2.pop(index)
      team2.append("3H")
      card = deck.pop()
      player2.append(card)
    while player3.count("3H") != 0:
      index = player3.index("3H")
      player3.pop(index)
      team3.append("3H")
      card = deck.pop()
      player3.append(card)
    while player3.count("3D") != 0:
      index = player3.index("3D")
      player3.pop(index)
      team3.append("3D")
      card = deck.pop()
      player3.append(card)
    card = deck.pop()
    discards.append(card)
    kanasta_play.play3p()
  elif players = 4:
    while player1.count("3H") != 0:
      index = player1.index("3H")
      player1.pop(index)
      team1.append("3H")
      card = deck.pop()
      player1.append(card)
    while player1.count("3D") != 0:
      index = player1.index("3D")
      player1.pop(index)
      team1.append("3D")
      card = deck.pop()
      player1.append(card)
    while player2.count("3H") != 0:
      index = player2.index("3H")
      player2.pop(index)
      team2.append("3H")
      card = deck.pop()
      player2.append(card)
    while player2.count("3D") != 0:
      index = player2.index("3D")
      player2.pop(index)
      team2.append("3H")
      card = deck.pop()
      player2.append(card)
    while player3.count("3H") != 0:
      index = player3.index("3H")
      player3.pop(index)
      team1.append("3H")
      card = deck.pop()
      player3.append(card)
    while player3.count("3D") != 0:
      index = player3.index("3D")
      player3.pop(index)
      team1.append("3D")
      card = deck.pop()
      player3.append(card)
    while player4.count("3H") != 0:
      index = player4.index("3H")
      player4.pop(index)
      team2.append("3H")
      card = deck.pop()
      player4.append(card)
    while player4.count("3D") != 0:
      index = player4.index("3D")
      player4.pop(index)
      team2.append("3H")
      card = deck.pop()
      player4.append(card)
    card = deck.pop()
    discards.append(card)
    kanasta_play.play4p()