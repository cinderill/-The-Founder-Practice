#!/usr/bin/env python3
# -*- coding: utf-8 -*-
word = input("Введите первое слово, чтобы начать (для выхода введите пустую строку): ")
cont = [word]

#Заполнение списка уникальных слов
while word != "":
  word = input("Введите следующее слово без пробелов (для выхода введите пустую строку): ")
  if word != "" and word not in cont:
    cont.append(word)

#Вывод
for x in cont:
  print(x)