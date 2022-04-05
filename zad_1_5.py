"""Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta (np.
z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o
takich bokach.
Wykorzystaj trzeci wzór z listy.
Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek
kwadratowy to:
import math
x = math.sqrt(10)"""

import math
a = float(input('Podaj długość boku "a": '))
b = float(input('Podaj długość boku "b": '))
c = float(input('Podaj długość boku "c": '))
p = 0.5 * (a + b + c)

if a < (b + c) and b < (a + c) and c < a + b:
    pole_trojkata = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print(f'Trójkąt poprawny, jego pole to {pole_trojkata} cm\u00b2.')
else:
    print(f'Nie da się złożyć trójkąta o wprowadzonych bokach'
          f'\na: {a:.2f} cm,'
          f'\nb: {b:.2f} cm,'
          f'\nc: {c:.2f} cm.')
    print()
    print(f'\nSpróbuj ponownie.')
