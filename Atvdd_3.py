valor = float(input("Digite o valor do produto: R$ "))

valor_imposto = valor * 0.08
valor_final = valor + valor_imposto

print("O valor do imposto é: R$", valor_imposto)
print("O valor final do produto é: R$", valor_final)