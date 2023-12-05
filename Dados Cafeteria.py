echo "# meu-projeto" >> README.md
  git init
  git add README.md
  git commit -m "primeiro commit"
  ramo git -M principal
  origem de adição remota git https://github.com/Cleitoncsb/meu-projeto.git
  git push -u origem principal

import pandas as pd
import matplotlib.pyplot as plt

#carregar os dados do excel
df = pd.read_excel('/Users/user/Downloads/Coffee_Shop_Sales.xlsx')

# Convertendo a coluna de data
df['Data_Convertida'] = pd.to_datetime(df['transaction_date'])

# Análise de Vendas por Dia da Semana
df['Dia_da_Semana'] = df['Data_Convertida'].dt.day_name()
df.groupby('Dia_da_Semana').size().sort_values(ascending=False).plot(kind='bar')
plt.show()

#Tendência de Vendas por mês
df.groupby(df['transaction_date'].dt.to_period("M")).size().plot(kind='line')
plt.show()

#Quais produtos são vendidos com mais e menos frequência?
df.groupby('product_type').size().sort_values(ascending=False).plot(kind='bar')
plt.show()

#Qual gera mais receita para o negócio?
df.groupby('product_type')['unit_price'].sum().sort_values(ascending=False).plot(kind='bar')
plt.show()

#ticket médio por produto
soma_transaction_id = df['transaction_id'].size
soma_unit_price = df['unit_price'].sum()
resultado = soma_unit_price / soma_transaction_id
df_plot = pd.DataFrame({'Resultado': [resultado]})

df_plot.plot(kind='bar')
plt.show()