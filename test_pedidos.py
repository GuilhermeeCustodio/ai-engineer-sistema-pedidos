
import pytest

from main import (
    calcular_subtotal,
    calcular_desconto,
    calcular_frete,
    calcular_total_carrinho,
    calcular_pedido,
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
    cliente = {"nome": "Guilherme", "cliente_vip": True}

    carrinho = [
        {"nome": "Notebook", "preco": 2500, "quantidade": 1}
    ]

    pedido = calcular_pedido(carrinho, cliente)

    assert pedido["valor_final"] == 2125


def test_preco_negativo():
    cliente = {"nome": "Guilherme", "cliente_vip": False}

    carrinho = [
        {"nome": "Mouse", "preco": -10, "quantidade": 1}
    ]

    with pytest.raises(ValueError):
        calcular_pedido(carrinho, cliente)


def test_quantidade_zero():
    cliente = {"nome": "Guilherme", "cliente_vip": False}

    carrinho = [
        {"nome": "Mouse", "preco": 80, "quantidade": 0}
    ]

    with pytest.raises(ValueError):
        calcular_pedido(carrinho, cliente)
