# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:12:05 2020

@author: Ola
"""
currencies = {"eur":4.54,"gbp":5.20, "usd":4.17, "nok":0.40, "sek":0.42, "chf":4.30}

def naZlotego(currencies):
    
    choose = input("Wybierz walutę: ")
    if choose in currencies:
        prise = float(input("Podaj kwotę: "))
        total = prise*currencies[choose]
        print(round(total,2),'pln')
    else:
        print("Nie ma takiej waluty:(")
def zeZlotego(currencies):
    
    choose = input("Wybierz walutę: ")
    if choose in currencies:
        prise = float(input("Podaj kwotę: "))
        total = prise/currencies[choose]
        print(round(total,2),'',choose)
    else:
        print("Nie ma takiej waluty :(")
print("Kalkulator walut")

print("Wymiana złotego na inną walutę - na, a z innej waluty na złotego - z")

choice = input()
if choice == "na":
    naZlotego(currencies)
elif choice == "z":
    zeZlotego(currencies)
else:
    print("Nie poprawna wartość")