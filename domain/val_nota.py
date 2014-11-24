class NotaValidator():
    def validate(self, gr):
        errors = []

        if gr.getStudent() == None:
            errors.append("Student invalid")

        if gr.getProb() == None:
            errors.append("Problema invalida")

        if errors != []:
            raise ValueError(errors)

