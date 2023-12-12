<h1>Análise de Dados de uma Cafeteria com Python </h1>


![Imagem1](https://github.com/Cleitoncsb/meu-Portfolio/assets/142935223/b9bf12f2-c1a3-46af-a8a8-b2fade673657)


 <h2> 📌 Overview   </h2>
 

O objetivo final desse projeto é gerar indicadores e proporcionar insights sobre o desempenho das vendas da cafeteria, permitindo uma análise detalhada por diferentes dimensões (tempo, produto, localização).
Assim usamos como na base (transações, dia da semana, horário das transações, localização, quantidade,tipo de produto,categoria do produto e tipo de produto). 


<h2>Um pouco sobre o setor analisado</h2>

A Arte da Experiência em Cafeterias ☕

No dinâmico mundo das cafeterias, a evolução vai além da simples oferta de uma boa xícara de café. Hoje, o sucesso desses estabelecimentos está intrinsecamente ligado à capacidade de proporcionar experiências únicas e memoráveis aos clientes. O coração de uma cafeteria pulsante é o seu ambiente. O design do espaço, a escolha da música, a iluminação e até a disposição dos assentos são componentes cruciais que contribuem para uma atmosfera convidativa. Esses elementos não são apenas detalhes estéticos; eles criam um refúgio onde os clientes podem desfrutar de momentos de tranquilidade ou encontros sociais.

<h2> ⚙️ Análise de Vendas de Cafeterias: Insights e Estratégias </h2>
Foi utilizado um script em Python para gerar indicadores chave de uma cafeteria a partir de seus dados de vendas.
Este script buscou responder as seguintes questões:</>

1. Analisar Tendências Mensais: Identificar quais meses tiveram mais vendas, ajudando a compreender padrões sazonais.
2. Avaliar Desempenho por Dia da Semana: Entender em quais dias a cafeteria tem mais receita, o que pode influenciar estratégias de marketing ou horários de funcionamento.
3. Comparar Filiais: Verificar qual localização da cafeteria é mais rentável, fornecendo insights para decisões estratégicas, como expansão ou marketing.
4. Identificar Produtos Populares: Determinar quais produtossão mais vendidos, auxiliando no planejamento de estoque e desenvolvimento de produtos.
5. Identificar Produtos com Maior Rentabilidade: Determinar quais produtos contribuem mais para o faturamento.<br>

   Base de dados: (https://github.com/Cleitoncsb/Analise-de-Dados-de-uma-Cafeteria-com-Python/raw/main/Coffee_Shop_Sales.xlsx)

<h2>Sobre a Métodologia</h2>
A aplicaçāo utilizada no código, segue os seguintes passos:</>

1. Importação de Bibliotecas:<br>
Pandas: Usada para manipular e analisar dados em tabelas (chamadas de DataFrames).<br>
Plotly.express: Uma biblioteca para criar gráficos interativos.<br>
Streamlit: Uma biblioteca para criar aplicações web rapidamente.<br>

2. Configuração Inicial:<br>
st.set_page_config(layout="wide"): Define a configuração da página da aplicação web para usar todo o espaço disponível na tela.<br>

3. Carregar Dados do Excel:<br>
df = pd.read_excel('/caminho/do/arquivo'): Carrega os dados de vendas de um arquivo Excel para uma tabela (DataFrame) chamada df.<br>

4. Preparação dos Dados:<br>
Converte a coluna com datas para um formato de data padrão e cria uma nova coluna chamada "Month" que contém o ano e o mês de cada venda.<br>
Filtro de Mês:<br>
Cria uma lista de meses únicos presentes nos dados e permite que o usuário escolha um mês específico para visualizar, através de um menu na lateral da aplicação.<br>

5. Visualização dos Dados Filtrados:<br>
Mostra na aplicação web os dados filtrados pelo mês escolhido.<br>

6. Criação de Gráficos:<br>
O código divide a tela em diferentes áreas para mostrar gráficos variados.<br>
Cria e exibe gráficos como:<br>
Evolução do faturamento por mês.<br>
Faturamento por dia da semana.<br>
Faturamento por filial da cafeteria.<br>
Faturamento por tipo de produto.<br>
Quantidade de vendas por tipo de produto.<br>

7. Uso dos Gráficos:<br>
Cada gráfico é criado usando plotly.express e exibido na aplicação web com streamlit.<br>
Os gráficos são interativos, permitindo ao usuário explorar os dados de formas diferentes.<br>


<h2> 📊 Resultados</h2>
Com base nas análises realizadas no nosso dashboard, conseguimos chegar nas seguintes conclusões:<br>
<br>
<br>

![Captura de Tela 2023-12-12 às 15 07 28](https://github.com/Cleitoncsb/Analise-de-Dados-de-uma-Cafeteria-com-Python/assets/142935223/c0b095c6-2ca3-4365-a423-0cf1bdec486e)

1. Tendências Mensais: A empresa tem demonstrado um crescimento exponencial crescendo 200% nos 6 primeiros meses e com possibilidade de seguir cresendo.<br>
2. Desempenho por Dia da Semana: O resultado acumulado dentro dos 6 meses, não mostrou uma variação relevante em relação aos dias da semana.<br>
3. Filiais: O desempenho das filiais também tem se mostrado muito proximo, tornando quase igual a participação de cada uma.<br>
4. Produtos Populares: Demonstrado os produtos mais populares.<br>
5. Produtos com Maior Rentabilidade: em relação aos produtos mais vendidos alguns produtos podem ser mais rentaveis mesmo não sendo os mais vendidos, um exemplo disso, é o Scone, 5º produto com maior faturamento, porem sendo o 10º produto mais vendido.<br>
