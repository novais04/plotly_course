# Gráfico de Barras

# chaoter.py
import plotly.express as px 

df = px.data.medals_wide()

fig = px.bar(
    data_frame=df,
    x='nation',
    y=['gold', 'silver', 'bronze'],
    title='Wide Form Data',
)

fig.show()