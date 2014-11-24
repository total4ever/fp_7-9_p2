from domain.problema import Problema
from domain.val_problema import ProblemaValidator
from repository.problema_repo import ProblemaRepo


class ProbCtrl():
    def __init__(self, val, repo):
        self.__val = val
        self.__repo = repo

    def add(self, id, descr, deadline):
        x = Problema(id, descr, deadline)

        self.__val.validate(x)
        self.__repo.add(x)

    def remove(self, id):
        self.__repo.remove(id)

    def update(self, id, descr, deadline):
        x = Problema(id, descr, deadline)
        self.__repo.update(x)

    def getAll(self):
        return self.__repo.getAll()


# # TESTS

def tests():
    repo = ProblemaRepo()
    val = ProblemaValidator()

    ctrl = ProbCtrl(val, repo)

    ctrl.add(1, "Film 1", "Actiune")

    assert len(ctrl.getAll()) == 1

    ctrl.add(2, "Film 2", "Alta actiune")
    ctrl.update(2, "Film x", "Epic...")

    x = ctrl.getAll()

    assert x[2].getDeadline() == "Epic..."


tests()