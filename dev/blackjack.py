# -*- coding: utf-8 -*-
#!/usr/bin/env python
#2-deck Blackjack
#known bugs include: ace always counts as eleven
#unimplemented features include: ai players, splitting hands, doubling down, 5-card tricks and pontoons

import random

"AH"=11, "2H"=2, "3H"=3, "4H"=4, "5H"=5, "6H"=6, "7H"=7, "8H"=8, "9H"=9 ,"10H"=10, "JH"=10, "QH"=10, "KH"=10 
"AC"=11, "2C"=2, "3C"=3, "4C"=4, "5C"=5, "6C"=6, "7C"=7, "8C"=8, "9C"=9 ,"10C"=10, "JC"=10, "QC"=10, "KC"=10 
"AD"=11, "2D"=2, "3D"=3, "4D"=4, "5D"=5, "6D"=6, "7D"=7, "8D"=8, "9D"=9 ,"10D"=10, "JD"=10, "QD"=10, "KD"=10 
"AS"=11, "2S"=2, "3S"=3, "4S"=4, "5S"=5, "6S"=6, "7S"=7, "8S"=8, "9S"=9 ,"10S"=10, "JS"=10, "QS"=10, "KS"=10 

deck = ["AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC"]
decks = [deck, deck]

p2capital = 200
p3capital = 200
p4capital = 200
p5capital = 200
p6capital = 200
p7capital = 200
p1pot = 0
player1 = []
player2 = []
player3 = []
player4 = []
player5 = []
player6 = []
player7 = []
bank = []

def menu():
  print '''1: Begin a new game
2: quit'''
  option = int(raw_input())
  if option = 1:
    start()

def start():
  global high_limit
  global low_limit
  global money 
  high_limit = int(raw_input("high limit?"))
  low_limit = int(raw_input("low limit?"))
  #players
  money = 200

def setup():
  random.shuffle(decks)
  play()
  
def play ():
  while len(decks) > 20:
    print "Table Limits: High = ", high_limit, "Low = ", low_limit
    bet = int(raw_input("initial stake?")
    while low_limit > bet  or bet > high_limit:
      print "initial stake must be between ", low_limit, " and ", high_limit
      bet = int(raw_input("initial stake?"))
    money = money - bet, p1pot = p1pot + bet, bet = 0
    player1.append(deck.pop)
    bank.append(deck.pop)
    player1.append(deck.pop)
    print "Your Hand:", player1
    print "Banker:", bank
    bank.append(deck.pop)
    turn = 1
    while turn == 1:
      if sum(player1) <= 21:
        move = str(raw_input("stick or twist"))
        if move == "stick":
          turn = 0
        elif move == "twist":
          player1.append(deck.pop)
      else:
        print "You went bust."
        bet = 0
        player1 = [], bank = []
        if money > low_limit:
          play_again = str(raw_input("play again? y/n"))
          if play_again = "y":
            play()
          else:
            print "you quit the game with £", money
            print "making a profit of £", money - 200
        else:
          print "you don't have enough money to continue betting at this table"
    #later versions can include play from other AI players
    banker()
  print "the decks are burnt and two new decks are introduced"
  decks = [deck, deck]
  setup()
  
def banker ():
  while sum(bank) < 17:
    bank.append(deck.pop)
    print bank(-1)
  scores()

def scores ():
  print "player 1 scores ", sum(player1)
  print "bank scores ", sum(bank)
  if sum(player1) > sum(bank):
    print "player1 wins"
    money = bet + money, bet = 0
  else:
    print "bank wins"
    bet = 0
  player1 = [], bank = []
  if money != 0:
    play_again = str(raw_input("play again? y/n"))
    if play_again = "y":
      play()
    else:
      print "you quit the game with £", money
      print "making a profit of £", money - 200
  else:
    print "you went bust"
  
play()
  
  
