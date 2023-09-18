
# x e y given as DataFrame columns

import plotly.express as px 

iris = px.data.iris()
#print(iris.sample(3).T)

fig = px.scatter(
    data_frame=iris,
    x = 'sepal_width',    
    y= 'sepal_length',
)

fig.write_image(r"../images/code_01-v2.png")

fig.show()