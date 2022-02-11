# Copied from the Dash tutorial documentation at https://dash.plotly.com/layout on 24/05/2021
# Import section modified 10/10/2021 to comply with changes in the Dash library.

# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.
from pathlib import Path
import json

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc,Input,Output
from dash import html
import numpy as np
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc,Input,Output
from dash import html

from crimechart import CrimeChart
from crimedata import CrimeData


file_path = Path(__file__).parent.joinpath('data', 'england_lad_2011.geojson')

with open(file_path) as json_file:
    la_geojson = json.load(json_file)
crime_data_path = Path(__file__).parent.joinpath('data', 'dataset_with_geo.csv')
crime_data = pd.read_csv(crime_data_path)

crime_melt = crime_data.melt(id_vars=['GEO_CODE', 'Borough', 'Major Class Description', 'Minor Class Description'],
    value_vars=['202001', '202109'],
    var_name='month')
#crime_melt = crime_melt[crime_melt['GEO_CODE'].isin(london)]
crime_prepared = crime_melt.groupby(["GEO_CODE", "Borough"]).value.sum().reset_index()


# Copied from the Dash tutorial documentation at https://dash.plotly.com/layout on 24/05/2021
# Import section modified 10/10/2021 to comply with changes in the Dash library.

# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.


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

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame see https://plotly.com/python/px-arguments/ for more options
#df = pd.DataFrame({
#    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#    "Amount": [4, 1, 2, 2, 4, 5],
 #   "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
#})

#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[

    html.H1(children='Business Crime Dashboard',style={'height':30}),

    dbc.Row([
        dbc.Col(width=3,children=[
            dbc.Label('Borough'),
            dcc.Dropdown(id="borough-select",
                         options=[{"label": x, "value": x} for x in data.borough_dropdown_list],
                         value="(All)",
                         placeholder='(All)'),
        ]),

        dbc.Col(width=3,children=[
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
    ]),
    dbc.Row([
        dbc.Col(width=5,children=[
            dbc.Col(children=[
                dcc.Graph(
                    id='borough-bar-chart',
                    figure=fig_borough_bc,
                    style={'height':300}
                )
                ]),
            dbc.Col(children=[
                dcc.Graph(
                    id='line-chart',
                    figure=fig_lc,
                    style={'height':300}
                )
                ])
            ]),
        dbc.Col(width=6, children=[
            dcc.Graph(id='map-chart',style={'height':600})
        ])
    ]),
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
    ])
    ])

# Create the callbacks
@app.callback(Output("line-chart", "figure"),
              Output("borough-bar-chart", "figure"),
              Output("major-bar-chart","figure"),
              Output("minor-bar-chart","figure"),
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
    return linechart,borough_barchart,major_barchart,minor_barchart


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
@app.callback(Output("map-chart","figure"),
              Input("borough-select","value"))
def plot_crime_by_borough(borough):
    if borough == "(All)":
        fig = px.choropleth_mapbox(crime_prepared,
                                   geojson=la_geojson,
                                   locations="GEO_CODE",
                                   featureidkey="properties.LAD19CD",
                                   color="value",
                                   color_continuous_scale='Viridis',
                                   range_color=(700, 2000),
                                   mapbox_style="carto-positron",
                                   zoom=8.4,
                                   center={"lat": 51.5074, "lon": 0.0000},
                                   opacity=0.5,
                                   hover_name="Borough",
                                   title="number of crime happened in London"
                                   )
    else:
        fig = px.choropleth_mapbox(crime_prepared[crime_prepared['Borough']==borough],
                                   geojson=la_geojson,
                                   locations="GEO_CODE",
                                   featureidkey="properties.LAD19CD",
                                   color="value",
                                   color_continuous_scale='magma',
                                   range_color=(700, 2000),
                                   mapbox_style="carto-positron",
                                   zoom=8.4,
                                   center={"lat": 51.5074, "lon": 0.0000},
                                   opacity=0.75,
                                   hover_name="Borough",
                                   title= f'number of crime happened in {borough} '
                                   )



    return fig
# @app.callback(Output("map-chart","figure"),
#               Input("major-select","value"))
# def plot_crime_by_major(major):
#

if __name__ == '__main__':
    app.run_server(debug=True,port=1122)
