# 🏦 Sistema Bancário com Programação Orientada a Objetos (POO)

Este projeto é a evolução do simulador de operações bancárias, desenvolvido para o desafio de modelagem de sistemas do Bootcamp Engenharia de Dados com Python da **DIO** em parceria com a **NTT DATA**.

## 📝 Descrição do Projeto
O sistema foi refatorado para aplicar os pilares da **Programação Orientada a Objetos (POO)**. O objetivo foi transformar a lógica anterior (procedural) em uma arquitetura robusta, onde cada entidade (Cliente, Conta, Transação) é representada por uma classe, simulando a estrutura real de um sistema de gestão financeira.

## 🚀 Funcionalidades e Arquitetura
O projeto agora utiliza uma estrutura de classes baseada no diagrama UML oficial do desafio:

- **Modelagem de Clientes:** Classe base `Cliente` e especialização `PessoaFisica`.
- **Gestão de Contas:** Classe `Conta` com especialização `ContaCorrente`, permitindo limites de saque e quantidade de operações.
- **Histórico e Transações:** Implementação de uma classe `Historico` e uma interface `Transacao` (utilizando `ABC` - Abstract Base Classes) para padronizar `Saque` e `Deposito`.
- **Operações Financeiras:** Validações de negócio encapsuladas dentro dos métodos das classes, garantindo maior segurança.

## 🛠️ Tecnologias e Conceitos de POO Aplicados
- **Linguagem:** Python 3.x
- **Encapsulamento:** Uso de propriedades (`@property`) para proteger atributos como saldo e histórico.
- **Herança:** Reuso de código entre classes pai e filho.
- **Polimorfismo:** Implementação do método `registrar` que se comporta de forma diferente para Saques e Depósitos.
- **Abstração:** Uso de métodos abstratos para definir contratos obrigatórios.

## 📁 Estrutura de Arquivos
- `sistema_bancario_poo.py`: Versão atualizada com toda a lógica de Objetos.
- `sistema_bancario.py`: Versão legível (procedural) para histórico de evolução.

## 📋 Como Rodar o Projeto
1. Certifique-se de ter o Python 3.x instalado.
2. No terminal, execute:
   ```bash
   python sistema_bancario_poo.py