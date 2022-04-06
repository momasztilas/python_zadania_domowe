"""

Zakładamy, że 1 rok psi, to 5 lat ludzkich.
Za pomocą konsoli wczytaj imię i wiek psa.
Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.
Przykład: Podaj imię psa - Burek
Podaj wiek psa - 3
Gdyby Burek był człowiekiem, miałby 15 lat.

"""

imie_psa = str(input('Podaj imię psa: '))
wiek_psa = float(input('Podaj wiek psa w latach: '))
wiek_czlowieka = wiek_psa * 5
print(f'Gdyby {imie_psa} był człowiekiem, jego wiek wynosiłby {wiek_czlowieka:.0f} lat.')