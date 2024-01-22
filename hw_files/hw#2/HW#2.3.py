#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cop = int(input("Всего копеек: "))
rubFive = cop // 500
cop = cop - rubFive * 500
rubTwo = cop // 200
cop = cop - rubTwo * 200
rubOne = cop // 100
cop = cop - rubOne * 100
copFifty = cop // 50
cop = cop - copFifty * 50
copTen = cop // 10
cop = cop - copTen * 10
copFive = cop // 5
cop = cop - copFive * 5
print("Итого:",
      "Пятирублевых: %d," % rubFive,
      "Двухрублевых: %d," % rubTwo,
      "Рублевых: %d," % rubOne,
      "По 50 копеек: %d," % copFifty,
      "По 10 копеек: %d," % copTen,
      "По 5 копеек: %d," % copFive,
      "По 1 копейке: %d." % cop,
      sep='\n')