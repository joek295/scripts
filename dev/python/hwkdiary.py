#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Homework diary application for Python

import time
import datetime
import compilations

week = 1
ttblmon = []
ttbltue = []
ttblwed = []
ttblthur = []
ttblfri = []
ttblsat = []
hwkdue = []
lessondue = []

'''if dayinput == '''

def welcome():
  print '''Take which action?
1: Set homework
2: Check due homework
3: Check timetable
4: Set timetable
5: Change week'''
print "Current week:", week
  option = int(raw_input())
  if option == 1:
    hwk_set()
  elif option == 2:
    hwk_check()
  elif option == 3:
    ttbl_check()
  elif option == 4:
    ttbl_set()
  elif option == 5:
    wk_set()
  else:
    print '''Error: Option invalid'''
  
  
def hwk_set():
  hwk_input = str(raw_input("What homework have you got?")
  hwkdue.append(hwk_input)
  due_input = str(raw_input("What lesson is it for?")
  lessondue.append(due_input)
  
def hwk_check():
  print hwkdue
  print lessondue
  
def ttbl_set():
  dayinput = 6
  while dayinput > 0:
    print "day ", (7 - dayinput), "'s lessons"
    usr_input = str(raw_input())
    if usr_input == "Finished":
      dayinput = dayinput - 1
    else:
      #ttblday.append(usr_input)
  
def ttbl_check():
  print "Monday:", ttblmon
  print "Tuesday:", ttbltue
  print "Wednesday:", ttblwed
  print "Thursday:", ttblthur
  print "Friday:", ttblfri
  print "Saturday:", ttblsat  
  
def wk_set():
  week = int(raw_input("Which week is it?")