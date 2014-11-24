class Student():
    def __init__(self, clientID, nume, grup):
        self.__clientID = clientID
        self.__nume = nume
        self.__grup = grup

    def getID(self):
        return self.__clientID

    def getName(self):
        return self.__nume

    def getGrup(self):
        return self.__grup

    def __eq__(self, other):
        if other == None:
            return False
        return self.getID() == other.getID()


def tests():
    s1 = Student(1, "Ion", "123")
    s2 = Student(2, "Vasile", "456")
    s3 = Student(1, "Gheroghe", "789")

    assert s1.getID() == 1
    assert s1.getName() == "Ion"
    assert s1.getGrup() == "123"

    assert s1 != s2
    assert s1 == s3

tests()
