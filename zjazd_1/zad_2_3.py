"""
Napisz program, który odczytuje od użytkownika wiele liczb.
Program powinien wyliczyć i na końcu wypisać następujące statystyki:

liczba podanych liczb (ile sztuk),
suma,
średnia,
minimum
maksimum

NIE używaj funkcji wbudowanych!

"""

import statistics
import math
liczby = []
i = 1

while i <= 10:
    liczba = int(input(f'Wprowadź liczbę nr {i}: '))
    # jak inaczej wprowadzić wartości, bez użycia wbudowanego input?
    i += 1
    liczby.append(liczba)

def mymax(liczby):
    max = liczby[0]
    for x in liczby:
        if x > max:
            max = x
        return max
def mymin(liczby):
    min = liczby[0]
    for y in liczby:
        if y < min:
            min = y
    return min

print (f'Wprowadziłeś {len(liczby)} liczb.')
print (f'Suma wprowadzonych liczb to {math.fsum(liczby)}')
print (f'Średnia wprowadzonych liczb to {statistics.mean(liczby)}')
print (f'Najmniejsza wprowadzona liczba to {mymin(liczby)}')
print (f'Największa wprowadzona liczba to {mymax(liczby)}')

