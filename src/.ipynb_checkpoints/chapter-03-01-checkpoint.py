# chapter-03-01.py

import plotly.graph_objects  as go
import numpy as np

x = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
#print(x)

# plotando Gráfico
fig = go.Figure(data=go.Scatter(x=x, y=x**2))


# mostrando gráfico
fig.show()