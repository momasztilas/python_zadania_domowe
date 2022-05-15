"""1. (Pominięte zadanie na zajęciach)
Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego. Klasa powinna umożliwiać pokonanie
zadanego dystansu, który nie może przekroczyć maksymalnego zasięgu zdefiniowanego dla samochodu. Samochód powinien
mieć także możliwość naładowania baterii.
>>> car = ElectricCar(100)
>>> car.drive(70)
70
>>> car.drive(50)
30
>>> car.drive(50)
0
>>> car.charge()
>>> car.drive(50)
50"""