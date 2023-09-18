from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    html.H4("Interagindo Scatter plot com Itris dataset"),
    dcc.Graph(id='scatter-plot'),
    html.P("Filtrando per 'petal width':"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=2.5, step=0.1,
        marks={0:'0', 2.5:'2.5'},
        value=[0.5, 2.0]    
    ),
])

@callback(
    Output('scatter-plot', 'figure'),
    Input('range-slider', 'value'),
)
def upadate_scatter_chart(slider_range):
    df = px.data.iris()
    low, high = slider_range
    mask = (df['petal_width'] > low) & (df['petal_width'] < high)
    fig = px.scatter(
        data_frame=df[mask],
        x='sepal_width', 
        y='sepal_length',
        color='species',
        size='petal_length',
        hover_data=['petal_width']
    )    
    return fig
    
# run
if __name__=='__main__':    
    app.run_server(debug=True)