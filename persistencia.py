
import csv
import json
from pathlib import Path


PASTA_DADOS = Path(__file__).resolve().parent / "data"

ARQUIVO_JSON = PASTA_DADOS / "pedidos.json"
ARQUIVO_CSV = PASTA_DADOS / "pedidos.csv"


def carregar_pedidos(caminho=ARQUIVO_JSON):
    caminho = Path(caminho)

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            pedidos = json.load(arquivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError as erro:
        raise ValueError(
            "O arquivo de pedidos possui JSON invalido."
        ) from erro

    if not isinstance(pedidos, list):
        raise ValueError(
            "O historico deve conter uma lista de pedidos."
        )

    return pedidos


def salvar_pedido(pedido, caminho=ARQUIVO_JSON):
    caminho = Path(caminho)

    pedidos = carregar_pedidos(caminho)
    pedidos.append(pedido)

    caminho.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            pedidos,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

    return len(pedidos)


def exibir_historico(caminho=ARQUIVO_JSON):
    pedidos = carregar_pedidos(caminho)

    if not pedidos:
        print("Nenhum pedido encontrado.")
        return

    print("\n===== HISTORICO DE PEDIDOS =====")

    for numero, pedido in enumerate(pedidos, start=1):
        cliente = pedido["cliente"]
        resumo = pedido["resumo"]

        print(
            f"{numero}. Cliente: {cliente['nome']} | "
            f"Total: R$ {resumo['valor_final']:.2f}"
        )


def exportar_pedidos_csv(
    caminho_json=ARQUIVO_JSON,
    caminho_csv=ARQUIVO_CSV
):
    pedidos = carregar_pedidos(caminho_json)

    if not pedidos:
        print("Nenhum pedido disponivel para exportacao.")
        return 0

    caminho_csv = Path(caminho_csv)
    caminho_csv.parent.mkdir(parents=True, exist_ok=True)

    colunas = [
        "pedido",
        "cliente",
        "vip",
        "produto",
        "preco_unitario",
        "quantidade",
        "subtotal",
        "valor_final_pedido"
    ]

    with open(
        caminho_csv,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=colunas,
            delimiter=";"
        )

        escritor.writeheader()

        quantidade_linhas = 0

        for numero, pedido in enumerate(pedidos, start=1):
            cliente = pedido["cliente"]
            resumo = pedido["resumo"]

            for produto in pedido["produtos"]:
                escritor.writerow({
                    "pedido": numero,
                    "cliente": cliente["nome"],
                    "vip": cliente["cliente_vip"],
                    "produto": produto["nome"],
                    "preco_unitario": produto["preco"],
                    "quantidade": produto["quantidade"],
                    "subtotal": (
                        produto["preco"] * produto["quantidade"]
                    ),
                    "valor_final_pedido": resumo["valor_final"]
                })

                quantidade_linhas += 1

    return quantidade_linhas
