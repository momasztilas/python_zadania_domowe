"""
Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu
liniach "choinkę" ze znaków * . Np. dla parametru 3 powinno się wypisać:

    *
  * * *
* * * * *

"""

wielkosc_choinki = int(input('Wprowadź liczbę poziomów choinki: '))

i = 1
while i < wielkosc_choinki + 1:
    print(" " * (2 * wielkosc_choinki - 2 * i), " #" * i, "# " * (i-1))
    i += 1
