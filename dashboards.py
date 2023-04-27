from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('clean_data.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='League of Legends Most Picked Champions', style={'textAlign':'center'}),
    dcc.Dropdown(df.Role.unique(), 'TOP', id='role-dropdown'),
    dcc.Graph(id='role-graph'),
    html.H1(children='League of Legends Winrate by Role', style={'textAlign':'center'}),
    dcc.Dropdown(df.Class.unique(), 'Fighter', id='class-dropdown'),
    dcc.Graph(id='class-graph')

])
@callback(
    Output('role-graph', 'figure'),
    Input('role-dropdown', 'value')
)
def update_graph(value):
    dff = df[df.Role==value]
    return px.bar(x='Name', y='Pick %', data_frame=dff.sort_values(by=['Pick %'], ascending=False).reset_index()[:10], color='Name')

@callback(
    Output('class-graph', 'figure'),
    Input('class-dropdown', 'value')
)
def update_graph(value):
    dff = df[df.Class==value]
    return px.bar(x='Name', y='Win %', data_frame=dff.sort_values(by=['Win %'], ascending=False).reset_index()[:10], color='Name')



if __name__ == '__main__':
    app.run_server(debug=True)
