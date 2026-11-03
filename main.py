
# SISTEMA DE PEDIDOS V3
# Aula 4 - Funções e Modularização


# 1. Calcular subtotal de um produto
def calcular_subtotal(preco, quantidade):
    return preco * quantidade


# 2. Calcular percentual de desconto
def calcular_desconto(total, cliente_vip):
    if total >= 200:
        desconto = 0.10
    elif total >= 100:
        desconto = 0.05
    else:
        desconto = 0.00

    if cliente_vip:
        desconto += 0.05

    return desconto


# 3. Calcular frete
def calcular_frete(total_com_desconto):
    if total_com_desconto < 150:
        return 20.00
    else:
        return 0.00


# 4. Validar os produtos
def validar_produtos(carrinho):
    for produto in carrinho:
        if produto["preco"] < 0:
            raise ValueError(
                f"Preço inválido para o produto {produto['nome']}"
            )

        if produto["quantidade"] <= 0:
            raise ValueError(
                f"Quantidade inválida para o produto {produto['nome']}"
            )


# 5. Calcular total original do carrinho
def calcular_total_carrinho(carrinho):
    total = 0

    for produto in carrinho:
        subtotal = calcular_subtotal(
            produto["preco"],
            produto["quantidade"]
        )
        total += subtotal

    return total


# 6. Calcular pedido completo
def calcular_pedido(carrinho, cliente):
    validar_produtos(carrinho)

    total = calcular_total_carrinho(carrinho)

    percentual_desconto = calcular_desconto(
        total,
        cliente["cliente_vip"]
    )

    valor_desconto = total * percentual_desconto
    total_com_desconto = total - valor_desconto

    frete = calcular_frete(total_com_desconto)
    valor_final = total_com_desconto + frete

    return {
        "total": total,
        "percentual_desconto": percentual_desconto,
        "valor_desconto": valor_desconto,
        "total_com_desconto": total_com_desconto,
        "frete": frete,
        "valor_final": valor_final
    }


# 7. Exibir resumo do pedido
def exibir_resumo(cliente, carrinho, pedido):
    print("\n--- RESUMO DO PEDIDO ---")
    print(f"Cliente: {cliente['nome']}")
    print(
        f"Cliente VIP: "
        f"{'Sim' if cliente['cliente_vip'] else 'Não'}"
    )

    print("\n--- PRODUTOS ---")

    for produto in carrinho:
        subtotal = calcular_subtotal(
            produto["preco"],
            produto["quantidade"]
        )

        print(
            f"{produto['nome']} | "
            f"Quantidade: {produto['quantidade']} | "
            f"Subtotal: R$ {subtotal:.2f}"
        )

    print("\n--- VALORES ---")
    print(f"Total original: R$ {pedido['total']:.2f}")
    print(
        f"Desconto: "
        f"{pedido['percentual_desconto'] * 100:.0f}%"
    )
    print(
        f"Valor descontado: "
        f"R$ {pedido['valor_desconto']:.2f}"
    )
    print(
        f"Total com desconto: "
        f"R$ {pedido['total_com_desconto']:.2f}"
    )
    print(f"Frete: R$ {pedido['frete']:.2f}")
    print(f"Valor final: R$ {pedido['valor_final']:.2f}")


# 8. Função principal
def main():
    cliente = {
        "nome": "Guilherme",
        "cliente_vip": True
    }

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

    pedido = calcular_pedido(carrinho, cliente)

    exibir_resumo(cliente, carrinho, pedido)


# 9. Executar apenas quando o arquivo for iniciado diretamente
if __name__ == "__main__":
    main()
