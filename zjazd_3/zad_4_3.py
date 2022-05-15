"""
3. Zmoyfikuj klasę Ulamek (z zajęć) tak, aby:
    - dodawanie i mnożenie można było wykonać nie tylko z innym Ulamkiem, ale też z intem,
    niezależnie po której stronie działania się znajdzie (tj. powinno działać zarówno `x * 5` jak i `5 * x`)
    - możliwa była zmiana znaku Ulamka (metoda __neg__())
    - możliwe było wykorzystanie operatorów logicznych: <, <=, >, >=, ==, !=
    działających dla porówniań ułamka z ułamkiem, ułamka z intem i inta z ułamkiem.
    - (*) po każdym działaniu na Ulamku był on w postaci nieskracalnej
    (tzn. 1/4 + 1/4 powinno dać w wyniku ułamek 1/2 a nie 2/4)"""