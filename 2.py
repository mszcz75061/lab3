licznik = 0
liczba = 2
wynik = []

while True:
    # Sprawdzamy, czy zmienna 'liczba' jest pierwsza
    czy_pierwsza = True
    dzielnik = 2

    while dzielnik * dzielnik <= liczba:
        if liczba % dzielnik == 0:
            czy_pierwsza = False
            break  # Przerywamy pętlę sprawdzającą, gdy znajdziemy dzielnik
        dzielnik += 1

    if czy_pierwsza:
        wynik.append(str(liczba))
        licznik += 1

    # Jeśli znaleźliśmy 10 liczb pierwszych, przerywamy główną pętlę
    if licznik == 10:
        break

    liczba += 1

# Łączymy liczby przecinkiem i wypisujemy wynik
print(",".join(wynik))