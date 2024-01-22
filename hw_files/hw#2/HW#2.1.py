#!/usr/bin/env python3
# -*- coding: utf-8 -*-
qt1 = int(input("Число сувениров: "))
qt2 = int(input("Число безделушек: "))
m_gr = qt1 * 75 + qt2 * 112
m_kg = m_gr // 1000
m_gr = m_gr - m_kg*1000
print("Общий вес купленных товаров: %d кг %d гр." % (m_kg, m_gr))

