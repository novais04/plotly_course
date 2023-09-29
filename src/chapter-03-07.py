# Bar charts in Dash

# chapter-03-07.py
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc 

app = Dash(__name__, external_scripts=[dbc.themes.DARKLY])

app.layout = html.Div([
    html.H4('Restautantes Gorgetas por Semana'),
    dcc.Dropdown(
        id='dropdown',
        options=["Fri", "Sat", "Sun"],
        value='Fri',
        clearable=False,    
    ),
    dcc.Graph(id='graph')
])

@callback(
    Output('graph', 'figure'),
    Input('dropdown', 'value'),
)

def update_graph_chart(day):
    df = px.data.tips()
    mask = df['day'] == day 
    fig = px.bar(df[mask], x='sex', y='total_bill',
                 color='smoker', barmode='group')
    return fig
    


if __name__ == '__main__':
    app.run_server(debug=True)