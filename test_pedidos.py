
import csv
import json

import pytest

from persistencia import (
    carregar_pedidos,
    salvar_pedido,
    exibir_historico,
    exportar_pedidos_csv,
)


@pytest.fixture
def pedido_exemplo():
    return {
        "cliente": {
            "nome": "Guilherme",
            "cliente_vip": True
        },
        "produtos": [
            {
                "nome": "Notebook",
                "preco": 2500,
                "quantidade": 1
            },
            {
                "nome": "Mouse",
                "preco": 80,
                "quantidade": 2
            }
        ],
        "resumo": {
            "total": 2660,
            "percentual_desconto": 0.15,
            "valor_desconto": 399,
            "total_com_desconto": 2261,
            "frete": 0,
            "valor_final": 2261
        }
    }


def test_carregar_arquivo_inexistente(tmp_path):
    caminho = tmp_path / "pedidos.json"

    assert carregar_pedidos(caminho) == []


def test_salvar_pedido(tmp_path, pedido_exemplo):
    caminho = tmp_path / "pedidos.json"

    numero = salvar_pedido(pedido_exemplo, caminho)

    assert numero == 1
    assert caminho.exists()


def test_carregar_pedido_salvo(tmp_path, pedido_exemplo):
    caminho = tmp_path / "pedidos.json"

    salvar_pedido(pedido_exemplo, caminho)

    pedidos = carregar_pedidos(caminho)

    assert len(pedidos) == 1
    assert pedidos[0]["cliente"]["nome"] == "Guilherme"
    assert pedidos[0]["resumo"]["valor_final"] == 2261


def test_salvar_dois_pedidos(tmp_path, pedido_exemplo):
    caminho = tmp_path / "pedidos.json"

    salvar_pedido(pedido_exemplo, caminho)
    salvar_pedido(pedido_exemplo, caminho)

    pedidos = carregar_pedidos(caminho)

    assert len(pedidos) == 2


def test_json_invalido(tmp_path):
    caminho = tmp_path / "pedidos.json"
    caminho.write_text("{invalido", encoding="utf-8")

    with pytest.raises(ValueError):
        carregar_pedidos(caminho)


def test_json_deve_ser_lista(tmp_path):
    caminho = tmp_path / "pedidos.json"

    caminho.write_text(
        json.dumps({"pedido": 1}),
        encoding="utf-8"
    )

    with pytest.raises(ValueError):
        carregar_pedidos(caminho)


def test_historico_vazio(tmp_path, capsys):
    caminho = tmp_path / "pedidos.json"

    exibir_historico(caminho)

    saida = capsys.readouterr().out

    assert "Nenhum pedido encontrado." in saida


def test_exportar_csv(tmp_path, pedido_exemplo):
    caminho_json = tmp_path / "pedidos.json"
    caminho_csv = tmp_path / "pedidos.csv"

    salvar_pedido(pedido_exemplo, caminho_json)

    quantidade = exportar_pedidos_csv(
        caminho_json,
        caminho_csv
    )

    assert quantidade == 2
    assert caminho_csv.exists()

    with open(
        caminho_csv,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as arquivo:
        leitor = csv.DictReader(
            arquivo,
            delimiter=";"
        )
        linhas = list(leitor)

    assert len(linhas) == 2
    assert linhas[0]["produto"] == "Notebook"
    assert linhas[1]["produto"] == "Mouse"


def test_exportar_sem_pedidos(tmp_path):
    caminho_json = tmp_path / "pedidos.json"
    caminho_csv = tmp_path / "pedidos.csv"

    quantidade = exportar_pedidos_csv(
        caminho_json,
        caminho_csv
    )

    assert quantidade == 0
    assert not caminho_csv.exists()
