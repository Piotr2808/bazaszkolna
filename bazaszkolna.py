
'''
Mamy trzy typy użytkowników:

Wychowawca - ma przypisane klasy
Nauczyciel - Mentor ma przypisany przedmiot i wiele klas
Uczeń - jest przypisany do jednej klasy

Napisz program, który ze standardowego wyjścia pobierze dane w następujący sposób:

Pobierze typ użytkownika: (uczeń, nauczyciel, wychowawca, koniec), oraz Imię i nazwisko Jeśli pobrano koniec,
przejdź do kroku 5
Jeśli typ użytkownika to uczeń, pobierz jedną linię - będzie to nazwa klasy (np. 3C), przejdź do kroku 1

Jeśli typ użytkownika to nauczyciel, pobierz 1 linię - nazwę przedmiotu prowadzonego,
a następnie w nowych liniach nazwy klas, aż do otrzymania pustej linii. Przejdź do korku 1
Jeśli typ użytkownika to wychowawca, pobieraj w nowych liniach nazwy klas, które prowadzi wychowawca,
aż do pustej linii, przejdź do kroku 1
Wykonaj polecenie na podstawie przekazanego argumentu

Program będzie wykonywany w następujący sposób (zakładając nazwę pliku bazaszkolna.py)
python bazaszkolna.py <phrase>
jeśli phrase to nazwa klasy: program wypisze wychowawcę i uczniów w klasie
jeśli phrase to wychowawca: wypisz wszystkich uczniów, których prowadzi wychowawca
jeśli phrase to nauczyciel: wypisz wychowawców wszystkich klas, z którym ma zajęcia nauczyciel
jeśli phrase to uczeń: wypisz wszystkie lekcje, które ma uczeń i nauczycieli, którzy je prowadzą
'''

komendy = ["Uczeń", "Nauczyciel", "Wychowawca", "Koniec"]
uczniowie = {}
nauczyciele = {}
wychowawcy = {}

while True:

    print(komendy)
    komenda = input("Użytkownik: ").title()
    if komenda == "Koniec":
        break

    if komenda == "Uczeń":
        while True:
            name = input("Imię i nazwisko: ")
            if name:
                klasa = input("Klasa: ")
                uczen = {name: klasa}
                uczniowie.update(uczen)
                print(uczniowie)
            if not name:
                break

    if komenda == "Nauczyciel":
        imie = input("Imię: ")
        przedmiot = input("Przedmiot: ")
        klasy_ = []
        while True:
            klasy = {input("Jakie klasy nauczasz?: ")}
            if klasy == {""}:
                break
            if klasy:
                klasy_ += klasy
                nauczyciele.update({imie: {przedmiot: klasy_}})
            print(nauczyciele)

    if komenda == "Wychowawca":
        while True:
            name = input("Imię i nazwisko: ")
            if name:
                klasa = input("Wychowawca klasy: ")
                wychowawca = {name: klasa}
                wychowawcy.update(wychowawca)
                print(wychowawcy)
            if not name:
                break

while True:
    komenda = input("Komenda: ")
    if komenda == "nazwa klasy":
        klasa = input("Szukam klasy: ")
        for k, value in wychowawcy.items():
            if klasa == value:
                print(f"Wychowawca: {k}")
        for i, value in uczniowie.items():
            if klasa == value:
                print(f"Uczeń: {i}")
    if komenda == "wychowawca":
        wychowawca = input("Wychowawca: ")

    if komenda == "":
        break