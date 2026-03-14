from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, _saldo, __senha, limite_cheque_especial):
        super().__init__(_saldo, __senha)
        self.limite_cheque_especial = limite_cheque_especial

    def tentar_acessar_dados(self):
        print("--- Tentativa de Acesso na Subclasse ---")
        
        # 1. Tentando acessar o atributo PROTEGIDO
        print("Acessando _saldo:")
        print(f"Sucesso! O saldo é R$ {self._saldo}")

        # 2. Tentando acessar o atributo PRIVADO
        print("\nAcessando __senha:")
        try:
            # Isso gera um erro
            print(f"A senha é: {self.__senha}")
        except AttributeError as erro:
            print(f"Falha! O Python bloqueou o acesso. Mensagem original: {erro}")