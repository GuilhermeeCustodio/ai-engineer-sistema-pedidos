
# SISTEMA DE PEDIDOS V4
# Aula 5 - Estruturas de repetição e coleções

import math


# 1. Exibir o menu
def exibir_menu():
    print("\n==== SISTEMA DE PEDIDOS V4 ====")
    print("1. Adicionar produto ao carrinho")
    print("2. Listar produtos no carrinho")
    print("3. Remover produto")
    print("4. Finalizar pedido")
    print("5. Sair")


# 2. Calcular subtotal de um produto
def calcular_subtotal(preco, quantidade):
    return preco * quantidade


# 3. Validar os produtos
def validar_produtos(carrinho):
    for produto in carrinho:
        if (
            not math.isfinite(produto["preco"])
            or produto["preco"] < 0
        ):
            raise ValueError(
                f"Preço inválido para o produto {produto['nome']}"
            )

        if produto["quantidade"] <= 0:
            raise ValueError(
                f"Quantidade inválida para o produto {produto['nome']}"
            )


# 4. Adicionar produto ao carrinho
def adicionar_produto(carrinho):
    nome = input("Digite o nome do produto: ").strip()

    if not nome:
        print("O nome do produto não pode ficar vazio.")
        return

    try:
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Digite um preço e uma quantidade válidos.")
        return

    if not math.isfinite(preco) or preco < 0 or quantidade <= 0:
        print("Preço ou quantidade inválidos.")
        return

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    carrinho.append(produto)
    print("Produto adicionado ao carrinho com sucesso!")


# 5. Listar produtos no carrinho
def listar_produtos(carrinho):
    if not carrinho:
        print("Carrinho vazio!")
        return

    print("\n--- PRODUTOS NO CARRINHO ---")

    for indice, produto in enumerate(carrinho, start=1):
        subtotal = calcular_subtotal(
            produto["preco"],
            produto["quantidade"]
        )

        print(
            f"{indice}. {produto['nome']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Quantidade: {produto['quantidade']} | "
            f"Subtotal: R$ {subtotal:.2f}"
        )


# 6. Remover produto do carrinho
def remover_produto(carrinho):
    if not carrinho:
        print("Carrinho vazio!")
        return

    listar_produtos(carrinho)

    try:
        numero = int(
            input("Digite o número do produto para remover: ")
        )
    except ValueError:
        print("Digite um número válido.")
        return

    if 1 <= numero <= len(carrinho):
        produto_removido = carrinho.pop(numero - 1)

        print(
            f"Produto '{produto_removido['nome']}' "
            f"removido com sucesso!"
        )
    else:
        print("Número inválido!")


# 7. Calcular total original do carrinho
def calcular_total_carrinho(carrinho):
    total = 0

    for produto in carrinho:
        subtotal = calcular_subtotal(
            produto["preco"],
            produto["quantidade"]
        )
        total += subtotal

    return total


# 8. Calcular percentual de desconto
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


# 9. Calcular frete
def calcular_frete(total_com_desconto):
    if total_com_desconto < 150:
        return 20.00

    return 0.00


# 10. Calcular pedido completo
def calcular_pedido(carrinho, cliente):
    if not carrinho:
        raise ValueError(
            "Não é possível finalizar um carrinho vazio."
        )

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


# 11. Exibir resumo do pedido
def exibir_resumo(cliente, carrinho, pedido):
    print("\n===== RESUMO DO PEDIDO =====")
    print(f"Cliente: {cliente['nome']}")
    print(
        f"Cliente VIP: "
        f"{'Sim' if cliente['cliente_vip'] else 'Não'}"
    )

    listar_produtos(carrinho)

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


# 12. Função principal
def main():
    carrinho = []

    print("Bem-vindo ao Sistema de Pedidos V4!")

    nome = input("Digite seu nome: ").strip()

    while not nome:
        print("O nome não pode ficar vazio.")
        nome = input("Digite seu nome: ").strip()

    while True:
        resposta = input(
            "É cliente VIP? (s/n): "
        ).strip().lower()

        if resposta in ("s", "n"):
            break

        print("Responda apenas 's' ou 'n'.")

    cliente = {
        "nome": nome,
        "cliente_vip": resposta == "s"
    }

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_produto(carrinho)

        elif opcao == "2":
            listar_produtos(carrinho)

        elif opcao == "3":
            remover_produto(carrinho)

        elif opcao == "4":
            if not carrinho:
                print(
                    "Não é possível finalizar "
                    "um carrinho vazio."
                )
                continue

            pedido = calcular_pedido(carrinho, cliente)
            exibir_resumo(cliente, carrinho, pedido)

            print("\nPedido finalizado com sucesso!")
            break

        elif opcao == "5":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


# 13. Iniciar o programa
if __name__ == "__main__":
    main()
