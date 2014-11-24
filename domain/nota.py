from domain.problema import Problema
from domain.student import Student


class Nota():
    def __init__(self, student, prob, nota):
        self.__student = student
        self.__prob = prob
        self.__nota = nota

    def getStudent(self):
        return self.__student

    def getProb(self):
        return self.__prob

    def getNota(self):
        return self.__nota

    def __eq__(self, other):
        if other == None:
            return False

        return self.getStudent() == other.getStudent() and self.getProb() == other.getProb()


def tests():
    c1 = Student(1, "Vasilica", "123")
    f1 = Problema(1, "How I", "whatever")

    r1 = Nota(c1, f1, 10)

    assert r1.getStudent() == c1
    assert r1.getProb() == f1


tests()