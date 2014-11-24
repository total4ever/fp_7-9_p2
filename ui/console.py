class Console():
    def __init__(self, ctrlStud, ctrlProb, ctrlNota):
        self.__ctrlStudent = ctrlStud
        self.__ctrlProb = ctrlProb
        self.__ctrlNota = ctrlNota

    def __meniu(self):
        print("1 - Adauga student")
        print("2 - Afisare student")

        print("3 - Adauga problema")
        print("4 - Afisare problema")

        print("5 - Modifica student")
        print("6 - Sterge student")

        print("7 - Modifica problema")
        print("8 - Sterge problema")

        print("9 - Adauga nota")

        print("media5 - Studenti cu media mai mica decat 5")
        print("note - Note laborator")

    def __cmd(self):
        return input("Comanda: ")

    def __adaugaStudent(self):
        id = int(input("ID student: "))
        name = input("Nume student: ")
        grup = input("Grup student: ")

        try:
            self.__ctrlStudent.add(id, name, grup)
        except ValueError as msg:
            print(msg)

    def __afiseazaStudenti(self):
        lista = self.__ctrlStudent.getAll()

        for item in lista:
            x = lista[item]
            print(x.getID(), ":", x.getName(), x.getGrup())

    def __adaugaProb(self):
        id = int(input("ID problema: "))
        desc = input("Descriere: ")
        dl = input("Deadline: ")

        try:
            self.__ctrlProb.add(id, desc, dl)
        except ValueError as msg:
            print(msg)

    def __afiseazaProbleme(self):
        lista = self.__ctrlProb.getAll()

        for item in lista:
            x = lista[item]
            print(x.getID(), ":", x.getDeadline(), x.getDescriere())

    def __modificaStud(self):
        id = int(input("ID stud: "))
        nume = input("Nume: ")
        gr = input("Grup: ")

        self.__ctrlStudent.update(id, nume, gr)

    def __stergeClient(self):
        id = int(input("ID student: "))

        self.__ctrlStudent.remove(id)

    def __modificaProblema(self):
        id = int(input("ID problema: "))
        titlu = input("Descriere noua: ")
        dl = input("Deadline nou: ")

        self.__ctrlProb.update(id, titlu, dl)

    def __stergeProb(self):
        id = int(input("ID probelma: "))

        self.__ctrlProb.remove(id)

    def __adaugaNota(self):
        studID = int(input("ID student: "))
        probID = int(input("ID problema: "))
        nota = float(input("Nota: "))

        try:
            self.__ctrlNota.add(studID, probID, nota)
        except ValueError as msg:
            print(msg)


    def __raport1(self):
        probID = int(input("ID problema: "))
        for x in self.__ctrlNota.listaStudProb(probID):
           print(x.getNumeStud(), x.getNota())

    def __raport2(self):
        for x in self.__ctrlNota.media5():
            print(x.getNumeStud(), x.getMedie())

    def startUI(self):

        while True:
            self.__meniu()
            cmd = self.__cmd()

            if cmd == "1":
                self.__adaugaStudent()
            if cmd == "2":
                self.__afiseazaStudenti()
            if cmd == "3":
                self.__adaugaProb()
            if cmd == "4":
                self.__afiseazaProbleme()
            if cmd == "5":
                self.__modificaStud()
            if cmd == "6":
                self.__stergeClient()
            if cmd == "7":
                self.__modificaProblema()
            if cmd == "8":
                self.__stergeProb()
            if cmd == "9":
                self.__adaugaNota()

            if cmd == "r1":
                self.__raport1()
            if cmd == "r2":
                self.__raport2()