#! env /usr/bin/python

#A program which keeps track of tasks and deadlines
#to do: write a menu-driven interface for the program; write tasksdue & remtask code.

import datetime
import os

tasksfile = "tasks.txt"

def addtask(x):
  name = x
  description = str(raw_input("Description?"))
  dueday = int(raw_input("Day due?"))
  duemonth = int(raw_input("Month due?"))
  dueyear =  int(raw_input("Year due?"))
  due = datetime.date(dueyear, duemonth, dueday)
  print "Mark as important? Y/N?"
  input = str(raw_input)
  if input == "Y":
    importance = 1
  elif input == "N":
    importance = 0
  else:
    importance = 0
  os.open(tasksfile,"w")
  FILE.writelines(due, importance)
  os.close(tasksfile)
  
def tasksdue():
  open (tasksfile, "r")
  #remove any timed out tasks
  #print remaining tasks due in next fortnight, + those marked as important.

def remtask():
  #mark a task in the list as complete i.e. remove from list.
  