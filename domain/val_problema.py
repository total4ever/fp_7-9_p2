from domain.problema import Problema


class ProblemaValidator():
    def validate(self, disc):
        errors = []

        if disc.getID() == "":
            errors.append("ID invalid")

        if disc.getDeadline() == "":
            errors.append("Nume vid")

        if disc.getDescriere() == "":
            errors.append("Descriere vida")

        if errors != []:
            raise ValueError(errors)

def tests():
    d1 = Problema("", "Titlu", "Descr")

    val = ProblemaValidator()

    try:
        val.validate(d1)
        assert False
    except ValueError:
        assert True

    d2 = Problema("14_2", "", "Descr")
    try:
        val.validate(d2)
        assert False
    except ValueError:
        assert True

    d3 = Problema("123", "Nume", "")
    try:
        val.validate(d3)
        assert False
    except ValueError:
        assert True

tests()