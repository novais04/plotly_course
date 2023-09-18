
# x e y given as DataFrame columns

import plotly.express as px 


iris = px.data.iris()

fig = px.scatter(
    data_frame=iris,
    x = 'petal_length',
    y = 'petal_width',
    color='species',
    size='sepal_width',
    hover_data=['sepal_length'],   
)

fig.write_image('../images/code_01-v03.png')

fig.show()