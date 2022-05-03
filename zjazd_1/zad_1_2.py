"""Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca
(poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru. Jeśli tak będzie ci
wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni."""

tydzien = ('poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota' , 'niedziela')

# W MOIM PROGRAMIE SZEWC OTWARTY JEST W NIEDZIELĘ! (GALERIA HANDLOWA)
# zakładam, że w dzień oddania butów zaczyna się ich naprawa,
# tj oddane w poniedziałek z realizacją 7 dni będą gotowe do odbioru w następny poniedziałek.

poczatek = int(input('Którego dnia oddano buty do naprawy [1-7]? '))
if poczatek >= 1 and poczatek <= 7:
    czas_naprawy = int(input('Ile dni potrwa naprawa? '))
    koniec = (poczatek + czas_naprawy - 1) % 7
    dzien_odbioru = tydzien[koniec]
    print(f'Dzien odbioru butów to {dzien_odbioru}')
else:
    print('Wprowadziłeś dzień poza zakresem, uruchom program ponownie.')





