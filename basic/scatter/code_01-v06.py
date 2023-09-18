
# title: Scatter plots and Categorical Axes

# Os gráficos de dispersão podem ser feitos usando qualquer tipo de eixo cartesiano, 
# incluindo eixos lineares, logarítmicos, categóricos ou de data.

# Os gráficos de dispersão onde um eixo é categórico são frequentemente conhecidos como gráficos de pontos.

# fonte: https://plotly.com/python/line-and-scatter/

# --- scatter-plots-and-categorical-axes ----#

import plotly.express as px

df = px.data.medals_long()
#print(df.head(3))

fig = px.scatter(
    data_frame=df,
    y='nation',
    x='count',
    color='medal',
    symbol='medal'
)
fig.update_traces(
    marker_size=10
)

fig.write_image('../images/code_01-v06.png')

fig.show()
