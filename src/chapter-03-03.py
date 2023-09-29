### Line charts in Dash ###

# chapter-03-03.py

# import packagers
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px 
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

# iniciando app

app = Dash(__name__, external_stylesheets=external_stylesheets)


# design
app.layout = html.Div([
    html.H4("Progressão das despesas de vida de países por continentes"),
    dcc.Graph(id='graph'),
    dcc.Checklist(
        id='checklist',
        options=["Asia", "Europe", "Africa", "Americas", "Oceania"],
        value=["America", "Oceania"],
        inline=True
    ),
])

@callback(
    Output("graph", 'figure'),
    Input("checklist", 'value')
)

def update_line_chart(continents):
    df = px.data.gapminder()
    mask = df['continent'].isin(continents)
    fig = px.line(df[mask], x='year', y='lifeExp', color='country')
    
    return fig
    



# runa

if __name__ == '__main__':
    app.run_server(debug=True)