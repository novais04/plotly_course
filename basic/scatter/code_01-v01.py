
# x e y given as array_like objects

import plotly.express as px 

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

fig.write_image(r"../images/code_01-v1.png")

fig.show()