from Funcionario import Funcionario
from Desenvolvedor import Desenvolvedor

funcionario = Funcionario("Carlos", 34)
desenvolvedor = Desenvolvedor("Luan", 20, "Python")

print("--- Apresentando Funcionário ---")
print(funcionario.apresentar())
print(f"\n{funcionario.trabalhar()}")

print("\n--- Apresentando Desenvolvedor ---")
print(desenvolvedor.apresentar())
print(f"\n{desenvolvedor.trabalhar()}\n")