"""Napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a
program wylicza, ile trzeba zapłacić. Zasady są takie:
nieletni (poniżej 18 roku życia) płacą 100 zł za noc
dorośli (ci, którzy mają przynajmniej 18 lat, ale mniej niż 65 lat) płacą:
200 zł za noc, jeśli nocują jedną noc
180 zł za noc, jeśli nocują przynajmniej dwie, ale mniej niż pięć nocy
150 zł za noc, jeśli nocują pięć lub więcej nocy
emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za
noc z 10% zniżki, czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł."""

wiek = int(input('Podaj wiek gościa hotelu: '))
dlugosc_pobytu = int(input('Podaj długość pobytu gościa w hotelu: '))
cena_doby_default = 200
cena_pobytu = cena_doby_default * dlugosc_pobytu

if wiek < 18:
    cena_pobytu = (cena_doby_default * 0.5) * dlugosc_pobytu
elif 18 <= wiek < 65 and dlugosc_pobytu == 1:
    cena_pobytu = cena_doby_default * dlugosc_pobytu
elif 18 <= wiek < 65 and 1 < dlugosc_pobytu < 5:
    cena_pobytu = (cena_doby_default * 0.9) * dlugosc_pobytu
elif 18 <= wiek < 65 and dlugosc_pobytu >= 5:
    cena_pobytu = (cena_doby_default * 0.75) * dlugosc_pobytu
elif wiek >= 65 and dlugosc_pobytu == 1:
    cena_pobytu = cena_doby_default * dlugosc_pobytu * 0.9
elif wiek >= 65 and dlugosc_pobytu < 5:
    cena_pobytu = ((cena_doby_default * 0.9) * dlugosc_pobytu) * 0.9
elif wiek >= 65 and dlugosc_pobytu > 5:
    cena_pobytu = ((cena_doby_default * 0.75) * dlugosc_pobytu) * 0.9

# mało zgrabne rozwiązanie, ale działa, wiem, że da się to inaczej zrobić, bez powtarzania kodu
if  wiek >= 65:
    print(f'Cena za pobyt w hotelu przez {dlugosc_pobytu} dni, z rabatem emeryta, wynosi : {cena_pobytu:.2f} zł.')
else:
    print(f'Cena za pobyt w hotelu przez {dlugosc_pobytu} dni wynosi : {cena_pobytu:.2f} zł.')
