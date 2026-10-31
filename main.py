
# Sistema de Análise de Pedidos - V2

# 1. Dados do cliente
nome = input("Digite seu nome: ")
cliente_vip = input("O cliente é VIP? (s/n): ").strip().lower() == "s"

# 2. Carrinho de compras
carrinho = [
    {
        "nome": "Notebook",
        "preco": 2500.00,
        "quantidade": 1
    },
    {
        "nome": "Mouse",
        "preco": 80.00,
        "quantidade": 2
    },
    {
        "nome": "Teclado",
        "preco": 150.00,
        "quantidade": 1
    },
    {
        "nome": "Monitor",
        "preco": 700.00,
        "quantidade": 1
    }
]

# 3. Validar os produtos
for produto in carrinho:
    if produto["preco"] < 0:
        raise ValueError(
            f"Preço inválido para o produto {produto['nome']}"
        )

    if produto["quantidade"] <= 0:
        raise ValueError(
            f"Quantidade inválida para o produto {produto['nome']}"
        )

# 4. Calcular o total do carrinho
total = 0

print("\n--- PRODUTOS DO PEDIDO ---")

for produto in carrinho:
    subtotal = produto["preco"] * produto["quantidade"]
    total += subtotal

    print(
        f"Produto: {produto['nome']} | "
        f"Preço: R$ {produto['preco']:.2f} | "
        f"Quantidade: {produto['quantidade']} | "
        f"Subtotal: R$ {subtotal:.2f}"
    )

# 5. Calcular o desconto normal
if total >= 200:
    desconto = 0.10
elif total >= 100:
    desconto = 0.05
else:
    desconto = 0

# 6. Aplicar desconto adicional VIP
if cliente_vip:
    desconto += 0.05

# 7. Calcular o valor com desconto
valor_desconto = total * desconto
total_com_desconto = total - valor_desconto

# 8. Calcular o frete
if total_com_desconto < 150:
    frete = 20
else:
    frete = 0

# 9. Calcular o valor final
valor_final = total_com_desconto + frete

# 10. Exibir resumo do pedido
print("\n--- RESUMO DO PEDIDO ---")
print(f"Cliente: {nome}")
print(f"Cliente VIP: {'Sim' if cliente_vip else 'Não'}")
print(f"Total original: R$ {total:.2f}")
print(f"Percentual de desconto: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Total com desconto: R$ {total_com_desconto:.2f}")
print(f"Frete: R$ {frete:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")