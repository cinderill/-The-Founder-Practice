#!/usr/bin/env python3
# -*- coding: utf-8 -*-
time = int(input("Введите число (секунды): "))
secPerDay = 60*60*24
secPerHour = 60*60
day = time // secPerDay
time = time - day*secPerDay
hour = time // secPerHour
time = time - hour*secPerHour
min = time // 60
sec = time - min*60
print("Отформатированное время: %d:%d:%d:%d." % (day,hour,min,sec))