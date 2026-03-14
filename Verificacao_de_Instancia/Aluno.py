from Pessoa import Pessoa

class Aluno (Pessoa):
    def __init__ (self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar_aluno(self):
        return f"{self.apresentar()}. Minha matrícula na faculdade é {self.matricula}."