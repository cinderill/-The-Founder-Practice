#!/usr/bin/env python3
# -*- coding: utf-8 -*-
abc = { 1 : "aAeEiIlLnNoOrRsStTuU",
         2 : "dDgG",
         3 : "bBcCmMpP",
         4 : "fFhHvVwWyY",
         5 : "kK",
         6 : "jJxX",
         7 : "qQzZ"}

word = input("Введите слово (на английском): ")
total = 0

for let in word:
  for key, value in abc.items():
    if let in value:
      total = total + key

print("Вы набрали %d очков!" % total)