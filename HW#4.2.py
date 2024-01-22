# -*- coding: utf-8 -*-
#"Шестнадцатиричный словарь"
hex = {
       '1' : 1,
       '2' : 2,
       '3' : 3,
       '4' : 4,
       '5' : 5,
       '6' : 6,
       '7' : 7,
       '8' : 8,
       '9' : 9,
       "Aa" : 10,
       "Bb" : 11,
       "Cc" : 12,
       "Dd" : 13,
       "Ee" : 14,
       "Ff" : 15
       }

#Из 16 в 10.
def hex2int():
    int2 = input("Введите число для перевода: ")
    for key,value in hex.items():
        if int2 in key and len(int2) == 1:
            print("%s x16 = %d x10." % (int2, value))
            break
        elif len(int2) > 1:
            print("Строка должна содержать один символ!")
            break

#Из 10 в 16.
def int2hex():
    int2 = int(input("Введите число для перевода: "))
    for key,value in hex.items():
        if value == int2 and int2 in range(16):
            print("%d x10 = %s x16." % (value, key[0]))
            break
        elif int2 not in range(16):
            print("Значение больше Ax16")
            break

while True:
    
    #Выбор системы счисления.    
    try:
        syst = int(input("Выберите Вашу систему счисления: 1 для шестнадцатеричной, 2 для десятичной, 0 для выхода: "))
    except ValueError:
        print("Ошибка ввода #1, попробуйте снова.")
        continue
    
    #Вывод.
    if syst == 1:
        hex2int()
    elif syst == 2:
        int2hex()
    elif syst == 0:
        break
    else:
        print("Ошибка ввода #2, попробуйте снова.")

