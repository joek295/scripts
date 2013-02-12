# -*- coding: utf-8 -*-
#A program that plays rock, paper, scissors against you.
print "To play rock, type 'rps (1)'"
print "To play paper, type 'rps (2)'"
print "To play scissors, type 'rps (3)'"
from random import choice
def rps (x):
	me = choice([1, 2, 3])
	if x == me:
		print "Draw"
	elif x == 1:
		if me == 2:
			print "I win"
		elif me == 3:
			print "You win"
	elif x == 2:
		if me == 1:
			print "You win"
		elif me == 3:
			print "I win"
	elif x == 3:
		if me == 1:
			print "I win"
		elif me == 2:
			print "You win"
	else:
		print "You can't do that!"