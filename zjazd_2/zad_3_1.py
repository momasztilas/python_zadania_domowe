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
from typing import List


def stopy_na_metry():
    stopy = float(input("Podaj ilość stóp: "))
    dzialanie = stopy * 0.3048
    print(f"{stopy} ft. to {dzialanie:.2f} m.")


# max

def funkcja_max():
    liczby_max: List[float] = []
    if len(liczby_max) > 2:
        pass
    else:
        liczby_max.append(float(input("Podaj liczbę nr 1: ")))
        liczby_max.append(float(input("Podaj liczbę nr 2: ")))

    maximum = liczby_max[0]
    for x in liczby_max:
        if x > maximum:
            maximum = x
    print(f"Max z podanych liczb {liczby_max} to: {maximum}")


# srednia - oblicza średnią z dwóch liczb

def funkcja_srednia():
    liczby_srednia = []
    suma = 0
    for i in liczby_srednia:
        suma = suma + i
    print(f"Średnia arytmetyczna z podanych liczb {liczby_srednia} wynosi: {(suma / len(liczby_srednia)):.2f}")


# pole_kola - oblicza pole koła o podanym promieniu (jeden parametr) podpowiedź:
# wartość PI jest dostępna jako Math.PI

def funkcja_pole_kola():
    promien = float(input(f"Podaj promień koła: "))
    pole = promien ** 2 * math.pi
    print(f"Pole koła o promieniu {promien:.2f} cm wynosi {pole:.2f} cm\u00b2.")


# bmi - oblicza współczynnik BMI dla podanych dwóch parametrów:
# wzrostu w metrach i wagi w kg.

def funkcja_bmi():
    wzrost = float(input('Podaj wzrost w cm: '))
    waga = float(input('Podaj masę ciała w kg: '))
    if wzrost < 0 and waga < 0 or waga < 0 or wzrost < 0:
        print("Wprowadzono niepoprawne dane, spróbuj ponownie.")
    else:
        bmi = float(waga / ((wzrost / 100) ** 2))
        print(f'BMI obliczone dla wzrostu {wzrost:.2f} cm i wagi {waga:.2f} kg to {bmi:.2f}')


# pole_trojkata - z trzema parametrami - oblicza pole trójkąta o podanych bokach
# z wzoru Herona.

def funkcja_pole_trojkata():
    a = float(input('Podaj długość boku "a": '))
    b = float(input('Podaj długość boku "b": '))
    c = float(input('Podaj długość boku "c": '))
    p = 0.5 * (a + b + c)

    if a < (b + c) and b < (a + c) and c < a + b:
        pole_trojkata = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f'Trójkąt poprawny, jego pole to {pole_trojkata:.2f} cm\u00b2.')
    else:
        print(f'Nie da się złożyć trójkąta o wprowadzonych bokach'
              f'\na: {a:.2f} cm,'
              f'\nb: {b:.2f} cm,'
              f'\nc: {c:.2f} cm.')
        print()
        print(f'\nSpróbuj ponownie.')


# kilometry_na_mile - przelicza odległość wyrażoną w kilometrach na mile, treningowo z

def funkcja_km_mile(km: float) -> float:
    """
    Funkcja przelicza odleglosc w kilometrach na mile
    :param km: odleglosc w km
    :return: odleglosc w milach
    """
    return km / 1.61


# mile_na_kilometry - przelicza odległość wyrażoną w milach na kilometry

def funkcja_mile_km(mile: float) -> float:
    """
    Funkcja przelicza odleglosc w milach na kilometry
    :param mile: odleglosc w milach
    :return: odleglosc w km
    """
    return mile * 1.61


print("Czołgiem, w programie dostępne są poniższe operacje:")

print()

print("operacja 1 - przeliczanie stóp na metry"
      "\noperacja 2 - maksimum z 2 podanych liczb"
      "\noperacja 3 - średnia z 2 podanych liczb"
      "\noperacja 4 - obliczanie pola koła o promieniu r"
      "\noperacja 5 - obliczanie bmi na podstawie wzrostu i wagi"
      "\noperacja 6 - obliczanie p.pow trójkąta ze sprawdzeniem"
      "\noperacja 7 - przeliczanie kilometrów na mile"
      "\noperacja 8 - przeliczanie mil na kilometry")
print()

task = input("Jaki rodzaj operacji chcesz wykonać?: ")
if task == "1" or task == "operacja 1":
    stopy_na_metry()
elif task == "2" or task == "operacja 2":
    funkcja_max()
elif task == "3" or task == "operacja 3":
    funkcja_srednia()
elif task == "4" or task == "operacja 4":
    funkcja_pole_kola()
elif task == "5" or task == "operacja 5":
    funkcja_bmi()
elif task == "6" or task == "operacja 6":
    funkcja_pole_trojkata()
elif task == "7" or task == "operacja 7":
    # troche inne wywolanie funkcji 7 i 8
    operacja7 = funkcja_km_mile(float(input(f'Wprowadź liczbę kilometrów: ')))
    print(f'Wprowadzoną odległość w kilometrach przeliczono na {operacja7:.2f} mi.')
elif task == "8" or task == "operacja 8":
    operacja8 = funkcja_mile_km(float(input(f'Wprowadź liczbę mil: ')))
    print(f'Wprowadzoną odległość w milach przeliczono na {operacja8:.2f} km.')
else:
    print(f'Nie ma takiej operacji {task}.')
