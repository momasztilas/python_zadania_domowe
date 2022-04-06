"""
Program losuje dwie liczby z zakresu od 0 do 99.
Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.

"""
import random
liczba_1 = (random.randint(0,99))
liczba_2 = (random.randint(0,99))
suma_realna = liczba_1 + liczba_2
# do sprawdzenia czy pętla się przerywa:
# print(f'Suma realna to {suma_realna}')
suma_pytanie = int(input('Jak myślisz, jaka jest suma? '))
while suma_pytanie != suma_realna:
    suma_pytanie = input(f'Wpisana suma to {suma_pytanie}. Nie zgadłeś, próbuj dalej: ')
else:
        print(f'Gratulacje, udało Ci się odgadnąć sumę: {suma_realna}')




