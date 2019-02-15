
# coding: utf-8




import folium
import pandas





file=pandas.read_csv('Volcanoes.txt')
#file





lat=list(file['LAT'])
lon=list(file['LON'])
elev=list(file['ELEV'])
# print(lat)
# print('/n')
# print(lon)
# print('/n')
# print(elev)





def color_producer(elevation):
    if elevation < 1000:
        return 'blue'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'





#map=folium.Map(location=[28.35,77.4] ,zoom_start=6,tiles='Mapbox Bright')





fg=folium.FeatureGroup(name='my map')




#for coordinate in [[28,77],[29,78]]:
#    fg.add_child(folium.Marker(location=[28.35,77.4] , popup='hello', icon=folium.Icon(color='red')))
#    fg.add_child(folium.Marker(location=coordinate , popup='hello', icon=folium.Icon(color='blue')))





for la , lo ,ele in zip(lat, lon ,elev):
    fg.add_child(folium.Marker(location=[la,lo] , popup=str(ele), icon=folium.Icon(color=color_producer(ele))))





map.add_child(fg)





map.add_child(folium.LayerControl())





map.save('map.html')

