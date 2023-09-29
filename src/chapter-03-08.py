# Aggregating into Single Colored Bars

# chapter-03-08.py

import plotly.express as px

df = px.data.tips() # ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']

fig = px.histogram(
    data_frame=df,
    x='sex',
    y='total_bill',
    color='smoker',
    barmode='group',
    
    text_auto=True,
)

fig.update_traces(textposition= 'outside') #  ['inside', 'outside', 'auto', 'none']


fig.update_layout(
    height=800,
    title_text="Aggregating into Single Colored Bars",
    
)

fig.show()