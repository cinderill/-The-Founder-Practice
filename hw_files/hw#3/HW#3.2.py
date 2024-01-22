#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Проверка корректности буквенной координаты
while True:
  coord1 = input("Введите столбец (буква от a до h): ")
  if coord1 not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
    print("Латинские буквы: a, b, c, d, e, f, g, h.")
    continue
  break

#Проверка корректности циферной координаты
while True:
  coord2 = input("Введите строку (цифра от 1 до 8): ")
  try:
    coord2 = int(coord2)
    if coord2 not in range(1,9):
      print("Попробуйте снова (целое число от 1 до 8).")
      continue
    break
  except ValueError:
    print("Попробуйте снова (целое число от 1 до 8).")

#Поиск соответствующего цвета
if coord1 in ["a", "c", "e", "g"]:
  if coord2 in [1,3,5,7]:
    print("Чёрный")
  else:
    print("Белый")
else:
  if coord2 in [1,3,5,7]:
    print("Белый")
  else:
    print("Чёрный")
