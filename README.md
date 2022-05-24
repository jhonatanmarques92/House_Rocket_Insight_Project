[![Linkedin](https://img.shields.io/badge/-linkedin-blue?logo=linkedin&link=https://www.linkedin.com/in/jhonatanmarques/)](https://www.linkedin.com/in/jhonatanmarques/)

# Projeto de insights da empresa House Rocket
<img src="https://github.com/jhonatanmarques92/house_rocket_insight_project/blob/main/img/House-For-Sale.jpg" width="300" height="300">

### Observação: A empresa House Rocket é fictícia e todo o contexto não é real

## Questão de Negócio  
House Rocket é uma empresa do ramo imobiliário com o foco na compra e venda de imóveis.  
O desafio da empresa é encontrar ótimos negócios dentro de um portfólio, dentre eles imóveis mais baratos e com ótimas condições para revenda, por esse motivo,
o CEO da House Rocket entrou em contato para encontrar esse imóveis com alto potencial, onde devemos analisar o portfólio e auxiliá-lo para maximizar os lucros. Para isso devemos responder a duas questões de negócio.  
### 1 - Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?  
### 2 - Qual o melhor momento para a venda das casas?  
Ao final do projeto serão entregues 2 arquivos csv, onde um contém as recomendações de compra e outra de venda, e um dashboard com a tabela de portfólio dos imóveis e um mapa com suas localizações.  

## Premissas de Negócio  
- Para as recomendações de compra, será adotado a estratégia de recomendação de imóveis cujo o preço estejam abaixo da mediana da região, separados também se há vista para a água ou não, e as condições estejam de nível 2 para cima.
- Para a recomendação de venda, será criado uma coluna usa_season, onde serão inseridas as estações do ano. A estratégia será agrupadar por região e estações, calculando a 
mediana dos preços.
  - Caso o preço da compra for maior que a mediana da região com a sazonalidade, será adicionado 10% sobre o valor.
  - Caso o preço da compra for menor que a mediana da região com a sazonalidade, será adicionado 30% sobre o valor.

## Informações dos dados  
Os dados foram retirados do site do kaggle: https://www.kaggle.com/harlfoxem/housesalesprediction  
O conjunto de dados possuem imóveis a venda em King County-USA

| Colunas | Descrição |
| ------- | --------- |
| ID      | Identificação do imóvel |
| Date    | Data da venda do imóvel |
| Price   | Preço da venda do imóvel |
| Bedrooms | Quantidade de quartos |
| Bathrooms | Quantidade de banheiros |
| sqft_living | Tamanho da área interna do imóvel |
| sqft_lot    | Tamanho do terreno |
| Floors    | Quantidade de andares |
| Waterfront    | Vista para a água (0 para não / 1 para sim) |
| View        | Índice de 0 a 4 da vista do imóvel |
| Condition   | Índice de 0 a 5 para classificar a condição do imóvel |
| Grade       | Índice de 1 a 13 para classificar por qualidade de construção, que se refere aos tipos de materiais utilizados e à qualidade do acabamento |
| sqft_above    | Tamanho do espaço habitacional interior acima do nível do solo |
| sqft_basement    | Tamanho do espaço habitacional interior abaixo do nível do solo |
| yr_built    | Ano de construção do imóvel |
| yr_renovated    | Ano da reforma do imóvel, 0 para os nunca reformados |
| Zipcode     | CEP |
| lat         | Latitude |
| long        | Longitude |
| sqft_living15    | Tamanho médio da área interna do imóvel para as 15 casas mais próximos |
| sqft_lot15    | Tamanho médio do terreno para as 15 casas mais próximos |   

## Processo da Solução  
- Entendimento do problema de negócio  
- Coleta dos dados  
- Limpeza e tratamento dos dados   
- Levantamento e validação de hipóteses
- Análise exploratória para a geração dos relatórios
- Criação da webapp com o dashboard  

## Validação das Hipóteses
- **Hipótese 1:** Imóveis com vista para o lago são mais caros.
  - **Verdadeiro**, o valor dos imóveis com vista para o mar é mais que o dobro na média.
  ![hipotese 1](https://github.com/jhonatanmarques92/house_rocket_insight_project/blob/main/img/h1.png)
- **Hipótese 2:** A localidade do imóvel afeta no preço.
  - **Verdadeiro**, pois a localidade afeta na média das preços.
  ![hipotese 2](https://github.com/jhonatanmarques92/house_rocket_insight_project/blob/main/img/h2.png)
- **Hipótese 3:** Imóveis sem reforma custam menos.
  - **Falso**, pois há imóveis que foram reformadados e que custam menos.
  ![hipotese 3](https://github.com/jhonatanmarques92/house_rocket_insight_project/blob/main/img/h3.png)
- **Hipótese 4:** Imóveis com a construção mais antigas são mais baratas.
  - **falso**, pois há imóveis com construção mais recente que custam menos.
  ![hipotese 4](https://github.com/jhonatanmarques92/house_rocket_insight_project/blob/main/img/h4.png)
- **Hipótese 5:** Imóveis são mais caros no inverno.
  - **Falso**, pois a média dos preços no inverno são menores.
  ![hipotese 5](https://github.com/jhonatanmarques92/house_rocket_insight_project/blob/main/img/h5.png)
- **Hipótese 6:** Imóveis em piores condições são mais baratas.
  - **Verdadeiro**, pois os imóveis de níveis 1 e 2 são aproximadamente metade do valor dos outro níveis, na média.
  ![hipotese 6](https://github.com/jhonatanmarques92/house_rocket_insight_project/blob/main/img/h6.png)
- **Hipótese 7:** Imóveis com mais de cômodos são mais caras.
  - **Falso**, imóveis com mais banheiros costumam ser mais caros, porém, o mesmo não se aplica aos quartos.
  ![hipotese 7](https://github.com/jhonatanmarques92/house_rocket_insight_project/blob/main/img/h7.png)
- **Hipótese 8:** O valor médio dos imóveis ficaram mais caras no decorrer dos meses.
  - **Falso**, pois há meses em que a média dos preços caem.
  ![hipotese 8](https://github.com/jhonatanmarques92/house_rocket_insight_project/blob/main/img/h8.png)

## Resultados Financeiros
Utilizando a base de dados e as premissas de negócio, foi obtido os seguintes resultados financeiros. 

**Valor total gasto na compra:** $ 7.473.783.752,00  
**Valor total ganho na venda:** $ 7.543.421.216,90  
**Receita final:** **Lucro** de $ 69.637.464,90 

## Conclusão
Após a análise, foram criados dois arquivos no formato csv com as recomendações de compra e venda. Também foi criado um APP no Heroku ([Link do APP](https://house-rocket-analyze.herokuapp.com/)), onde pode ser filtrados a tabela com os imóveis e o mapa com suas localidades.
