
# SISTEMA DE PEDIDOS V5
# Aula 6 - Tratamento de erros e exceções

import math
from test_persistencia import (
    salvar_pedido,
    exibir_historico,
    exportar_pedidos_csv,
    ARQUIVO_JSON,
)


# 1. Exibir o menu
def exibir_menu():
    print("\n==== SISTEMA DE PEDIDOS V6 ====")
    print("1. Adicionar produto ao carrinho")
    print("2. Listar produtos no carrinho")
    print("3. Remover produto")
    print("4. Finalizar pedido")
    print("5. Consultar historico")
    print("6. Exportar pedidos CSV")
    print("7. Sair")


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


# 4. Ler e validar o preço
def ler_preco():
    while True:
        try:
            preco = float(
                input("Digite o preço do produto: ")
            )

            if not math.isfinite(preco) or preco < 0:
                print(
                    "Preço inválido! Digite um valor "
                    "maior ou igual a zero."
                )
                continue

            return preco

        except ValueError:
            print(
                "Entrada inválida! Digite um número válido."
            )


# 5. Ler e validar a quantidade
def ler_quantidade():
    while True:
        try:
            quantidade = int(
                input("Digite a quantidade desejada: ")
            )

            if quantidade <= 0:
                print(
                    "Quantidade inválida! Digite um "
                    "número maior que zero."
                )
                continue

            return quantidade

        except ValueError:
            print(
                "Quantidade inválida! "
                "Digite um número inteiro."
            )


# 6. Adicionar produto ao carrinho
def adicionar_produto(carrinho):
    nome = input("Digite o nome do produto: ").strip()

    if not nome:
        print("O nome do produto não pode ficar vazio.")
        return

    # Reutilizando as funções da Aula 6
    preco = ler_preco()
    quantidade = ler_quantidade()

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    carrinho.append(produto)

    print("Produto adicionado ao carrinho com sucesso!")


# 7. Listar produtos no carrinho
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


# 8. Remover produto do carrinho
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


# 9. Calcular total original do carrinho
def calcular_total_carrinho(carrinho):
    total = 0

    for produto in carrinho:
        subtotal = calcular_subtotal(
            produto["preco"],
            produto["quantidade"]
        )

        total += subtotal

    return total


# 10. Calcular percentual de desconto
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


# 11. Calcular frete
def calcular_frete(total_com_desconto):
    if total_com_desconto < 150:
        return 20.00

    return 0.00


# 12. Calcular pedido completo
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


# 13. Exibir resumo do pedido
def exibir_resumo(cliente, carrinho, pedido):
    print("\n===== RESUMO DO PEDIDO =====")

    print(f"Cliente: {cliente['nome']}")

    print(
        f"Cliente VIP: "
        f"{'Sim' if cliente['cliente_vip'] else 'Não'}"
    )

    listar_produtos(carrinho)

    print("\n--- VALORES ---")

    print(
        f"Total original: R$ {pedido['total']:.2f}"
    )

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

    print(
        f"Valor final: R$ {pedido['valor_final']:.2f}"
    )


# 14. Função principal

def main():
    carrinho = []

    print("Bem-vindo ao Sistema de Pedidos V6!")

    nome = input("Digite seu nome: ").strip()

    while not nome:
        print("O nome nao pode ficar vazio.")
        nome = input("Digite seu nome: ").strip()

    while True:
        resposta = input(
            "E cliente VIP? (s/n): "
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

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            adicionar_produto(carrinho)

        elif opcao == "2":
            listar_produtos(carrinho)

        elif opcao == "3":
            remover_produto(carrinho)

        elif opcao == "4":
            if not carrinho:
                print(
                    "Nao e possivel finalizar "
                    "um carrinho vazio."
                )
                continue

            try:
                resumo = calcular_pedido(
                    carrinho,
                    cliente
                )

                registro = {
                    "cliente": cliente.copy(),
                    "produtos": [
                        produto.copy()
                        for produto in carrinho
                    ],
                    "resumo": resumo
                }

                numero = salvar_pedido(registro)

            except ValueError as erro:
                print(f"Erro de validacao: {erro}")
                continue

            except OSError as erro:
                print(f"Erro ao salvar o pedido: {erro}")
                continue

            exibir_resumo(
                cliente,
                carrinho,
                resumo
            )

            print(
                f"\nPedido numero {numero} "
                "salvo com sucesso!"
            )

            break

        elif opcao == "5":
            try:
                exibir_historico()

            except (ValueError, OSError) as erro:
                print(f"Erro ao consultar historico: {erro}")

        elif opcao == "6":
            try:
                quantidade = exportar_pedidos_csv()

                if quantidade > 0:
                    print(
                        f"{quantidade} linhas exportadas "
                        "para CSV com sucesso!"
                    )

            except (ValueError, OSError) as erro:
                print(f"Erro ao exportar CSV: {erro}")

        elif opcao == "7":
            print("Saindo do sistema...")
            break

        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
