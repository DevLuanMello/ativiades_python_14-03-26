# 🐍 Exercícios de POO em Python: Herança

Este repositório contém as implementações das atividades práticas sobre **Herança em Programação Orientada a Objetos (POO)** em Python. Os exercícios foram propostos na disciplina de 4-ADS/ESW, ministrada pelo Prof. Juliano O. Lima.

## 🎯 Objetivo do Repositório
Colocar em prática os conceitos fundamentais da Orientação a Objetos, focando na reutilização de código, organização de hierarquias e proteção de dados em Python.

## 📚 Conceitos Abordados
Durante a resolução destas atividades, foram aplicados os seguintes conceitos:
* **Herança Simples e Múltipla:** Criação de Subclasses e Superclasses.
* **Método `super()`:** Inicialização e reaproveitamento de atributos da classe pai.
* **Sobrescrita de Métodos (Overriding):** Redefinição de comportamentos em subclasses.
* **Encapsulamento:** Uso de atributos Protegidos (`_`) e Privados (`__`).
* **Polimorfismo:** Adaptação de métodos herdados para contextos específicos.
* **Validação de Tipos:** Utilização de `isinstance()` e `issubclass()`.

---

## 🚀 Lista de Atividades Implementadas

### 1. Implementação de Herança Simples
* Criação da superclasse `Pessoa` com os atributos `nome` e `idade`.
* Criação da subclasse `Aluno`, que herda de `Pessoa` e adiciona o atributo `matricula`.
* Uso do método `super()` para inicializar a classe base.

### 2. Sobrescrita de Métodos (Overriding)
* Criação da classe `Funcionario` com o método genérico `trabalhar()`.
* Criação da subclasse `Desenvolvedor` que sobrescreve o método `trabalhar()` para exibir a rotina de escrita de código.

### 3. Atributos Protegidos e Privados
* Estruturação da classe `ContaBancaria` contendo o atributo protegido `_saldo` e o atributo privado `__senha`.
* Criação da subclasse `ContaCorrente` demonstrando o acesso e a proteção do encapsulamento na prática.

### 4. Verificação de Instância
* Utilização das funções nativas `isinstance()` e `issubclass()`.
* Validação para confirmar instâncias e heranças entre as classes criadas.

### 5. Herança Múltipla
* Criação do sistema de um dispositivo inteligente unindo as classes `Relogio` e `Calendario`.
* Implementação da classe `SmartWatch` herdando comportamentos de ambas as superclasses simultaneamente e executando seus métodos em conjunto.

---
