# -*- coding: utf-8 -*-
#deals cards to each player.
#jokers not yet implemented.
import random
def deal(players, cards, [packs], [jokers]):
  deck = (AH, 2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H, 10H, JH, QH, KH, AD, 2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D, 10D, JD, QD, KD, AC, 2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C, 10C, JC, QC, KC, AS, 2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S, 10S, JS, QS, KS)
  pack = deck*packs
  while players > 0:
    while cards > 0:
      card = random.choice(pack)
      pack.remove(card)
      player1.append(card)