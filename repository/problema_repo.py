from domain.problema import Problema


class ProblemaRepo():

    def __init__(self):
        self.__data = {}

    def add(self, item):

        if item.getID() in self.__data:
            raise ValueError("Problema existenta deja")

        self.__data[item.getID()] = item

    def remove(self, id):
        if id in self.__data:
            del self.__data[id]

    def find(self, id):
        if id in self.__data:
            return self.__data[id]

        return None

    def update(self, item):
        if item.getID() in self.__data:
            self.__data[item.getID()] = item
        else:
            raise ValueError("Problema inexistenta")

    def getAll(self):
        return self.__data


def tests():
    d1 = Problema(1, "Titlu", "Descr")

    repo = ProblemaRepo()

    repo.add(d1)
    assert len(repo.getAll()) == 1

    x = repo.find(1)
    assert x.getDescriere() == "Titlu"

    d2 = Problema(1, "Titlu", "Descr")

    try:
        repo.add(d2)
        assert False
    except ValueError:
        assert True

    d3 = Problema(3, "Film 2", "Epic?")

    repo.add(d3)
    assert len(repo.getAll()) == 2

    repo.update(Problema(3, "Film x", "Mai epic"))
    assert repo.find(3).getDescriere() == "Film x"

    repo.remove(3)
    assert len(repo.getAll()) == 1


tests()