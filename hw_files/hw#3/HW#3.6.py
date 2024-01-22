#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input("Введите верхнюю границу (целое положительное число): "))

#Формируется список из чисел от 0 до N
sieve = list(range(N+1))
sieve[1] = 0
#Начало цикла с двойки
count = 2

#Решето
while count < N+1:
  if count != 0:
    for x in range(2*count, N+1, count):
      sieve[x] = 0
  count = count + 1

#Удаление нулей
bowl = set(sieve)
bowl.remove(0)
print(sorted(bowl))