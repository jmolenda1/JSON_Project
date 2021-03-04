import json

infile = open('US_fires_9_1.json', 'r')

wildfire_data = json.load(infile)

list_of_wildfires = wildfire_data

lons = []
lats = []
brights = []

for wf in list_of_wildfires:
    lon = wf['longitude']
    lat = wf['latitude']
    bright = wf['brightness']
    if wf['brightness']>=450:
        lons.append(lon)
        lats.append(lat)
        brights.append(bright)


print(brights[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker':{
        'size':[.05*bright for bright in brights],
        'color':brights,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}]
my_layout = Layout(title='California Wildfires 9-01-2020 until 9-13-2020')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='California_Wildfires.html')

