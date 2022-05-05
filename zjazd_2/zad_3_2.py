"""

Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
Logikę obliczania liczby dni wydziel do osobnej funkcji.
Wersja A Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
Wersja B (trudniejsza) Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty
był przestępny czy nie."""

miesiace = {
    'styczeń': 31,
    'luty': 28,
    'marzec': 31,
    'kwiecień': 30,
    'maj': 31,
    'czerwiec': 30,
    'lipiec': 31,
    'sierpień': 31,
    'wrzesień': 31,
    'październik': 31,
    'listopad': 30,
    'grudzień': 31
}

odpowiedz = (input('Podaj nazwę miesiąca: '))
if odpowiedz in miesiace:
    pass
else:
    print(f'Nie ma takiego miesiąca {odpowiedz}')
    quit()
# to ponizej wciagnac do elifa tam wyzej
if odpowiedz == 'luty':
    rok = int(input('Podaj rok: '))
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        miesiace['luty'] = 29
    else:
        pass
else:
    pass
print(f'Miesiąc {odpowiedz} ma {miesiace.get(odpowiedz)} dni.')


""" 
tu pomysł z napisaniem funkcj zwracajacej true/false - zamysl byl taki, zeby odpowiedz luty odpalala funkcje
rok przestepny, ktory przy true dla podanego roku zaktualizuje slownik dla klucza luty do 29 zamiast bazowych 28.
Prawdopodobnie z bledami.

def rok_przestepny(rok):
    return (rok % 4 == 0 and (rok % 100 != 0) or (rok % 400 == 0)

rok_przestepny(rok)    

if rok_przestepny(rok) == True:
    miesiace['luty'] = 29
else:
    pass
            
"""

# rok_przestepny()
