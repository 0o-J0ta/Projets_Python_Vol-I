import random
import string

# Função para gerar senha aleatória
def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Pergunta quantas senhas gerar
quantidade = int(input("Quantas senhas você deseja gerar? "))

# Gera e exibe as senhas
for i in range(quantidade):
    print(f"Senha {i + 1}: {gerar_senha()}")
