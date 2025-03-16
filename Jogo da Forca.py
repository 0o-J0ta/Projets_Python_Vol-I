import random

# Lista de palavras
palavras = ["python", "computador", "desenvolvimento", "jogo"]

# Escolhe uma palavra aleatória
palavra_secreta = random.choice(palavras)
letras_certas = ["_"] * len(palavra_secreta)
tentativas = 6

print("Bem-vindo ao Jogo da Forca!")

# Loop do jogo
while tentativas > 0 and "_" in letras_certas:
    print("Palavra:", " ".join(letras_certas))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_secreta:
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                letras_certas[i] = letra
    else:
        tentativas -= 1
        print(f"Errou! Tentativas restantes: {tentativas}")

if "_" not in letras_certas:
    print(f"Parabéns! Você acertou a palavra: {palavra_secreta}")
else:
    print(f"Você perdeu! A palavra era: {palavra_secreta}")
