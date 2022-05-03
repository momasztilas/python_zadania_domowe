"""Przy pomocy input() zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i
jaka jest jego cena. Wyświetl odpowiedni komunikat.

Przykład: Co chcesz kupić? - ziemniaki
Podaj cenę towaru - 5
Podaj ilość towaru - 10
Za ziemniaki, który chcesz kupić, zapłacisz 50 zł"""

towar = str(input('Co chcesz kupić? '))
cena = float(input('Podaj cenę towaru za kg w zł: '))
ilosc = float(input('Podaj ilość towaru w kg: '))

print (f'Za {towar} o wadze {ilosc} kg, zapłacisz {cena * ilosc:.2f} zł.')
