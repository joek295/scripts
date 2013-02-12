#! /usr/bin/env python
from sys import argv
import os.path

faresfile, pot = argv

if os.path.isfile(faresfile):
  #somefunction
else:
  print faresfile "is not a valid filename"

