import os
import shutil

# Pastas de destino
pasta_doc = "Documentos"
pasta_outros = "Outros"

# Verifica e cria pastas
os.makedirs(pasta_doc, exist_ok=True)
os.makedirs(pasta_outros, exist_ok=True)

# Move arquivos
for arquivo in os.listdir():
    if arquivo.endswith(".docx"):
        shutil.move(arquivo, pasta_doc)
    else:
        shutil.move(arquivo, pasta_outros)

print("Arquivos organizados!")
