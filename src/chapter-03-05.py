## Grafico de barras

# chapter-03-05.py

#import packegers
import plotly.express as px
long_df = px.data.medals_long()
#print(long_df)

fig = px.bar(
    data_frame=long_df,
    x='nation',
    y='count',
    color='medal',
    title='Long-Form Input'
)

fig.show()
