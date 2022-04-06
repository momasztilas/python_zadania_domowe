"""Założenia: - 0-6 - wiek przedszkolny - cena biletu: 0 - 7-17 - wiek szkolny - cena biletu: 2.28 -
18-64 - wiek dorosły - cena biletu: 3.80 - +65 - wiek emerytalny - cena biletu: 1.90
Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile
biletów chce kupić.
Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić.
Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli."""

wiek = int(input('Podaj wiek kupującego bilet: '))
ilosc = int(input('Podaj ilość biletów: '))
if wiek > 0 and ilosc > 0:
    if 0 <= wiek <= 6:
        cena_biletu = 0
        typ = "ulga przedszkolaka"
    elif 7 <= wiek <= 17:
        cena_biletu = 2.28
        typ = "ulga szkolna"
    elif 18 <= wiek <= 64:
        cena_biletu = 3.8
        typ = "brak"
    elif 65 <= wiek:
        cena_biletu = 1.9
        typ = "ulga emeryta"
    cena = ilosc * cena_biletu
    print(f'Ilość kupionych biletów to: {ilosc}\nRodzaj zastosowanej ulgi: {typ}\nDo zapłaty: {cena:.2f} zł')
else:
    print('Wprowadzono niepoprawne wartości, spróbuj ponownie')
