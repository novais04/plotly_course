
# x e y given as DataFrame columns

import plotly.express as px 


iris = px.data.iris()

fig = px.scatter(
    data_frame=iris,
    x='sepal_width',
    y='sepal_length',
    color='petal_length'
)

fig.write_image('../images/code_01-v04.png')

fig.show()