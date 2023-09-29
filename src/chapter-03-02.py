# chapter-03-01.py

import plotly.graph_objects as go
import numpy as np 
np.random.seed(1)

N  = 100
x  = np.linspace(0,1,N)
y0 = np.random.randn(N) + 5
y1 = np.random.randn(N)
y2 = np.random.randn(N) - 5


# plotando Gráfico
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=x,
        y=y0,
        mode='lines',
        name='lines'
    ),
)

fig.add_trace(
    go.Scatter(
        x=x,
        y=y1,
        mode='lines+markers',
        name='lines+markers'
    ),
)

fig.add_trace(
    go.Scatter(
        x=x,
        y=y2,
        mode='markers',
        name='markers'
    ),
)

# mostrando gráfico
fig.show()


# exportando para web
import chart_studio as ct
import chart_studio.plotly as py

username = 'novais03'
api_key = 'BHBZxpK3Tscf4NThymJ6'

ct.tools.set_credentials_file(
    username=username,
    api_key=api_key
)

py.plot(fig, filename='Line Plot Modes', auto_open=True, sharing='public')