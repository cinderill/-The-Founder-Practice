#!/usr/bin/env python3
# -*- coding: utf-8 -*-
dep_f = float(input("Введите сумму вашего первоначального депозита: "))
s1 = dep_f * 1.04
s2 = s1 * 1.04
s3 = s2 * 1.04
print("В конце первого года на счету будет находиться %.2f ед." % s1,
      "В конце второго года %.2f ед." % s2,
      "В конце третьего года %.2f ед." % s3,
      sep='\n')