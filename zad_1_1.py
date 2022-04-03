"""Napisz program, który prosi użytkownika (przez input() ), żeby podał, ile kosztuje kilo
ziemniaków. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo
ziemniaków."""

# cena_ziemniaka = float(input("Podaj cenę kilograma ziemniaków: "))
# zaplata = cena_ziemniaka * 5
# print(f'5 kg ziemniaków kosztuje {zaplata:.2f} zł.')

"""Potem napisz program, który prosi użytkownika (przez input() ), żeby podał, ile kosztuje
kilo ziemniaków i ile kilo chce kupić. Niech program policzy i wyświetli, ile trzeba będzie
zapłacić za te ziemniaki."""

# cena_ziemniaka = float(input("Podaj cenę kilograma ziemniaków: "))
# waga_ziemniaka = float(input("Ile ziemniaków chcesz kupić? (kg): "))
# print(f'Twoje ziemniaki kosztują {cena_ziemniaka * waga_ziemniaka} zł.')

"""Potem napisz program, który prosi użytkownika (przez input() ), żeby podał, ile kosztuje
kilo ziemniaków, ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów
chce kupić. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i
banany razem. I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za
banany czy za ziemniaki."""

cena_ziemniaka = float(input("Podaj cenę kilograma ziemniaków (zł): "))
waga_ziemniaka = float(input("Ile ziemniaków chcesz kupić? (kg): "))
cena_banana = float(input("Podaj cenę kilograma bananów (zł): "))
waga_banana = float(input("Ile bananów chcesz kupić? (kg): "))
zaplata_ziemniak = cena_ziemniaka * waga_ziemniaka
zaplata_banan = cena_banana * waga_banana
print(f'Twoje zakupy kosztują {(zaplata_ziemniak + zaplata_banan):.2f} zł.')
if zaplata_ziemniak > zaplata_banan:
    print(f'Więcej zapłacisz za ziemniaki, {zaplata_ziemniak:.2f} zł.')
elif zaplata_banan > zaplata_ziemniak:
    print(f'Więcej zapłacisz za banany, {zaplata_banan:.2f} zł.')
else:
    print('Banany i ziemniaki kosztują po równo.')
