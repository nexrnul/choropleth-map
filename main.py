import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('url goes here')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['number students'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Blues',
    colorbar_title = "color scale title",
))

fig.update_layout(
    title_text = 'title here',
    geo_scope='usa', # limite map scope to USA
)

fig.show()