#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random

class Neuron:
    def __init__ (self, w):
        self.w = w

    def arr_mult(self, x) :
        s = 0
        for i in range(len(self.w)):
          s = s + self.w[i] * x[i]
        return s

    def onestep(self, x):
        if x >= 0:
          return 1
        else:
          return 0

Xi = []

while True:
  xi = input("Введите входной параметр (1 или 0) или оставьте пустую строку для продолжения: ")
  if len(Xi) == 9:
    Xi.append(-1)
    break
  elif xi == "":
    Xi.append(-1)
    break
  elif int(xi) == 1 or int(xi) == 0:
    Xi.append(int(xi))
  else:
    print("Значения: 1, 0, 'пустая строка'.")

Wi = []
for i in range(len(Xi)):
  Wi.append(random.randint(1,10))

Ner = Neuron(Wi)

print(Xi)
print(Wi)
sum = Ner.arr_mult(Xi)
print("Взвешенная сумма:", sum)
print("Ответ:", Ner.onestep(sum))


