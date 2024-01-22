#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randrange
value = randrange(0, 38)

#Check for 00 and 0, show result
if value == 37:
  print("00 on the run!",
        "And that's all folks!",
        sep='\n')
elif value == 0:
  print("ZERO!",
        "Hope you enjoy the show!",
        sep='\n')
else:
  print("%d made it!" % value,
        "What else?",
        sep='\n')

red = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)

#Check for color
if value in red:
  print("RED ONE!")
elif value not in red and value != 0 and value != 37:
  print("BLACK ONE!")

#Check for odd/even
if value % 2 == 1 and value != 37:
  print("IT'S ODD!")
elif value % 2 == 0 and value != 0:
  print("IT'S EVEN!")

#Check for halfs
if value > 18 and value != 37:
  print("Big half wons!")
elif value < 19 and value != 0:
  print("Small half wons!")