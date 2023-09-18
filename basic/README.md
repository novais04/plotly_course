# Estudo de visualização usando plotly
font: [plotly basic](https://plotly.com/python/line-and-scatter/)

# Scatter Plots in Python 
    Como fazer gráficos de dispersão em Python com Plotly.

__Plotly Express__ é a interface de alto nível fácil de usar para Plotly, que opera em uma variedade de tipos de dados e produz figuras fáceis de estilizar.

Com `px.scatter`, cada ponto de dados é representado como um ponto marcador, cuja localização é dada pelas colunas x e y.

fonte: [line-scatter](https://plotly.com/python/line-and-scatter/)



## Configurando tamanho e cor com nomes de colunas

Os gráficos de dispersão (__scater__) com marcadores circulares de tamanho variável são frequentemente conhecidos como gráficos de bolhas (__bubble charts__). Observe que os dados de cor e tamanho são adicionados às informações instantâneas. Você pode adicionar outras colunas aos dados flutuantes com o argumento hover_data de px.scatter.
    
    code_01-v03.py

## A cor pode ser contínua como segue, ou discreta/categórica como acima.

    code_01-v04.py

## O argumento do símbolo também pode ser mapeado para uma coluna. Uma grande variedade de símbolos está disponível.

    code_01-v05.py

## Scatter plots in Dash
__Dash__ é a melhor maneira de construir aplicativos analíticos em Python usando figuras __Plotly__. Para executar o aplicativo abaixo, execute pip install dash.

    app.py



