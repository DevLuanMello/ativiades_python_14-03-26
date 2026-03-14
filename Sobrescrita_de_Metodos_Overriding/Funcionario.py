class Funcionario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Trabalhador: {self.nome}, {self.idade} anos."

    def trabalhar(self):
        return f"Realizando tarefas gerais..."