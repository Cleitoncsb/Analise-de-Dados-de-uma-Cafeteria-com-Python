import pandas as pd
import plotly.express as px
import streamlit as st

#Garantindo que sera usado 100% do espaço disponível para margens
st.set_page_config(layout="wide")

#carregar os dados do excel
df = pd.read_excel('/Users/user/Downloads/Coffee_Shop_Sales.xlsx')

# Convertendo a coluna de data
df['Data_Convertida'] = pd.to_datetime(df['transaction_date'])
df=df.sort_values('Data_Convertida')
df['Data_Convertida'] = pd.to_datetime(df['transaction_date'])
df["Month"] = df['Data_Convertida'].apply(lambda x: f"{x.year}-{x.month}")
unique_months = ['Todos'] + sorted(df["Month"].unique().tolist())
month = st.sidebar.selectbox("Mês", unique_months)
if month == 'Todos':
    df_filtered = df
else:
    df_filtered = df[df['Month'] == month]
st.write(df_filtered)

#Dividindo o espaço dos gráficos
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

#Tendência de Vendas por mês
monthly_sum = df_filtered.groupby('Month')['unit_price'].sum().reset_index()
fig_fat = px.line(monthly_sum, x="Month", y="unit_price", title="Evolução do faturamento")
col1.plotly_chart(fig_fat, use_container_width=True)

#Faturamento por dia da semana
df_sum = df_filtered.groupby("dia_semana")["unit_price"].sum().reset_index()
df_sum_sorted = df_sum.sort_values(by="unit_price", ascending=False)
fig_dia = px.bar(df_sum_sorted, x="dia_semana", y="unit_price", title="Faturamento por dia da semana")
col2.plotly_chart(fig_dia, use_container_width=True)

# Tendência de Vendas por Filial
fig_filial = px.pie(df_filtered, values="unit_price", names="store_location", title="Faturamento por Filial")
col3.plotly_chart(fig_filial,use_container_width=True)

#Tendência de Vendas por produto
df_agg_sorted = df_filtered.groupby('product_type')['unit_price'].sum().reset_index().sort_values(by='unit_price', ascending=False)
fig_vendas = px.bar(df_agg_sorted, x="product_type", y="unit_price", title="Faturamento por Produto")
col4.plotly_chart(fig_vendas, use_container_width=True)

#Tendência de Vendas por produto
df_agg_sorted = df_filtered.groupby('product_type')['transaction_qty'].sum().reset_index().sort_values(by='transaction_qty', ascending=False)
fig_vendas = px.bar(df_agg_sorted, x="product_type", y="transaction_qty", title="Quantidade de Vendas por Produto")
col5.plotly_chart(fig_vendas, use_container_width=True)
