
import pytest

from main import (
    calcular_subtotal,
    calcular_desconto,
    calcular_frete,
    calcular_total_carrinho,
    calcular_pedido,
    adicionar_produto,
    remover_produto,
    listar_produtos,
)


def test_subtotal():
    assert calcular_subtotal(150, 3) == 450


def test_desconto_comum():
    assert calcular_desconto(200, False) == 0.10


def test_desconto_vip():
    assert calcular_desconto(200, True) == pytest.approx(0.15)


def test_frete():
    assert calcular_frete(100) == 20
    assert calcular_frete(150) == 0


def test_total_carrinho():
    carrinho = [
        {"nome": "Mouse", "preco": 80, "quantidade": 2},
        {"nome": "Teclado", "preco": 150, "quantidade": 1}
    ]

    assert calcular_total_carrinho(carrinho) == 310


def test_pedido_vip():
    cliente = {"nome": "Teste", "cliente_vip": True}

    carrinho = [
        {"nome": "Notebook", "preco": 2500, "quantidade": 1}
    ]

    pedido = calcular_pedido(carrinho, cliente)

    assert pedido["valor_final"] == pytest.approx(2125)


def test_preco_negativo():
    cliente = {"nome": "Teste", "cliente_vip": False}

    carrinho = [
        {"nome": "Mouse", "preco": -10, "quantidade": 1}
    ]

    with pytest.raises(ValueError):
        calcular_pedido(carrinho, cliente)


def test_quantidade_zero():
    cliente = {"nome": "Teste", "cliente_vip": False}

    carrinho = [
        {"nome": "Mouse", "preco": 80, "quantidade": 0}
    ]

    with pytest.raises(ValueError):
        calcular_pedido(carrinho, cliente)


def test_carrinho_vazio():
    cliente = {"nome": "Teste", "cliente_vip": False}

    with pytest.raises(ValueError):
        calcular_pedido([], cliente)


def test_adicionar_produto(monkeypatch):
    carrinho = []

    entradas = iter(["Mouse", "80", "2"])
    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    adicionar_produto(carrinho)

    assert len(carrinho) == 1
    assert carrinho[0]["nome"] == "Mouse"
    assert carrinho[0]["quantidade"] == 2


def test_remover_produto(monkeypatch):
    carrinho = [
        {"nome": "Notebook", "preco": 2500, "quantidade": 1},
        {"nome": "Mouse", "preco": 80, "quantidade": 2}
    ]

    monkeypatch.setattr("builtins.input", lambda _: "2")

    remover_produto(carrinho)

    assert len(carrinho) == 1
    assert carrinho[0]["nome"] == "Notebook"


def test_listar_carrinho_vazio(capsys):
    listar_produtos([])

    saida = capsys.readouterr().out

    assert "Carrinho vazio!" in saida


def test_adicionar_preco_invalido(monkeypatch):
    carrinho = []

    entradas = iter(["Mouse", "abc", "2"])
    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    adicionar_produto(carrinho)

    assert carrinho == []


def test_remover_numero_invalido(monkeypatch):
    carrinho = [
        {"nome": "Mouse", "preco": 80, "quantidade": 1}
    ]

    monkeypatch.setattr("builtins.input", lambda _: "abc")

    remover_produto(carrinho)

    assert len(carrinho) == 1
