# IMPORT LIBRARIES
import folium
from folium import plugins
import pandas as pd
import numpy as np
import datetime

# URL
url_potvrdeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_umrli='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_oporavljeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

try:
    df_potvrdeni=pd.read_csv(url_potvrdeni)
    df_umrli=pd.read_csv(url_umrli)
    df_oporavljeni=pd.read_csv(url_oporavljeni)

except:
    print('Something went wrong... URL problems')

# ROWS DON'T MATCH, FIXING AND SORTING VALUES
cro_potvrdeni=df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Canada']
cro_umrli=df_umrli.loc[df_umrli['Country/Region']=='Canada']


Lat=52.9399
Long=-73.5491
cro_potvrdeni=cro_potvrdeni.groupby('Country/Region').sum()
cro_umrli=cro_umrli.groupby('Country/Region').sum()

cro_potvrdeni['Lat']=Lat
cro_potvrdeni['Long']=Long
cro_potvrdeni['Province/State']='None'
cro_umrli['Lat']=Lat
cro_umrli['Long']=Long


cro_potvrdeni.reset_index(inplace=True)
cro_umrli.reset_index(inplace=True)
cro_umrli['Province/State']='NaN'
cro_potvrdeni['Province/State']='NaN'

mid = cro_potvrdeni['Province/State']
cro_potvrdeni.drop(labels=['Province/State'], axis=1,inplace = True)
cro_potvrdeni.insert(0, 'Province/State', mid)

mid = cro_umrli['Province/State']
cro_umrli.drop(labels=['Province/State'], axis=1,inplace = True)
cro_umrli.insert(0, 'Province/State', mid)

df_potvrdeni=df_potvrdeni.drop(df_potvrdeni[df_potvrdeni['Country/Region']=='Canada'].index)

df_umrli=df_umrli.drop(df_umrli[df_umrli['Country/Region']=='Canada'].index)
df_potvrdeni=df_potvrdeni.append(cro_potvrdeni, ignore_index=True)
df_umrli=df_umrli.append(cro_umrli, ignore_index=True)

df_potvrdeni=df_potvrdeni.sort_values('Country/Region')
df_umrli=df_umrli.sort_values('Country/Region')
df_oporavljeni=df_oporavljeni.sort_values('Country/Region')

df_potvrdeni.reset_index(inplace=True, drop=True)
df_umrli.reset_index(inplace=True, drop=True)
df_oporavljeni.reset_index(inplace=True, drop=True)

# LISTS OF COORDINATES
long_list=list(df_potvrdeni.Long.values)
lat_list=list(df_potvrdeni.Lat.values)

# CONNECTING - ZIP
spojeno=zip(long_list, lat_list)

koordinate_lista=[]

for i in spojeno:
    koordinate_lista.append(i)

# FILTER    
novih=df_potvrdeni.iloc[:,-1].values-df_potvrdeni.iloc[:,-2].values
umrlih=df_umrli.iloc[:,-1].values-df_umrli.iloc[:,-2].values
oporavljenih=df_oporavljeni.iloc[:,-1].values-df_oporavljeni.iloc[:,-2].values

# FILTER2    
uk_potvrdenih=df_potvrdeni.iloc[:,-1].values
uk_umrlih=df_umrli.iloc[:,-1].values
uk_oporavljenih=df_oporavljeni.iloc[:,-1].values


m=folium.Map(location=[52.954784,-1.158109],zoom_start=5)


#### TYPES OF MAPS
folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)


#### MINI MAP, ZOOM TOOLS
minimap=plugins.MiniMap(toggle_display=True)
m.add_child(minimap)
plugins.ScrollZoomToggler().add_to(m)
plugins.Fullscreen(position='topright').add_to(m)


#### GET LAT AND LONG TOOLS
m.add_child(folium.LatLngPopup())


#### MEASURING TOOLS
measure_control = plugins.MeasureControl(position='topleft',active_color='red',completed_color='blue',primary_length_unit='metres')
m.add_child(measure_control)


#### DRAWING TOOLS
draw=plugins.Draw(export=True).add_to(m)


###### TOTAL NUMBERS LAYER
fg=folium.FeatureGroup(name="Ukupne brojke").add_to(m)

b=0
for k in koordinate_lista:
    loc=[k[1],k[0]]
    try:
        pop="<strong>NEW: </strong>"+str(uk_potvrdenih[b])+'\n'+"<strong>DEATHS: </strong>"+str(uk_umrlih[b])+'\n'+"<strong>RECOVERED: </strong>"+str(uk_oporavljenih[b])
    except:
        pop="<strong>NEW: </strong>"+str(uk_potvrdenih[b])+'\n'+"<strong>DEATHS: </strong>"+str(uk_umrlih[b])+'\n'+"<strong>RECOVERED: </strong>"+'No Data'
    # ADD A MARKER
    mk=folium.Marker(location=loc, tooltip="TOTAL", popup=pop).add_to(m)
    fg.add_child(mk)
    b+=1

# ADD LAYER TO MAP
m.add_child(fg)

###### DAILY NUMBERS LAYER
fg1=folium.FeatureGroup(name="Dnevne brojke").add_to(m)

g=0
for j in koordinate_lista:
    loc1=[j[1],j[0]]
    try:
        pop1="<strong>NEW: </strong>"+str(novih[g])+'\n'+"<strong>DEATHS: </strong>"+str(umrlih[g])+'\n'+"<strong>RECOVERED: </strong>"+str(oporavljenih[g])
    except:
        pop1="<strong>NEW: </strong>"+str(novih[g])+'\n'+"<strong>DEATHS: </strong>"+str(umrlih[g])+'\n'+"<strong>RECOVERED: </strong>"+'No data'
    # ADD A MARKER
    mk1=folium.Marker(location=loc1, tooltip="DAILY", popup=pop1).add_to(m)
    fg1.add_child(mk1)
    g+=1

# ADD LAYER TO MAP
m.add_child(fg1)

# ADD LAYER CONTROL TO MAP
m.add_child(folium.LayerControl())

# SAVE MAP
m.save('web_map.html')
