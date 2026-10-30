# Sistema de Análise de pedidos

nome = input("Digite seu nome: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
cliente_vip = input("O cliente é VIP? (s/n): ").lower() == 's'



# Validar se o preço e a quantidade são válidos
if preco < 0 or quantidade <= 0:
    raise ValueError("Erro: Preço ou quantidade não podem ser negativos.")

total = preco * quantidade



# primeirao calcular o desconto normal
if total >= 200:
    desconto = 0.10

elif total >= 100:
    desconto = 0.05

else:
    desconto = 0

# Segundo: verificar se o cliente é VIP e aplicar desconto adicional

if cliente_vip:
    desconto += 0.05



#1. Calcular o valor do desconto
valor_desconto = total * desconto

#2. Calcular o total após desconto
total_com_desconto = total - valor_desconto

#3. Verificar o frete
if total_com_desconto < 150:
    frete = 20
else:
    frete = 0

#4. Calcular o valor final do pedido
valor_final = total_com_desconto + frete




print("\n--- RESUMO DO PEDIDO ---")
print(f"Cliente: {nome}")
print(f"Valor original: R$ {total:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Frete: R$ {frete:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")