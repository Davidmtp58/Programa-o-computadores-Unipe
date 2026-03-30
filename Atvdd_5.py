peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura ** 2)

print(f"O IMC é: {imc:.2f}")