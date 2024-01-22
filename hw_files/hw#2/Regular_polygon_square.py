#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
a = float(input("Длина одной из сторон правильного многоугольника: "))
n = float(input("Количество сторон (углов) у фигуры: "))
S1 = n * (a**2)
S2 = 4 * math.tan(math.pi / n)
S = S1 / S2
print("Площадь %d-угольника со сторонами %d ед. равна %.2f кв.ед." % (int(n), int(a), S))
