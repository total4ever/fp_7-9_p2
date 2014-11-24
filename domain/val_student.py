from domain.student import Student


class StudentValidator():
    def validate(self, cl):
        errors = []

        if cl.getName() == "":
            errors.append("Nume vid")

        if cl.getID() < 0:
            errors.append("ID invalid")

        if cl.getGrup() == "":
            errors.append("Grup vid")


        if errors != []:
            raise ValueError(errors)


# # TESTS

def tests():
    val = StudentValidator()

    c1 = Student(-1, "Paul", "123")

    try:
        val.validate(c1)
        assert False
    except ValueError:
        assert True

    c2 = Student(1, "", "")

    try:
        val.validate(c2)
        assert False
    except ValueError:
        assert True


tests()