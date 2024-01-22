#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
  age = input("Введите человеческий возраст: ")

  #Проверка корректности данных
  try:
    age = float(age)
    if age < 0:
      print("НЕОТРИЦАТЕЛЬНОЕ ЧИСЛО!")
      continue
    break

  except ValueError:
    print("Попробуйте снова (НЕОТРИЦАТЕЛЬНОЕ ЧИСЛО)")

print("Возраст человека %d." % age)

dog_age = 0

#Вычисление возраста
while age > 0:
  if dog_age < 2:
    age = age - 10.5
  elif dog_age >= 2:
    age = age - 4

  dog_age = dog_age + 1

#Вывод
if age < 0:
  print("Возраст по собачьим меркам неполных %d." % dog_age)
elif age == 0:
  print("Возраст по собачьим меркам ровно %d." % dog_age)