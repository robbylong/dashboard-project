from pathlib import Path
import plotly.express as px
import pandas as pd
import json
import numpy as np

file_path = Path(__file__).parent.joinpath('data', 'england_lad_2011.geojson')

with open(file_path) as json_file:
    la_geojson = json.load(json_file)

    # Read the data for the over 100's (F105) into a data frame skipping the second heading row
age_data_path = Path(__file__).parent.joinpath('data', 'la_age_data.csv')
age_data = pd.read_csv(age_data_path, usecols=["GEO_CODE", "GEO_LABEL", "F105"], skiprows=[1])
crime_data_path = Path(__file__).parent.joinpath('data', 'dataset_with_geo.csv')
crime_data = pd.read_csv(crime_data_path)

crime_melt = crime_data.melt(id_vars=['GEO_CODE', 'Borough', 'Major Class Description', 'Minor Class Description'],
    value_vars=['202001', '202109'],
    var_name='month')
#crime_melt = crime_melt[crime_melt['GEO_CODE'].isin(london)]
print(crime_melt.sample(10))
crime_prepared = crime_melt.groupby(["GEO_CODE", "Borough"]).value.sum().reset_index()
print(crime_prepared)

def plot_crime_by_borough(borough):
    fig = px.choropleth_mapbox(crime_melt,
                               geojson=la_geojson,
                               locations="GEO_CODE",
                               featureidkey="properties.LAD19CD",
                               color="value",
                               color_continuous_scale='Viridis',
                               range_color=(0, 200),
                               mapbox_style="carto-positron",
                               zoom=8,
                               center={"lat": 51.5074, "lon": 0.0000},
                               opacity=0.5,
                               hover_name="GEO_LABEL",
                               labels={'GEO_LABEL': 'Local authority'},
                               title="crime happened in London"
                               )
    return fig

