import json

infile = open('US_fires_9_1.json', 'r')

wildfire_data = json.load(infile)

json.dump(wildfire_data,outfile,indent=4)

list_of_wildfires = wildfire_data['']

lons = []
lats = []
brights = []

for wf in list_of_wildfires:
    lon = wf['longitude']
    lat = wf['latitude']
    bright = wf['brightness']
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
    'bright': brights,
    'text':hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='global_earthquakes.html')

