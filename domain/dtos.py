class NotaDTO():
    def __init__(self, idStud, idProb, nota):
        self.__idStud = idStud
        self.__idProb = idProb

        self.__nota = nota
        self.__note = []

        self.__numeStud = ""

    def getNumeStud(self):
        return self.__numeStud

    def setNumeStud(self, x):
        self.__numeStud = x

    def getProbID(self):
        return self.__idProb

    def getStudID(self):
        return self.__idStud

    def getNota(self):
        return self.__nota

    def adaugaNota(self, nota):
        self.__note.append(nota)
    def getMedie(self):
        if len(self.__note) > 0:
            total = 0
            for nota in self.__note:
                total += nota

            return total / len(self.__note)

        return 0.0


