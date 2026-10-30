# Sistema de Análise de Pedidos

Projeto desenvolvido durante minha formação em Engenharia de Inteligência Artificial (AI Engineer).

## Objetivo

Desenvolver um sistema em Python capaz de calcular o valor de pedidos, aplicar descontos e determinar o valor do frete.

## Funcionalidades

- Cadastro do nome do cliente
- Cálculo do valor total do pedido
- Descontos progressivos de 0%, 5% e 10%
- Desconto adicional de 5 pontos percentuais para clientes VIP
- Frete grátis para pedidos de R$ 150 ou mais após descontos
- Validação de preços e quantidades

## Tecnologias

- Python
- Git
- GitHub

## Como executar

Instale Python 3 e execute:

```bash
python main.py
```

## Regras de negócio

| Valor original do pedido | Desconto |
|---|---|
| Abaixo de R$ 100 | 0% |
| R$ 100 até menos de R$ 200 | 5% |
| R$ 200 ou mais | 10% |

Clientes VIP recebem 5 pontos percentuais adicionais.

O frete custa R$ 20 quando o valor após descontos é inferior a R$ 150. Caso contrário, é gratuito.

## Aprendizados

- Variáveis e tipos de dados
- Operadores matemáticos e lógicos
- Condicionais
- Conversão de dados
- Validação com ValueError
- Git e GitHub.
