from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('clean_data.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='League of Legends Champion Pick %', style={'textAlign':'center'}),
    dcc.Dropdown(df.Role.unique(), 'TOP', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.Role==value]
    return px.bar(x='Name', y='Pick %', data_frame=dff.sort_values(by=['Pick %'], ascending=False).reset_index()[:10], color='Name')

if __name__ == '__main__':
    app.run_server(debug=True)
