#!/usr/bin/env python
# -*- coding: utf-8 -*-
def bottles (n):
  while n > 0:
    print '''There are''', n, '''green bottles, standing on the wall
There are''', n, '''green bottles, standing on the wall"
And if one green bottle should accidently fall"
There'll be''', n-1, '''green bottles, standing on the wall.'''
    print ""
    n = n-1
