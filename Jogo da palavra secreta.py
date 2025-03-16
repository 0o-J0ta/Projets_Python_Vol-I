import random

# Função para jogar o jogo da palavra secreta
def jogo_palavra_secreta():
    palavras = ["python", "programacao", "desenvolvimento", "algoritmo"]
    palavra_secreta = random.choice(palavras)
    tentativas = 6
    letras_descobertas = ["_"] * len(palavra_secreta)
    
    print("Bem-vindo ao Jogo da Palavra Secreta!")
    
    # Loop até o usuário acertar ou as tentativas acabarem
    while tentativas > 0 and "_" in letras_descobertas:
        print("Palavra:", " ".join(letras_descobertas))
        palpite = input(f"Tentativas restantes: {tentativas}. Digite uma letra: ").lower()

        if len(palpite) == 1 and palpite.isalpha():
            if palpite in palavra_secreta:
                print(f"Boa! A letra '{palpite}' está na palavra.")
                for i in range(len(palavra_secreta)):
                    if palavra_secreta[i] == palpite:
                        letras_descobertas[i] = palpite
            else:
                tentativas -= 1
                print(f"A letra '{palpite}' não está na palavra.")
        else:
            print("Entrada inválida! Digite apenas uma letra.")
    
    if "_" not in letras_descobertas:
        print("Parabéns, você acertou a palavra:", palavra_secreta)
    else:
        print(f"Você perdeu! A palavra secreta era: {palavra_secreta}")

# Chama a função para jogar o jogo da palavra secreta
jogo_palavra_secreta()
