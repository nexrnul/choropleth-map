import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://github.com/marestaing/hosting/blob/main/visited_states.csv?raw=true') 
#importing google form (csv utilzed because of ability to store numbers/text data entires with ease) into plotly 

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['number students'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'PuBu', #sequential clor scale due to graph format
    colorbar_title = "number of students who visited specific state:", #key for color scaling
))

fig.update_layout(
    title_text = 'APCSP America Choropleth Map', #general title
    geo_scope='usa', # limits map scope to USA
)

fig.show() 