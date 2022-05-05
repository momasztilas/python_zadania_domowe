"""Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie
wykona odpowiednie operacje i zwróci odpowiedni wynik.

lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)

suma(liczby) - zwraca sumę liczb z listy liczby - postaraj się nie używać
funkcji sum wbudowanej w pythona
srednia(liczby) - zwraca średnią wartość z listy liczby
max(liczby) – zwraca największą wartość z listy liczby - postaraj się nie
używać funkcji max wbudowanej w pythona
roznica_min_max(liczby) – różnica pomiędzy największą a najmniejszą liczbą
w liście; 0 jeśli tablica jest pusta
wypisz_wieksze(liczby, x) – wypisuje ( print() ) wszystkie te liczby z listy
liczby , które są większe od x
pierwsza_wieksza(liczby, x) – zwraca ( return ) pierwszą znalezioną w
liczby liczbę większą od x ; zwraca None , jeśli takiej liczby tam nie ma
suma_wiekszych(liczby, x) – zwraca ( return ) sumę liczb z listy
liczby , które są większe niż x
ile_wiekszych(liczby, x) – liczy ile elementów listy liczby jest większych
od liczby x
wypisz_podzielne(liczby, x) – wypisuje ( print ) wszystkie te liczby z listy
liczby , które są podzielne przez x
pierwsza_podzielna(liczby, x) – zwraca ( return ) pierwszą znalezioną w
liczby liczbę podzielną przez x ; zwraca None , jeśli takiej liczby tam nie ma
znajdz_wspolny(liczby1, liczby2) – zwraca element (liczbę), który
występuje zarówno w liście liczby1 , jak i liczby2 ; zwraca None , jeśli takiego
elementu nie ma
"""

lista_liczb = [10, 20, 30, 40, 1000, 34, 69, 420, 888]
print(f'Wejściowa lista liczb to: {lista_liczb}')
lista_liczb.sort()
print(f'Lista liczb po sortowaniu (asc): {lista_liczb}')
# suma liczb

def suma(lista_liczb: list) -> float:
    """
    Funkcja zwraca sume liczb z podanej listy
    :param lista_liczb: lista liczb wprowadzonych do programu
    :return: suma liczb
    """
    total: float = 0  # ten float nie okresla rodzaju danych i printowany jest int podobnie jak poniżej w maksimum
    for liczba in lista_liczb:
        total += liczba
    return total


print(f'Wynik sumowania liczb z listy {lista_liczb} to: {suma(lista_liczb)}')


# średnia


def srednia(lista_liczb: list) -> float:
    """
    Funkcja zwraca srednia z sumy liczb z wprowadzonej listy
    :param lista_liczb: lista liczb wprowadzonych do programu
    :return: srednia z liczb
    """
    average: float = suma(lista_liczb) / len(lista_liczb)
    return average


# przy okazji okreslania typu wartosci average na float ten sposob dziala,
# w przypadku sumy i maksa musialem okreslic rodzaj danych przy return - co robię źle?

print(f'Wynik średniej z sumy liczb w liście {lista_liczb} to: {srednia(lista_liczb)}')


# max

def maksimum(lista_liczb: list) -> float:
    """
    :param lista_liczb: lista liczb
    :return: maksymalna wartośś w podanej liście
    """
    lista_liczb.sort(reverse=True)
    maks: float = lista_liczb[0]
    return maks
    # tu okreslenie typu maks w linii 75 nic nie daje w ostatecznym wyniku, wartosc printuje sie bez wartosci po
    # przecinku.


print(f'Maksymalna wartość listy {lista_liczb} to {maksimum(lista_liczb)}')


# różnica min_max


def min_maks_diff(lista_liczb: list) -> float:
    """
    :param lista_liczb: lista wprowadzonych liczb
    :return: różnica wartości skrajnych z listy
    """
    lista_liczb.sort()
    minimum = lista_liczb[0]
    if lista_liczb is None:  # czy to zadziała jak powinno? Nie bardzo rozumiem polecenie z 0 gdy tablica bedzie pusta
        return 0
    else:
        return float(maksimum(lista_liczb) - minimum)


lista_liczb.sort()

print(f'Różnica skrajnych wartości z listy {lista_liczb} to {min_maks_diff(lista_liczb)}')
# powyższy print wypisuje liste posortowana po pierwszym sorcie w funkcji maksimum, czy jest opcja na obejście tego?
# wykorzystalem podwojne sortowanie - na poczatku przed funkcjami i po funkcjach