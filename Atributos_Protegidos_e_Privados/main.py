from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente

minha_conta = ContaCorrente(1500.00, "123456", 500.00)
minha_conta.tentar_acessar_dados()

"""
Consigo acessar o atributo Protegido, pois consigo utilizar ele dentro da classe onde ele foi criado e em suas subclasses.
Já o atributo Privado, eu não consigo ultilizar, pois apenas consigo usar ele dentro da própria classe onde ele foi criado.
Quando atilizamos dois underlines __, o Python aciona um mecanismo de segurança chamado Name Mangling (Desfiguração de Nomes). 
Nos bastidores, ele altera o nome real da variável para esconder o dado.
Por causa dessa mudança de nome invisível, quando a sua subclasse tenta chamar self.__senha, o Python diz que esse atributo simplesmente não existe (gerando o AttributeError), protegendo a senha original de ser lida ou alterada acidentalmente por qualquer outra classe.

"""