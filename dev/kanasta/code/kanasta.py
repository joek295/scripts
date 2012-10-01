#!/usr/bin/env python
# -*- coding: utf-8 -*-

#kanasta is a canasta client for linux
#the current version will be text-based and command-line only when completed
#later versions may implement a gui, but this is currently low-priority
#this module is the kanasta core
#it imports all the necessary modules for the game, sets up the deck, and then runs the main menu

#global modules needed to play kanasta
import random

#kanasta modules needed to play
import kanasta_menu
import kanasta_setup
import kanasta_play
import kanasta_ai
import kanasta_score

#Cards and their attributes - to be completed later...
"joker" = [50, "wild", "no-meld", "freeze"]
"AH","AC","AD","AS" = [20, "unwild", "meld", "pick-up"]
"2C","2H","2D","2S" = [20, "wild", "no-meld", "freeze"]
"3C","3S" = [5, "unwild", "no-meld", "no-pickup"]
"3H","3D" = [100, "unwild", "no-meld", "freeze"]
"4C","4H","4D","4S" = [5, "unwild", "meld", "pick-up"]
"5C","5H","5D","5S" = [5, "unwild", "meld", "pick-up"]
"6C","6H","6D","6S" = [5, "unwild", "meld", "pick-up"]
"7C","7H","7D","7S" = [5, "unwild", "meld", "pick-up"]
"8C","8H","8D","8S" = [10, "unwild", "meld", "pick-up"]
"9C","9H","9D","9S" = [10, "unwild", "meld", "pick-up"]
"10C","10H","10D","10S" = [10, "unwild", "meld", "pick-up"]
"JC","JH","JD","JS" = [10, "unwild", "meld", "pick-up"]
"QC","QH","QD","QS" = [10, "unwild", "meld", "pick-up"]
"KC","KH","KD","KS" = [10, "unwild", "meld", "pick-up"]

#Building the deck
hearts = ["AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH"]
clubs = ["AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC"]
diamonds = ["AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD"]
spades = ["AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS"]
deck = [hearts, hearts, clubs, clubs, diamonds, diamonds, spades, spades, "joker", "joker", "joker", "joker"]
discards = []
team1 = []
team2 = []
team1_down_cost = 50
team2_down_cost = 50
team1_down = 0
team2_down = 0

kanasta_menu.menu()

