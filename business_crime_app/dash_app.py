import dash
import dash_bootstrap_components as dbc
from dash import dcc,Input,Output
from dash import html

from crimechart import CrimeChart
from crimedata import CrimeData

# Prepare the data set
data = CrimeData()
data.get_data()
borough = '(All)'
major = '(All)'
minor = '(All)'
data.process_data_for_selection(borough,major,minor)

#Create the figures
cc = CrimeChart(data)
fig_lc = cc.create_line_chart(borough,major,minor)
fig_borough_bc = cc.create_borough_bar_chart(borough,major,minor)
fig_major_bc = cc.create_major_crime_bar_chart(borough,major,minor)
fig_minor_bc = cc.create_minor_crime_bar_chart(borough,major,minor)
fig_borough_map = cc.create_borough_map(borough)

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Business Crime Dashboard'),

    dbc.Row([
        dbc.Col(width=3, children=[
            dbc.Label('Borough'),
            dcc.Dropdown(id="borough-select",
                         options=[{"label": x, "value": x} for x in data.borough_dropdown_list],
                         value="(All)",
                         placeholder='(All)'),
        ]),

        dbc.Col(width=3, children=[
            dbc.Label('Major'),
            dcc.Dropdown(id="major-select",
                         options=[{"label": x, "value": x} for x in data.major_dropdown_list],
                         value="(All)",
                         placeholder='(All)'),
        ]),
        dbc.Col(width=3, children=[
            dbc.Label('Minor'),
            dcc.Dropdown(id="minor-select",
                         options=[{"label": x, "value": x} for x in data.minor_dropdown_list],
                         value="(All)",
                         placeholder='(All)'),
        ])
    ]
    ),

    dbc.Row(children=[
        dbc.Row([
            dbc.Col(width=7, children=[
                dbc.Row([
                    dcc.Graph(
                        id='line-chart',
                        figure=fig_lc,
                        style={"height": 300}
                    )
                ]
                ),

                dbc.Row([
                    dcc.Graph(
                        id='borough-bar-chart',
                        figure=fig_borough_bc,
                        style={"height": 350}
                    )

                ]
                )
            ]
                    ),
            dbc.Col(width=5,children=[
                dcc.Graph(
                    id='map-chart',
                    figure=fig_borough_map,
                    style={"height": 700}
                )

            ])
        ]
        )
    ]
    ),
    dbc.Row([
        dbc.Col(width=5, children=[
            dcc.Graph(
                id='major-bar-chart',
                figure=fig_major_bc
            )
        ]),
        dbc.Col(width=7, children=[
            dcc.Graph(
                id='minor-bar-chart',
                figure=fig_minor_bc
            )
        ])
    ], style={"height": "10%"}
    )

])

# Create the callbacks
@app.callback(Output("line-chart", "figure"),
              Output("borough-bar-chart", "figure"),
              Output("major-bar-chart","figure"),
              Output("minor-bar-chart","figure"),
              Output("map-chart","figure"),
              Input("borough-select", "value"),
              Input("major-select", "value"),
              Input("minor-select","value"))
def update_line_chart(borough_select,major_select,minor_select):
    data.get_data()
    data.process_data_for_selection(borough_select,major_select,minor_select)
    linechart = CrimeChart(data).create_line_chart(borough_select,major_select,minor_select)
    borough_barchart = CrimeChart(data).create_borough_bar_chart(borough_select, major_select, minor_select)
    major_barchart = CrimeChart(data).create_major_crime_bar_chart(borough_select, major_select, minor_select)
    minor_barchart = CrimeChart(data).create_minor_crime_bar_chart(borough_select,major_select,minor_select)
    map = CrimeChart(data).create_borough_map(borough_select)
    return linechart,borough_barchart,major_barchart,minor_barchart,map


@app.callback(Output("minor-select","options"),
              Output("minor-select","value"),
              Input("borough-select","value"),
              Input("major-select","value"))
def update_minor_dropdown_list(borough_select,major_select):
    data.get_data()
    list = data.process_minor_dropdown_list(borough_select,major_select)
    options = [{"label": x, "value": x} for x in list]
    #print(borough_select,major_select)
    value = "(All)"
    return options,value


if __name__ == '__main__':
    app.run_server(debug=True,port=1122)
