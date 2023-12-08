#Este código é uma solução eficiente para processar e converter grandes volumes de dados 
#de um arquivo CSV para o formato Excel. Ele lê as primeiras 500.000 linhas de um dataset 
#sobre fraude, presumivelmente com várias colunas de dados relevantes, e as salva em um novo 
#arquivo XLSX. Esta abordagem facilita a análise posterior dos dados em ferramentas que suportam o formato Excel, 
#permitindo uma manipulação mais conveniente dos dados para inspeções, relatórios ou análises mais detalhadas. 
#É particularmente útil em cenários onde a análise de grandes conjuntos de dados é necessária, mas a capacidade 
#de processamento é limitada.

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
