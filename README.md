<h1>Explorando os Dados da Cafeteria Maven Roasters com o Auxílio do Python</h1>


![Imagem1](https://github.com/Cleitoncsb/meu-Portfolio/assets/142935223/b9bf12f2-c1a3-46af-a8a8-b2fade673657)


 <h2> 📌 Overview   </h2>
 

Este projeto visa criar indicadores e fornecer percepções aprofundadas acerca do rendimento das vendas da cafeteria Maven Roasters. Ele permite uma análise minuciosa em várias dimensões como tempo, tipo de produto e localização. A base do projeto inclui várias informações, tais como transações, dias da semana, horários das transações, localização, quantidade, categorias de produtos e tipos de produtos."


<h2>☕ Um pouco sobre o setor analisado</h2>

A Arte da Experiência em Cafeterias 

No vibrante setor de cafeterias, o progresso transcende a simples oferta de um bom café. Atualmente, o êxito desses locais está fortemente atrelado à habilidade de criar experiências singulares e inesquecíveis para os frequentadores. O verdadeiro núcleo de uma cafeteria pulsante reside na sua atmosfera. Aspectos como o design do local, a seleção musical, a iluminação e até o arranjo dos assentos desempenham papéis fundamentais em forjar um ambiente acolhedor. Estes fatores vão além da estética; eles estabelecem um oásis para momentos de serenidade ou interações sociais

<h2> ⚙️ Análise das Vendas da Cafeteria Maven Roasters </h2>
Utilizamos um script Python para extrair indicadores-chave das vendas de uma cafeteria, analisando seus dados de vendas. O script foi desenvolvido para responder às seguintes perguntas:

1. Análise de Tendências Mensais: Identificar quais meses apresentaram maior volume de vendas, auxiliando na compreensão de padrões sazonais.
2. Avaliação do Desempenho por Dia da Semana: Compreender em quais dias a cafeteria registra maior receita, o que pode influenciar estratégias de marketing e horários de funcionamento.
3. Comparação entre Filiais: Verificar qual localização da cafeteria é mais lucrativa, fornecendo insights para decisões estratégicas, como expansão ou ações de marketing.
4. Identificação de Produtos Populares: Determinar quais produtos são mais vendidos, auxiliando no planejamento de estoque e no desenvolvimento de novos produtos.
5. Identificação de Produtos com Maior Rentabilidade: Estabelecer quais produtos contribuem mais para o faturamento."<br>

   Base de dados: (https://github.com/Cleitoncsb/Analise-de-Dados-de-uma-Cafeteria-com-Python/raw/main/Coffee_Shop_Sales.xlsx)

<h2> 📊 Resultados e Insigths</h2>
O resultado do código acima, retorna o dashboard que permiter enxergar de forma gráfica e simples, os resultados da empresa com base nas análises realizadas no nosso dashboard, conseguimos chegar nas seguintes conclusões:<br>
<br>
<br>

![Captura de Tela 2023-12-12 às 15 07 28](https://github.com/Cleitoncsb/Analise-de-Dados-de-uma-Cafeteria-com-Python/assets/142935223/c0b095c6-2ca3-4365-a423-0cf1bdec486e)

Sabendo da necessidade de criar boas visões, também foi criada uma visão em Power BI, apresentando os mesmos dados. <br>
Link para acesso do Dashboard em Power BI online.

<img width="614" alt="Analise Cafeteria PowerBi" src="https://github.com/Cleitoncsb/Analise-de-Dados-de-uma-Cafeteria-com-Python-e-PowerBI/assets/142935223/af11bed4-d127-4170-bb19-2d7f84d0e437">

1. Tendências Mensais: A empresa demonstrou um crescimento exponencial de 200% nos primeiros seis meses e possui potencial para continuar crescendo.
2. Desempenho por Dia da Semana: O resultado acumulado nos seis meses não apresentou variação relevante em relação aos dias da semana.
3. Filiais: O desempenho das filiais tem se mostrado muito similar, com participações quase iguais entre elas.
4. Produtos Populares: Apresentação dos produtos mais populares.
5. Produtos com Maior Rentabilidade: Em relação aos produtos mais vendidos, alguns podem ser mais rentáveis mesmo não sendo os mais vendidos. Um exemplo disso é o Scone, o 5º produto em termos de faturamento, mas apenas o 10º mais vendido.<br>


<h2>Sobre a Metodologia</h2>
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
