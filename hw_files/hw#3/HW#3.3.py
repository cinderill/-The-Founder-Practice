#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for N in range(1,101):
  if N%3 == 0 and N%5 == 0:
    print(N, "- Fizz-Buzz!")
  elif N%3 == 0:
    print(N, "- Fizz!")
  elif N%5 == 0:
    print(N, "- Buzz!")
  else:
    print(N)
