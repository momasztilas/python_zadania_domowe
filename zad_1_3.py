"""Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze
współczynnik BMI, oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI:
wzór, interpretację wyników, proszę znaleźć samodzielnie)."""

wzrost = float(input('Podaj wzrost w cm: '))
masa = float(input('Podaj masę ciała w kg: '))
if wzrost > 0 and masa > 0:
    bmi = float(masa / ((wzrost / 100) ** 2))
    # WERSJA Z ROUND dla bmi, ponizej uzylem f-stringa dla treningu
    # bmi = round(float(masa/((wzrost/100) ** 2)),2)
    if bmi < 18.5:
        print(f'NIEDOWAGA! Twoje BMI to {bmi:.2f}'
              f'\nW sytuacji kiedy wskaźnik wskazuje niedowagę powinno to być  dla nas ostrzeżeniem.'
              f'\nW tych przypadkach stan swojego zdrowia powinno się skonsultować z lekarzem oraz wykonać zlecone badania,'
              f'\nktóre pomogą wykluczyć lub potwierdzić istnienie niektórych chorób istotnie wpływających na naszą masę ciała.')
    elif bmi >= 18.5 and bmi <= 24.99:
        print(f'WARTOŚĆ PRAWIDŁOWA! Twoje BMI to {bmi:.2f}'
              f'\nElegancko, BMI jest prawidłowe. '
              f'\nBadania wykazują, że osoby ze współczynnikiem w przedziale 18,5 – 24,99'
              f'\nnajdłużej cieszą się dobrym stanem zdrowia, jak również mają mniejsze ryzyko'
              f'\nwystąpienia niektórych chorób takich jak nadciśnienie tętnicze, cukrzyca typu 2 czy miażdżyca.')
    elif bmi >= 25 and bmi <= 29.99:
        print(f'NADWAGA! Twoje BMI to {bmi:.2f}'
              f'\nWarto zadbać o zmianę stylu życia, a przede wszystkim o codzienną,'
              f'\nzbilansowaną dietę i włączenie regularnej aktywności fizycznej.'
              f'\nOsoby z nadwagą powinny zmniejszyć ilość spożywania posiłków zawierających szkodliwe dla organizmu cukry.')
    elif bmi >= 30 and bmi <= 34.9:
        print(f'OTYŁOŚĆ I STOPNIA! Twoje BMI to {bmi:.2f}'
              f'\nSkonsultuj się z lekarzem, otyłośc jest przyczyną wielu chorób układu krążenia i cukrzycy.'
              f'\nWarto zadbać o zmianę stylu życia, a przede wszystkim o codzienną,'
              f'\nzbilansowaną dietę i włączenie regularnej aktywności fizycznej.')
    elif bmi >= 35 and bmi <= 39.9:
        print(f'OTYŁOŚĆ II STOPNIA! Twoje BMI to {bmi:.2f}'
              f'\nSkonsultuj się z lekarzem, otyłośc jest przyczyną wielu chorób układu krążenia i cukrzycy.'
              f'\nWarto zadbać o zmianę stylu życia, a przede wszystkim o codzienną,'
              f'\nzbilansowaną dietę i włączenie regularnej aktywności fizycznej.'
              f'\nIm wyższy stopień otyłości, tym większe ryzyko wystąpienia groźnych chorób, takich jak: '
              f'\nmiażdżyca, choroba niedokrwienna serca, udar mózgu, a nawet niektóre nowotwory.')
    elif bmi >= 40:
        print(f'OTYŁOŚĆ III STOPNIA! Twoje BMI to {bmi:.2f}!!!'
              f'\nBRUH')
else:
    print("Wprowadzono niepoprawne dane, spróbuj ponownie.")
