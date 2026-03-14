from Funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, nome, idade, linguagem):
        super().__init__(nome, idade)
        self.linguagem = linguagem

    def apresentar(self):
        return f"Trabalhador: {self.nome}, {self.idade} anos. Trabalha com {self.linguagem}."
    
    def trabalhar(self):
        return f"Escrevendo código em Python..."