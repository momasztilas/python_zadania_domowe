"""
Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc
jej. Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana
liczba była za duża, czy za mała. Gdy użytkownik poda właściwą liczbę, program wypisuje
gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.
Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa
się bisekcją i pełni w informatyce bardzo ważną rolę. Umiejętnie ją stosując powinno się te
zagadki rozwiązywać w 9-10 próbach (bo 2^10=1024).

"""

import random
losowa_liczba = random.randint(0,999)
ilosc_strzalow = 1
# print(losowa_liczba)
print("Spróbuj odgadnąć liczbę z komory losującej.")
strzal = int(input('Jaka liczba została wylosowana?\n'))
while strzal != losowa_liczba:
    if strzal < losowa_liczba:
        print('Liczba wylosowana jest większa.')
    else:
        print('Liczba wylosowana jest mniejsza. ')
    strzal = int(input('Jeszcze raz.\nJaka liczba została wylosowana?\n'))
    ilosc_strzalow += 1
print(f'Gz, udało Ci się odgadnąć liczbę po {ilosc_strzalow} razach.')
