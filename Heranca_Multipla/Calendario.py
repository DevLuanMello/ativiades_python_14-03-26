class Calendario:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def exibir_data(self):
        return f"{self.dia}/{self.mes}/{self.ano}"