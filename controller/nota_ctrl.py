from domain.dtos import NotaDTO
from domain.problema import Problema
from domain.nota import Nota
from domain.student import Student
from domain.val_nota import NotaValidator
from repository.problema_repo import ProblemaRepo
from repository.nota_repo import NotaRepo
from repository.student_repo import StudentRepo

class RentCtrl():
    def __init__(self, val, studRepo, probRepo, notaRepo):
        self.__val = val
        self.__studRepo = studRepo
        self.__probRepo = probRepo
        self.__notaRepo = notaRepo

    def add(self, studID, probID, nota):
        std = self.__studRepo.find(studID)
        prob = self.__probRepo.find(probID)

        g = Nota(std, prob, nota)

        self.__val.validate(g)
        self.__notaRepo.add(g)

    def listaStudProb(self, probID):
        lista = self.__notaRepo.getAllDTO()
        final = []

        for x in lista:

            if x.getProbID() == probID:
                y = NotaDTO(x.getStudID(), x.getProbID(), x.getNota())
                y.setNumeStud(self.__studRepo.find(x.getStudID()).getName())
                final.append(y)

        return final

    def media5(self):
        lista = self.__notaRepo.getAllDTO()
        final = []

        for x in lista:
            poz = -1

            for i in range(len(final)):
                if x.getStudID() == final[i].getStudID():
                    poz = i

            if poz == -1:
                y = NotaDTO(x.getStudID(), 0, 0)
                y.adaugaNota(x.getNota())

                final.append(y)
            else:
                final[poz].adaugaNota(x.getNota())

        final2 = []
        for i in range(len(final)):
            if final[i].getMedie() < 5:
                final[i].setNumeStud(self.__studRepo.find(final[i].getStudID()).getName())
                final2.append(final[i])

        return final2


def tests():
    val = NotaValidator()
    clientRepo = StudentRepo()
    filmRepo = ProblemaRepo()
    rentRepo = NotaRepo()

    ctrl = RentCtrl(val, clientRepo, filmRepo, rentRepo)


    clientRepo.add(Student(1, "Paul", "123"))
    clientRepo.add(Student(2, "Vasilica", "456"))
    clientRepo.add(Student(3, "Gheorghe", "789"))

    filmRepo.add(Problema(1, "F1", "d1"))
    filmRepo.add(Problema(2, "f2", "d2"))
    filmRepo.add(Problema(3, "f3", "d3"))
    filmRepo.add(Problema(4, "f4", "d4"))

    ctrl.add(1, 2, 5)
    ctrl.add(2, 3, 9)
    ctrl.add(3, 1, 9)
    ctrl.add(1, 4, 7)
    ctrl.add(1, 3, 1)
    ctrl.add(3, 2, 9)

    #for x in ctrl.listaStudProb(3):
    #    print(x.getNumeStud(), x.getNota())

    #for x in ctrl.media5():
    #    print(x.getNumeStud(), x.getMedie())


tests()