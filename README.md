<h1>Análise de Dados de uma Cafeteria com Python </h1>


![Imagem1](https://github.com/Cleitoncsb/meu-Portfolio/assets/142935223/b9bf12f2-c1a3-46af-a8a8-b2fade673657)


 <h2> Overview   </h2>
 

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
5. Identificar Produtos com Maior Rentabilidade: Determinar quais produtos contribuem mais para o faturamento.

<h2>Sobre a Métodologia</h2>
A aplicaçāo utilizada no código, segue os seguintes passos:</>

1. Importação de Bibliotecas:</>
Pandas: Usada para manipular e analisar dados em tabelas (chamadas de DataFrames).<br>
Plotly.express: Uma biblioteca para criar gráficos interativos.<br>
Streamlit: Uma biblioteca para criar aplicações web rapidamente.<br>

Configuração Inicial:
st.set_page_config(layout="wide"): Define a configuração da página da aplicação web para usar todo o espaço disponível na tela.<br>

Carregar Dados do Excel:
df = pd.read_excel('/caminho/do/arquivo'): Carrega os dados de vendas de um arquivo Excel para uma tabela (DataFrame) chamada df.<br>

Preparação dos Dados:
Converte a coluna com datas para um formato de data padrão e cria uma nova coluna chamada "Month" que contém o ano e o mês de cada venda.<br>

Filtro de Mês:
Cria uma lista de meses únicos presentes nos dados e permite que o usuário escolha um mês específico para visualizar, através de um menu na lateral da aplicação.<br>

Visualização dos Dados Filtrados:
Mostra na aplicação web os dados filtrados pelo mês escolhido.
Criação de Gráficos:
O código divide a tela em diferentes áreas para mostrar gráficos variados.
Cria e exibe gráficos como:
Evolução do faturamento por mês.
Faturamento por dia da semana.
Faturamento por filial da cafeteria.
Faturamento por tipo de produto.
Quantidade de vendas por tipo de produto.

Uso dos Gráficos:
Cada gráfico é criado usando plotly.express e exibido na aplicação web com streamlit.
Os gráficos são interativos, permitindo ao usuário explorar os dados de formas diferentes.
