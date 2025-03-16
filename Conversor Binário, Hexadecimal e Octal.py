# Função para converter número
def converter():
    numero = int(input("Digite um número inteiro: "))
    print(f"Binário: {bin(numero)[2:]}")
    print(f"Hexadecimal: {hex(numero)[2:].upper()}")
    print(f"Octal: {oct(numero)[2:]}")

converter()
