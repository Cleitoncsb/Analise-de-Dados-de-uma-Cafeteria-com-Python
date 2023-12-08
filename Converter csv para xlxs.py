import pandas as pd

# Carregar as primeiras 1 milhão de linhas do arquivo CSV
arquivo_csv = '/Users/user/Documents/DATABASES/fraudTrain.csv'
n_linhas = 500000  # Número de linhas que você deseja ler
df = pd.read_csv(arquivo_csv, nrows=n_linhas)

# Escolher o nome para o arquivo XLSX de saída
arquivo_xlsx = '/Users/user/Documents/DATABASES/Base_Fraude.xlsx'  # Corrigido a extensão para .xlsx

# Salvar o DataFrame como um arquivo XLSX
df.to_excel(arquivo_xlsx, index=False)

print(f'As primeiras {n_linhas} linhas do arquivo CSV foram convertidas para {arquivo_xlsx}.')


