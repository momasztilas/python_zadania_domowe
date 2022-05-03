"""
ZADANIE 3.1
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i
zwraca przeliczoną wartość.

1. stopy_na_metry - przelicza odległość wyrażoną w stopach na metry,
2. max - zwraca większą z dwóch liczb - postaraj się nie używać funkcji max
wbudowanej w pythona
3. srednia - oblicza średnią z dwóch liczb,
4. pole_kola - oblicza pole koła o podanym promieniu (jeden parametr) podpowiedź:
wartość PI jest dostępna jako Math.PI
5. bmi - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w
metrach i wagi w kg.
6. pole_trojkata - z trzema parametrami - oblicza pole trójkąta o podanych bokach
z wzoru Herona.
7. kilometry_na_mile - przelicza odległość wyrażoną w kilometrach na mile
8. mile_na_kilometry - przelicza odległość wyrażoną w milach na kilometry

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują
wynik.

"""

# stopy na metry
import math


def stopy_na_metry():
    stopy = float(input("Podaj ilość stóp: "))
    dzialanie = stopy * 0.3048
    print(f"{stopy} ft. to {dzialanie:.2f} m.")


# max
liczby = []

if len(liczby) > 2:
    pass
else:
    liczby.append(float(input("Podaj liczbę nr 1: ")))
    liczby.append(float(input("Podaj liczbę nr 2: ")))


def funkcja_max(liczby):
    maximum = liczby[0]
    for x in liczby:
        if x > maximum:
            maximum = x
    return maximum


print(f"Max z dwóch podanych liczb to: {funkcja_max(liczby):.2f}")


# srednia - oblicza średnią z dwóch liczb

def funkcja_srednia(liczby):
    suma = 0
    for i in liczby:
        suma = suma + i
    return suma / len(liczby)


print(f"Średnia arytmetyczna z podanych liczb wynosi: {funkcja_srednia(liczby):.2f}")

funkcja_max(liczby)
funkcja_srednia(liczby)
print(f"Lista podanych liczb to {liczby}")


# pole_kola - oblicza pole koła o podanym promieniu (jeden parametr) podpowiedź:
# wartość PI jest dostępna jako Math.PI

def funkcja_pole_kola():
    promien = float(input(f"Podaj promień koła: "))
    pole = promien ** 2 * math.pi
    print(f"Pole koła o promieniu {promien:.2f} cm wynosi {pole:.2f} cm\u00b2.")


funkcja_pole_kola()
