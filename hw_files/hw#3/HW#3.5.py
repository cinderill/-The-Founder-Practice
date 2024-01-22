#!/usr/bin/env python3
# -*- coding: utf-8 -*-
digit = input("Введите первое число, чтобы начать (для выхода введите пустую строку): ")
arr = []
arr1 = []
arr2 = []
arr3 = []
total = 0

#Заполнение списка чисел
while digit != "":
  digit = float(digit)
  arr.append(digit)
  total = total + digit
  digit = input("Введите число (для выхода введите пустую строку): ")

total = total/len(arr)
print("Среднее значение: %.3f." % total)

for j in range(len(arr)):
  if arr[j] < total:
    arr1.append(arr[j])
  elif arr[j] > total:
    arr2.append(arr[j])
  else:
    arr3.append(arr[j])

print("Числа больше среднего значения:", arr2,
      "Числа меньше среднего значения", arr1,
      "Числа равные среднему значению", arr3,
      sep='\n'
      )