import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from bokeh.plotting import ColumnDataSource, figure, output_file, show
import datetime
from bokeh.layouts import column, row
from pyproj import Proj, transform
from bokeh.tile_providers import get_provider, Vendors
from bokeh.models import HoverTool
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

# FUNCTION THAT CREATES COORDINATES
def create_coordinates(long, lat):
    ulazni_wgs=Proj(init='epsg:4326')
    izlazni_mercator=Proj(init='epsg:3857')
    long2, lat2 = long, lat
    mercator_x, mercator_y = transform(ulazni_wgs, izlazni_mercator,
                                       long2, lat2)
    return (mercator_x, mercator_y)


long_list=list(df_potvrdeni.Long.values)
lat_list=list(df_potvrdeni.Lat.values)

spojeno=zip(long_list, lat_list)

koordinate_lista=[]

for i in spojeno:
    koordinate_lista.append(i)

koordinate_lista_transformirano=[]

for j in koordinate_lista:
    koordinate_lista_transformirano.append((create_coordinates(j[0], j[1])))

x_m=[]
for xm in koordinate_lista_transformirano:
    x_m.append(xm[0])
y_m=[]
for ym in koordinate_lista_transformirano:
    y_m.append(ym[1])

source=ColumnDataSource(data=dict(x=x_m,
          y=y_m,
          novih=df_potvrdeni.iloc[:,-1].values-df_potvrdeni.iloc[:,-2].values,
          umrlih=df_umrli.iloc[:,-1].values-df_umrli.iloc[:,-2].values,
          oporavljenih=df_oporavljeni.iloc[:,-1].values-df_oporavljeni.iloc[:,-2].values))

TOOLTIPS = [
    ('NEW CASES', '@novih'),
    ('DEATHS', "@umrlih"),
    ('RECOVERED', "@oporavljenih")
]

tileProvider=get_provider(Vendors.CARTODBPOSITRON)

m=figure(plot_width=1000, plot_height=1000, x_range=(-12000000,9000000),
         y_range=(-1000000,7000000), x_axis_type='mercator', y_axis_type='mercator',
         tooltips=TOOLTIPS)

m.add_tile(tileProvider)

m.circle(x='x',y='y',size=10,color='red', source=source)
show(m)



