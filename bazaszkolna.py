
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
uczniowie = {'Karol': '3',
             'Ola': '3',
             'Anka': '4'
             } # {imie: klasa}

nauczyciele = {'Anka': {'przyroda': ['3']},
               'Klaudia': {'religia': ['4']},
                'Artur': {'Niemiecki': ['3']}
                }

                # {imie: {przedmiot: [klasy]}}

wychowawcy = {'patryk': '3'
              } # {imie: klasy}

class Uczen:
    def __init__(self, imie, klasa):
        self.imie = imie
        self.klasa = klasa

    def format_uczen(self):
        return{self.imie: self.klasa}

class Nauczyciel:
    def __init__(self, imie, przedmiot, klasy):
        self.imie = imie
        self.przedmiot = przedmiot
        self.klasy = klasy

    def format_nauczyciel(self):
        return{self.imie: {self.przedmiot: self.klasy}}

class Wychowawca:
    def __init__(self, imie, klasa):
        self.imie = imie
        self.klasa = klasa
    def format_wychowawca(self):
        return{imie: klasa}

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
                u = Uczen(name, klasa)
                uczniowie.update(u.format_uczen())
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
                n = Nauczyciel(imie, przedmiot, klasy_)
                nauczyciele.update(n.format_nauczyciel())
            print(nauczyciele)

    if komenda == "Wychowawca":
        while True:
            name = input("Imię i nazwisko: ")
            if name:
                klasa = input("Wychowawca klasy: ")
                w = Wychowawca(name, klasa)
                wychowawcy.update(w.format_wychowawca())
                print(wychowawcy)
            if not name:
                break
polecenia = ["Uczeń", "Nauczyciel", "Nazwa Klasy", "Wychowawca"]
while True:
    print(polecenia)
    komenda = input("Komenda: ").title()

    if komenda == "Nazwa Klasy":
        klasa = input("Szukam klasy: ")
        for k, value in wychowawcy.items():
            if klasa == value:
                print(f"Wychowawca: {k}")
        for i, value in uczniowie.items():
            if klasa == value:
                print(f"Uczeń: {i}")

    if komenda == "Wychowawca":
        print(wychowawcy.keys())
        wychowawca = input("Imię wychowawcy: ")
        for imie, klasa in wychowawcy.items():
            if wychowawca == imie:
                print(f"Wychowawca klasy {klasa}: {wychowawca}")
                for i, grupa in uczniowie.items():
                    if klasa == grupa:
                        print(f"uczniowie klasy: {i}")

    if komenda == "Nauczyciel":
        nauczyciel = input("Nauczyciel: ")
        if nauczyciel:
            for n in nauczyciele[nauczyciel].values():
                klasy = n
                for klasa in klasy:
                    for w, value in wychowawcy.items():
                        if klasa == value:
                            print(f"Wychowawcy w klasach {klasa}: {w}")

    if komenda == "Uczeń": # uczeń: wypisz wszystkie lekcje, które ma uczeń i nauczycieli, którzy je prowadzą
        print(uczniowie.keys())
        uczen = input("Imie ucznia: ")
        for u, value in uczniowie.items():
            if uczen == u:
                lista = []
                lista.append(value)
                for i, values in nauczyciele.items():
                    for przedmiot, klasy in values.items():
                        if lista == klasy:
                            print(f"Nauczyciel: {i}\nprzedmiot: {przedmiot}")

    if komenda == "":
        break