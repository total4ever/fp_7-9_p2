from controller.prob_ctrl import ProbCtrl
from controller.student_ctrl import StudentCtrl
from controller.nota_ctrl import RentCtrl
from domain.val_problema import ProblemaValidator
from domain.val_nota import NotaValidator
from domain.val_student import StudentValidator
from repository.problema_repo import ProblemaRepo
from repository.nota_repo import NotaRepo
from repository.student_repo import StudentRepo
from ui.console import Console

valStud = StudentValidator()
valProb = ProblemaValidator()
valNota = NotaValidator()

repoStud = StudentRepo()
repoProb = ProblemaRepo()
repoNota = NotaRepo()

ctrlStud = StudentCtrl(valStud, repoStud)
ctrlProb = ProbCtrl(valProb, repoProb)
ctrlNota = RentCtrl(valNota, repoStud, repoProb, repoNota)

console = Console(ctrlStud, ctrlProb, ctrlNota)

console.startUI()
