import folium
import pandas

volcanoes = pandas.read_csv('Volcanoes.txt')

lat = list(volcanoes['LAT'])
lon = list(volcanoes['LON'])
name = list(volcanoes['NAME'])
elev = list(volcanoes['ELEV'])


# Func to determing the volcano icon color
def color_producer(e):
    if e < 1000:
        return 'green'
    elif 1000 <= e < 3000:
        return 'orange'
    else:
        return 'red'


# Create the Map
maps = folium.Map(location=[47.5628325754074, -122.27544023142107], zoom_start=7, tiles="Stamen Terrain")

# Feature group to add Population layer to the map
# LAMBDA is an inline function (really not sure how it works)
fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 1000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Feature group to add Volcanoes layer to the Map
fgv = folium.FeatureGroup(name='Volcanoes')

html = """<h4>Volcano information:</h4>
Height: %s m
"""

for lt, ln, nm, elv in zip(lat, lon, name, elev):
    details = [nm, elv]
    iframe = folium.IFrame(html=html % str(int(elv)), width=200, height=100)
    fgv.add_child(
        folium.Marker(location=[lt, ln], popup=folium.Popup(iframe),
                      icon=folium.Icon(color=color_producer(elv))))

maps.add_child(fgp)
maps.add_child(fgv)
maps.add_child(folium.LayerControl())
maps.save('Map1.html')
