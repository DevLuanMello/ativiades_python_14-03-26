class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def exibir_hora(self):
        return f"{self.hora}:{self.minuto}:{self.segundo}"