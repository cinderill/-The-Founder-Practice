#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
cond = { 0 : "Сейчас Зима?",
         1 : "Сейчас Весна?",
         2 : "Сейчас Лето?",
         3 : "Сейчас Осень?",
         4 : "Есть ли осадки?",
         5 : "На работу/учёбу?",
         6 : "С товарищем?"
         }

print("Идти ли на улицу?")

for key, value in cond.items():
  print(value)
  xi = int(input("Да - 1, Нет - 0: "))
  Xi.append(xi)

Xi.append(-1)

print(Xi)
print("Анализ ответа...")

Wi = [1,6,8,4,-2,6,2,6]

Ans = Neuron(Wi)
sum = Ans.arr_mult(Xi)

print("Взвешенная сумма равна %d (проходной балл - 6)." % (sum + 6))

if Ans.onestep(sum) == 1:
  print("Идите на улицу.")
else:
  print("Не выходите на улицу.")


