import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Função para gerar um QR Code e salvar como imagem
def gerar_qrcode(dados, nome_arquivo="meu_qrcode.png"):
    caminho = r"C:\Users\User\OneDrive\Documentos\python\Projetos do J0ta" + "\\" + nome_arquivo  
    qr = qrcode.make(dados)
    qr.save(caminho)
    print(f"QR Code salvo em {caminho}")

# Função para decodificar QR Code a partir de uma imagem
def decodificar_qrcode(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    dados = decode(imagem)
    if dados:
        for item in dados:
            print("Conteúdo do QR Code:", item.data.decode())  # Decodifica e exibe o conteúdo
    else:
        print("Nenhum QR Code encontrado na imagem.")

# Teste: gerando e decodificando um QR Code
texto = input("Digite o texto ou link para o QR Code: ")
gerar_qrcode(texto)  # Gera um QR Code com o texto informado
decodificar_qrcode("qrcode.png")  # Decodifica o QR Code salvo
