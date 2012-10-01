# -*- coding: utf-8 -*-
#A repository of useful (and less useful) one-liners, often involving modules

#Shebang making python code executable through the command line:
#!/usr/bin/env python

#Finds and prints platform
from sys import platform; print platform

#Finds and outputs subversion & version
from sys import subversion, version; print subversion; print version

#Creates a timestamp
import time; print time.asctime()

#Swaps variable values
a, b = b, a

#Conscise incrementation and decrementation
x += 1
x -= 1

#incrementation of each number in a list
map(xlist, x+=1)

#Reversal of a string
string[::-1]