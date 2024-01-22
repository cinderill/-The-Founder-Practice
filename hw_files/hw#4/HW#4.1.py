#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

letters = "АВЕКМНОРСТУХ"
digits = "1234567890"

def old_style(id):
  for i in range(6):
    if i < 3:
      id.append(random.choice(letters))
    else:
      id.append(random.choice(digits))

def new_style(id):
  for i in range(7):
    if i < 4:
      id.append(random.choice(digits))
    else:
      id.append(random.choice(letters))

id = []

while len(id) == 0:
  style = input("Выберите формат знака (Введите Y для нового, N для старого, пустую строку для выхода): ")
  if style in "Yy": new_style(id)
  elif style in "Nn": old_style(id)
  elif style == "": break

print(id)