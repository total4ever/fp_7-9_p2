from domain.problema import Problema
from domain.dtos import NotaDTO
from domain.nota import Nota
from domain.student import Student


class NotaRepo():
    def __init__(self):
        self.__data = []

    def add(self, x):
         self.__data.append(x)

    def getAllDTO(self):
        final = []
        for item in self.__data:
            x = NotaDTO(item.getStudent().getID(), item.getProb().getID(), item.getNota())
            final.append(x)
        return final


def tests():
    c1 = Student(1, "Vaile", "123")
    c2 = Student(2, "Ion", "123")
    c3 = Student(3, "Maria", "123")

    f1 = Problema(1, "Godfather", "EPIC")
    f2 = Problema(2, "Saw", "Mai epic")

    repo = NotaRepo()

    r1 = Nota(c1, f1, 9)
    r2 = Nota(c1, f2, 8)
    r3 = Nota(c2, f1, 5)
    r4 = Nota(c3, f2, 10)

    repo.add(r1)
    repo.add(r2)
    repo.add(r3)
    repo.add(r4)

    assert len(repo.getAllDTO()) == 4



tests()