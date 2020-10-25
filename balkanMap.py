import folium
import json

balkanMap = folium.Map(location=[42.753213, 21.156792], zoom_start=4, tiles="Stamen Terrain")


data = json.load(open("world.json", encoding="utf-8-sig"))

bal_countries = [x for x in data['features']
if x['properties']['NAME'] == 'Albania'
or x['properties']['NAME'] == 'Greece'
or x['properties']['NAME'] == 'Serbia'
or x['properties']['NAME'] == 'Montenegro'
or x['properties']['NAME'] == 'Romania'
or x['properties']['NAME'] == 'Slovenia'
or x['properties']['NAME'] == 'Croatia'
or x['properties']['NAME'] == 'Bosnia and Herzegovina'
or x['properties']['NAME'] == 'Turkey'
or x['properties']['NAME'] == 'Bulgaria']

pop = list()
lat = list()
lon = list()

for i in range(len(bal_countries)):

    pop.append(bal_countries[i]['properties']['POP2005'])
    lat.append(bal_countries[i]['properties']['LAT'])
    lon.append(bal_countries[i]['properties']['LON'])

fg = folium.FeatureGroup("MapFeatures")
for lt, ln, pl in zip(lat, lon, pop):
    fg.add_child(folium.Marker(location=[lt, ln], popup='Population '+str(pl), icon=folium.Icon(color='green')))

fg.add_child(folium.GeoJson(data = open("world.json", 'r', encoding="utf-8-sig").read(),
style_function = lambda x: {'fillColor':'green' if  x['properties']['POP2005'] < 3000000 and  (x in bal_countries)
else 'yellow' if 3000000 < x['properties']['POP2005'] < 10000000 and  (x in bal_countries)
else 'red' if 10000000 < x['properties']['POP2005'] < 90000000 and  (x in bal_countries)
else 'white'}))

balkanMap.add_child(fg)
balkanMap.save("balkanMap.html")
