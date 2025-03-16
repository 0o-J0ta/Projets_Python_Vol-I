# Tabuleiro inicial
tabuleiro = [" "] * 9

# Função para exibir o tabuleiro
def exibir_tabuleiro():
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("-" * 9)
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("-" * 9)
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

# Função para jogar
def jogar():
    jogador = "X"
    for _ in range(9):
        exibir_tabuleiro()
        posicao = int(input(f"Jogador {jogador}, escolha um número (0-8): "))
        if tabuleiro[posicao] == " ":
            tabuleiro[posicao] = jogador
            jogador = "O" if jogador == "X" else "X"
        else:
            print("Posição ocupada! Escolha outra.")
    exibir_tabuleiro()

jogar()
