from domain.student import Student
from domain.val_student import StudentValidator
from repository.student_repo import StudentRepo


class StudentCtrl():
    def __init__(self, val, repo):
        self.__val = val
        self.__repo = repo

    def add(self, id, name, grup):
        x = Student(id, name, grup)

        self.__val.validate(x)
        self.__repo.add(x)

    def remove(self, id):
        self.__repo.remove(id)

    def update(self, id, nume, grup):
        x = Student(id, nume, grup)
        self.__repo.update(x)

    def getAll(self):
        return self.__repo.getAll()


def tests():
    repo = StudentRepo()
    val = StudentValidator()

    ctrl = StudentCtrl(val, repo)

    ctrl.add(1, "Vasile", "123")

    assert len(ctrl.getAll()) == 1

    ctrl.add(2, "Ion", "456")
    ctrl.update(2, "Gheorghe", "789")

    x = ctrl.getAll()

    assert x[2].getName() == "Gheorghe"

tests()