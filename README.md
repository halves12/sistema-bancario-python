🏦 Sistema Bancário Otimizado com Python
Este projeto é um simulador de operações bancárias desenvolvido como o segundo desafio do Bootcamp Engenharia de Dados com Python da  em parceria com a NTT DATA.

📝 Descrição do Projeto
Este projeto consiste em um sistema bancário modularizado desenvolvido em Python, focado na aplicação de regras de negócio para gestão de contas e usuários. O sistema foi estruturado para simular o fluxo de um ERP financeiro, garantindo a integridade dos dados e a rastreabilidade das operações.

🚀 Funcionalidades Principais
Cadastro de Usuários: Registro de clientes com CPF único (Chave Primária), nome, data de nascimento e endereço.

Abertura de Contas: Criação de contas correntes vinculadas a um usuário existente, gerando números de conta sequenciais.

Operações Financeiras:

Depósito: Incremento de saldo com registro histórico no extrato.

Saque: Validação tripla (Saldo insuficiente, limite por operação e quantidade máxima de saques diários).

Extrato: Relatório detalhado de todas as movimentações e saldo total formatado.

Listagem de Contas: Consulta estruturada de todas as contas cadastradas (Agência, C/C e Titular).

🛠️ Tecnologias e Conceitos Aplicados
Linguagem: Python 3.x

Modularização: Divisão de responsabilidades entre funções dedicadas (sacar, depositar, criar_usuario).

Argumentos de Função: Implementação de parâmetros positional-only (/) e keyword-only (*) para maior segurança no fluxo de dados.

Estrutura de Dados: Uso de Listas e Dicionários aninhados para simular um banco de dados em memória.

UX/UI Terminal: Uso de textwrap.dedent e limpezas de tela para uma interface mais limpa e intuitiva.

📋 Como Rodar o Projeto
Certifique-se de ter o Python instalado em sua máquina.

Clone este repositório ou baixe o arquivo .py.

No terminal, execute o comando: