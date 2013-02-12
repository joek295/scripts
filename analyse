# -*- coding: utf-8 -*-
'''Module which analyses strings of letters, numbers, or a mixture of the two and returns information about 
their composition'''

#Counts frequency of starting digits from list 'data'
def benford(data):
  dataset = []
  results = []
  for i in data:
    while i/10 >= 10:
      i = i/10
    dataset.append(i)
  for i in dataset:
    count = count(i)
    results.append(count)
  return results

#Counts frequency of letters in string
def freq_analyse (string):
  ustring = string.upper()
  ACount = ustring.count("A")
  BCount = ustring.count("B") 
  CCount = ustring.count("C") 
  DCount = ustring.count("D")
  ECount = ustring.count("E") 
  FCount = ustring.count("F") 
  GCount = ustring.count("G") 
  HCount = ustring.count("H")
  ICount = ustring.count("I") 
  JCount = ustring.count("J") 
  KCount = ustring.count("K") 
  LCount = ustring.count("L")
  MCount = ustring.count("M") 
  NCount = ustring.count("N") 
  OCount = ustring.count("O") 
  PCount = ustring.count("P")
  QCount = ustring.count("Q") 
  RCount = ustring.count("R") 
  SCount = ustring.count("S") 
  TCount = ustring.count("T")
  UCount = ustring.count("U") 
  VCount = ustring.count("V") 
  WCount = ustring.count("W") 
  XCount = ustring.count("X")
  YCount = ustring.count("Y") 
  ZCount = ustring.count("Z")
  print "A:",ACount, "B:",BCount, "C:",CCount, "D:",DCount, "E:",ECount, "F:",FCount, "G:",GCount, "H:",HCount, "I:",ICount, "J:",JCount, "K:",KCount, "L:",LCount, "M:",MCount
  print "N:",NCount, "O:",OCount, "P:",PCount, "Q:",QCount, "R:",RCount, "S:",SCount, "T:",TCount, "U:",UCount, "V:",VCount, "W:",WCount, "X:",XCount, "Y:",YCount, "Z:",ZCount
