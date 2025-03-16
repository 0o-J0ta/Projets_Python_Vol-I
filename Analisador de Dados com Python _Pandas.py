import pandas as pd

# Carrega um arquivo CSV
arquivo = input("Digite o caminho do arquivo CSV: ")
df = pd.read_csv(arquivo)

# Exibe informações básicas do arquivo
print(df.head())  # Primeiras linhas
print(df.describe())  # Estatísticas gerais
