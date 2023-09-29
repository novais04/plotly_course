# importando bibliotecas
import numpy as np 
import plotly
import chart_studio
import chart_studio.plotly as py
import plotly.express as px 

# atribuir valores a x e y
x = np.random.randint(low=1, high=50, size=50)
y = np.random.randint(low=51, high=100, size=50)
#print(f"{x} \n \n{y}")

# Criando Gráfico
fig = px.scatter(x=x, y=y)

#fig.show()

import chart_studio as ct

username = 'novais03'
api_key = 'BHBZxpK3Tscf4NThymJ6'

ct.tools.set_credentials_file(
    username=username,
    api_key=api_key
)

py.plot(fig, filename='Basic Scatter', auto_open=False, sharing='public')
