# Função para calcular a média das provas
def calcular_media():
    # Solicita o número de provas
    num_provas = int(input("Quantas provas você tem? "))
    
    # Inicializa uma variável para somar as notas
    soma_notas = 0
    
    # Solicita a nota de cada prova
    for i in range(num_provas):
        nota = float(input(f"Digite a nota da prova {i + 1}: "))
        soma_notas += nota  # Adiciona a nota à soma total
    
    # Calcula a média
    media = soma_notas / num_provas
    print(f"A média das suas provas é: {media:.2f}")

# Chama a função para calcular a média
calcular_media()
