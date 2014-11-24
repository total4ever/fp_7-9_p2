class Problema():
    def __init__(self, problemaID, descriere, deadline):
        self.__filmID = problemaID
        self.__deadline = deadline
        self.__descriere = descriere

    def getID(self):
        return self.__filmID

    def getDeadline(self):
        return self.__deadline

    def getDescriere(self):
        return self.__descriere

    def __eq__(self, other):
        if other == None:
            return False

        return self.getID() == other.getID()

def tests():
    d1 = Problema("1_1", "greu", "today")

    assert d1.getID() == "1_1"
    assert d1.getDeadline() == "today"
    assert d1.getDescriere() == "greu"


tests()

