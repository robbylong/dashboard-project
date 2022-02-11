import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
external_stylesheets = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css"]
prepared_dataset = pd.read_csv('prepared_dataset.csv')
#df1 = prepared_dataset.groupby(["Borough"]).sum()
prepared_dataset['Total Offences']= prepared_dataset.iloc[:, 4:].sum(axis=1)
fig_bar = px.bar(prepared_dataset, x="Borough", y="Total Offences")
fig_bar.update_traces(textfont_size=12, textangle=90, textposition="outside", cliponaxis=False)
fig_line=px.line(prepared_dataset,x=)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#fig_bar=px.bar(prepared_dataset,x='Borough',y='Major Class Description')
app.layout = html.Div([
    html.Div([

        html.Div([

            html.Br(),
            html.Label(['Borough:'],style={'font-weight': 'bold', "text-align": "center"}),
            dcc.Dropdown(
                id='Borough',
                options=[
                    {'label': Borough, 'value': Borough}
                    for Borough in prepared_dataset['Borough'].unique()
                ],
                placeholder='All',
                style={'width': "150%"},
                searchable=True,
                optionHeight=50)],
        style={'width': '10%', 'display': 'inline-block'}),
        #html.Label(['Major:'], style={'font-weight': 'bold', "text-align": "center"}),

        html.Div([
            html.Br(),
            html.Label(['Major:'], style={'font-weight': 'bold', "text-align": "center"}),
            dcc.Dropdown(
                id='Major',
                options=[
                    {'label': Major,'value': Major}
                    for Major in prepared_dataset['Major Class Description'].unique()

                ],
                placeholder='All',
                style={'width':'150%'},
                optionHeight=50
            )
            ],
        style={'width': '10%', 'display': 'inline-block'}),
        html.Div([
            html.Br(),
            html.Label(['Minor:'], style={'font-weight': 'bold', "text-align": "center"}),
            dcc.Dropdown(
                id='Minor',
                options=[
                    {'label': Minor,'value': Minor}
                    for Minor in prepared_dataset['Minor Class Description'].unique()

                ],
                placeholder='All',
                style={'width':'150%'},
                optionHeight=50
            )

        ],
        style={'width': '10%', 'display': 'inline-block'})
        ]),
    html.Div([
        dcc.Graph(figure=fig_bar)

    ]),
    html.Div([
        dcc.Graph(figure=)
    ])
#     html.Div([
#         dcc.Graph(
#             id='barplot-offences-by-bourgh',
#             hoverData={'points': [{'customdata': 'Japan'}]}
#         )
#     ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
#     html.Div([
#         dcc.Graph(id='x-time-series'),
#         dcc.Graph(id='y-time-series'),
#     ], style={'display': 'inline-block', 'width': '49%'})
  ])




if __name__ == '__main__':
    app.run_server(debug=True)