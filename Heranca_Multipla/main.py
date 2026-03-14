from Relogio import Relogio
from Calendario import Calendario
from SmartWatch import SmartWatch


smartwatch = SmartWatch(13, 23, 56, 14, 12, 2026, "87%", False)

print(smartwatch.mostrar_tela_inicial())

print("\n")

print(smartwatch.conectar_smartphone())
print(smartwatch.mostrar_tela_inicial())