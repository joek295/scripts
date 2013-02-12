# -*- coding: utf-8 -*-
#Module which performs simple cryptographic procedures
'''WARNING: All these procedures are INSECURE. They have all been broken for hundreds of years.
In the event that you wish to secure data properly, please use RSA, PGP, or another encryption standard.
The cryptograms in this module are toys, and are not a replacement for proper data security.
'''

#Performs a Caesar shift on a string by n places.
def caesar_shift (string, shift):
  d = {}
  for c in (65, 97):
    for i in range(26):
      d[chr(i+c)] = chr((i+shift) % 26 + c)
  print "".join([d.get(c, c) for c in string])

#INCOMPLETE!!!
def vignere (string, key):
  #convert key into integers mapping a::0, b::1 etc
  d = {}
  for c in (65, 97):
    for i in range(26):
      d[chr(i+c)] = chr((i+shift) % 26 + c)
  print "".join([d.get(c, c) for c in string])

#Conducts frequency analysis on a string.
def freq_analyse (string):
  string_2 = string.upper()
  ACount = string_2.count("A")
  BCount = string_2.count("B") 
  CCount = string_2.count("C") 
  DCount = string_2.count("D")
  ECount = string_2.count("E") 
  FCount = string_2.count("F") 
  GCount = string_2.count("G") 
  HCount = string_2.count("H")
  ICount = string_2.count("I") 
  JCount = string_2.count("J") 
  KCount = string_2.count("K") 
  LCount = string_2.count("L")
  MCount = string_2.count("M") 
  NCount = string_2.count("N") 
  OCount = string_2.count("O") 
  PCount = string_2.count("P")
  QCount = string_2.count("Q") 
  RCount = string_2.count("R") 
  SCount = string_2.count("S") 
  TCount = string_2.count("T")
  UCount = string_2.count("U") 
  VCount = string_2.count("V") 
  WCount = string_2.count("W") 
  XCount = string_2.count("X")
  YCount = string_2.count("Y") 
  ZCount = string_2.count("Z")
  print "A:",ACount, "B:",BCount, "C:",CCount, "D:",DCount, "E:",ECount, "F:",FCount, "G:",GCount, "H:",HCount, "I:",ICount, "J:",JCount, "K:",KCount, "L:",LCount, "M:",MCount, "N:",NCount, "O:",OCount, "P:",PCount, "Q:",QCount, "R:",RCount, "S:",SCount, "T:",TCount, "U:",UCount, "V:",VCount, "W:",WCount, "X:",XCount, "Y:",YCount, "Z:",ZCount

#Performs a railfence cipher on a string.
def railfence(string):
  plaintext = list(string)
  a = len(plaintext)
  for i in range(0, a, 2):
    print plaintext[i]
  for j in range (1, a, 2):
    print plaintext[j]
    
