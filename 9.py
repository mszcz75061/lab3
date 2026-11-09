imie=str(input("Podaj imię: "))
print("Witaj, ", imie,)
wiek=int(input("Podaj wiek: "))
print("Twój wiek to: ", wiek)
nazwisko=str(input("Podaj nazwisko: "))
print("Twoje inicjały to: ", imie[0],nazwisko[0])
powtorzenie=str(input("Podaj tekst do powtórzenia: "))
print(powtorzenie * 5)
l1 = input("Podaj pierwszy tekst: ")
l2 = input("Podaj drugi tekst: ")
l3_polaczone = l1 + l2
print(f"Połączone tekst: {l3_polaczone}")
tekst1 = input("Podaj tekst główny: ")
tekst2 = input("Podaj drugi tekst (opcjonalny): ") # wczytany zgodnie z treścią zadania
polowa_dlugosci = len(tekst1) // 2
l3_polowa = tekst1[:polowa_dlugosci]
print(f"Pierwsza połowa pierwszego tekstu: {l3_polowa}")


