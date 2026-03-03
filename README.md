# Sistema Bancário em Python 🏦

Este projeto é um simulador de operações bancárias desenvolvido como o primeiro desafio do **Bootcamp Engenharia de Dados com Python** da [DIO](https://www.dio.me/) em parceria com a **NTT DATA**.

## 💻 Sobre o Desafio
O objetivo foi criar um sistema interativo que permitisse a um usuário realizar operações básicas do dia a dia bancário, aplicando regras de negócio e validações de fluxo.

### Operações Implementadas:
- **Depósito:** Permite adicionar valores positivos ao saldo.
- **Saque:** - Limite de 3 saques diários.
  - Valor máximo de R$ 500,00 por transação.
  - Verificação de saldo disponível.
- **Extrato:** Lista todas as movimentações e exibe o saldo atual formatado.

## 🛠️ Tecnologias e Conceitos Utilizados
- **Linguagem:** Python 3.x
- **Lógica de Programação:** Estruturas de repetição (`while`), condicionais (`if/elif/else`) e operadores lógicos.
- **Formatação de Dados:** Uso de f-strings para exibição de valores monetários.
- **UX/UI Terminal:** Implementação de feedbacks de sucesso/erro e pausas de tela para melhor leitura.

## 🚀 Como executar
1. Certifique-se de ter o Python instalado.
2. Clone o repositório ou baixe o arquivo `sistema_bancario.py`.
3. Execute o comando:
   ```bash
   python sistema_bancario.py

   ## 🆕 Novidades desta Versão
- **Confirmação de Transação:** Implementada uma camada de segurança que pergunta ao usuário se ele deseja confirmar o depósito ou saque (`s/n`), evitando erros acidentais.
- **Melhoria Visual:** Menu formatado com tabulações (`\t`) para melhor alinhamento no terminal.
- **Correção de Fluxo:** Ajuste na lógica de exibição do extrato para garantir a leitura antes de retornar ao menu.