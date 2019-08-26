import folium
import pandas as pd

data = pd.read_csv('Volcanoes.txt')
lon = list(data['LON'])
lat = list(data['LAT'])
ele = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.99], zoom_start=6, tiles = "Stamen Terrain")

#Volcanoes Map
fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el in zip(lat, lon , ele):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(el)+ " m", parse_html=True), icon=folium.Icon(color=color_producer(el))))




#Population Map
fgp = folium.FeatureGroup(name='Population')


fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 100000000 
else 'orange' if 100000000 <=x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('Map1.html')