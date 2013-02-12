#!/usr/bin/env python
#2-deck Blackjack
#known bugs include: ace always counts as eleven
#unimplemented features include: ai players, splitting hands, doubling down, 5-card tricks and pontoons

import random

AH=11, H2=2, H3=3, H4=4, H5=5, H6=6, H7=7, H8=8, H9=9, H10=10, JH=10, QH=10, KH=10 
AC=11, C2=2, C3=3, C4=4, C5=5, C6=6, C7=7, C8=8, C9=9, C10=10, JC=10, QC=10, KC=10 
AD=11, D2=2, D3=3, D4=4, D5=5, D6=6, D7=7, D8=8, D9=9, D10=10, JD=10, QD=10, KD=10 
AS=11, S2=2, S3=3, S4=4, S5=5, S6=6, S7=7, S8=8, S9=9, S10=10, JS=10, QS=10, KS=10 

deck = [AH,H2,H3,H4,H5,H6,H7,H8,H9,H10,JH,QH,KH,AD,D2,D3,D4,D5,D6,D7,D8,D9,D10,JD,QD,KD,AS,S2,S3,S4,S5,S6,S7,S8,S9,S10,JS,QS,KS,AC,C2,C3,C4,C5,C6,C7,C8,C9,C10,JC,QC,KC]
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
  if option == 1:
    start()
  else:
    break

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
    bet = int(raw_input("initial stake?"))
    while high_limit > bet or low_limit < bet:
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
          if play_again == "y":
            play()
          else:
            print "you quit the game with ", money
            print "making a profit of ", money - 200
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
    if play_again == "y":
      play()
    else:
      print "you quit the game with ", money
      print "making a profit of ", money - 200
  else:
    print "you went bust"
  
play()
  
