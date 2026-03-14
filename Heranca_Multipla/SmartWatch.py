from Relogio import Relogio
from Calendario import Calendario

class SmartWatch(Relogio, Calendario):
    def __init__(self, hora, minuto, segundo, dia, mes, ano, bateria, bluetooth_conectado):
        Relogio.__init__(self, hora, minuto, segundo)
        Calendario.__init__(self, dia, mes, ano)
        self.bateria = bateria
        self.bluetooth_conectado = bluetooth_conectado

    def conectar_smartphone(self):
        self.bluetooth_conectado = True
        return f"Bluetooth conectado com sucesso!"
    
    def mostrar_tela_inicial(self):
        return f"Hoje é {self.exibir_data()} e são exatamente {self.exibir_hora()}\nBluetooth está conectado?: {self.bluetooth_conectado}\nBateria: {self.bateria}"