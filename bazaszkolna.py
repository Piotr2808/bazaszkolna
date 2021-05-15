
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

teachers_list = []
student_list = []
tutor_list = []
group_list = []

class Teacher: #Nauczyciel
    def __init__(self, name, group, subject):
        self.name = name
        self.subject = subject
        self.group = group

    def data_teacher(self): #format
        return{name: {"group": self.group, "subject": self.subject}}

class Tutor: #Wychowawca
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def data_tutor(self): #format
        return{"name" :self.name, "group": self.group}

class Studnet: #Uczeń
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def data_student(self): #format
        return{"name": self.name, "group": self.group}


commands = ("Teacher", "Tutor", "Student", "Information", "End")

while True:
    print(commands)
    command = input("User type: ").title()

    if not command in commands:
        continue

    if command == "End": #Kończy program
        break

    if command == "Teacher":
        class_list = [] #lista klas
        subject_list = [] # lista przedmiotów
        name = input("Your name: ")
        list = ["yes"]
        if_tutor = input('If you are tutor? [yes/no]: ').lower() #Opcja dodanien wychowacy z koendy nauczyciela

        if if_tutor == "yes":
            your_class = input("Your class: ")
            tutor = Tutor(name, your_class)
            tutor_list.append(tutor.data_tutor())

            if not your_class in class_list:
                class_list.append(your_class)

        if name in teachers_list: #Aby nie powielać
            print("User saved.")

        if not name in teachers_list:

            while True:
                subject = input("Subject: ")

                if not subject:
                    break
                subject_list.append(subject)

            while True:
                group = input("Your class: ")

                if not group:
                    break
                class_list.append(group) # Dodaje klasy do listy klas.

                if not group in group_list:
                    group_list.append(group) # Dodaje klasy do globalnej listy klas.

            teach = Teacher(name, class_list, subject_list) # Dodaje do lity nauczycieli w foramcie.
            teachers_list.append(teach.data_teacher())

    if command == "Tutor":
        search = ["Search Tutor", "Add Tutor"] # Opcja wyszukania lub dodania wychowawcy klasy
        search_ = input("Function: [Search Tutor/Add Tutor: ").title()

        if search_ == "Add Tutor": # Dodaje naucziciela
            name = input("Tutor name: ")

            if name in tutor_list: # Jeśli wychowaca jest już na liście, a chcemy mu przydzielić klasę.
                tutor_list.append(["name"] + "group")
                group = input("Add class: ")

                if not group in group_list:
                    group_list.append(group) # Dodaje do globalnej listy klas

            else: # Jeśli nie ma na liście wychowawcy.
                group = input("Your class: ")

                if not group in group_list:
                    group_list.append(group)

                tutor = Tutor(name, group)
                tutor_list.append(tutor.data_tutor())

        if search_ == "Search Tutor": # Do poprawki wyszukiwarka
            print(tutor_list)
            class_ = input("Class: ")

            if class_ in tutor_list:
                print("Class: Tutor")


    if command == "Student":
        name = input("Name: ").title() # Dodaje ucznia
        group = input("Your class: ")

        if not group in group_list: # Dodaje klase do globalnej listy klas.
            group_list.append(group)

        stu = Studnet(name, group)
        student_list.append(stu.data_student())

    if command == "Information": # Wszystki informacje.
        print(f"Teachers list: {teachers_list}")
        print(f"student list {student_list}")
        print(f"Tutor list: {tutor_list}")
        print(f"Class list: {group_list}")