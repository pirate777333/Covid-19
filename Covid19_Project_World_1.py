# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import geopandas as gpd
from shapely.geometry import Point

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

# INPUT NAME OF THE COUNTRY
drzava=input('Unesite drzavu:  ')
print('Vasa drzava:  '+drzava)
drzava=drzava.lower()
drzava=drzava.title()

try:
    cp=df_potvrdeni.loc[df_potvrdeni['Country/Region']==drzava]
    cu=df_umrli.loc[df_umrli['Country/Region']==drzava]
    co=df_oporavljeni.loc[df_oporavljeni['Country/Region']==drzava]
    p=cp.iloc[:,-1].values[0]-cp.iloc[:,-2].values[0] # DIFFERENCE LAST 2 COLUMNS
    u=cu.iloc[:,-1].values[0]-cu.iloc[:,-2].values[0]
    o=co.iloc[:,-1].values[0]-co.iloc[:,-2].values[0]
except:
    print('Something went wrong. Name of the Country is wrong or does not exist.')

# FORMAT THE MESSAGE    
print(str(p)+' New cases\n' + str(u) + ' Deaths\n' + str(o)+' Recovered')
t=drzava+'\n'+str(p)+' New cases\n' + str(u) + ' Deaths\n' + str(o)+' Recovered'

# X COORDINATES
drzx=cp.loc[:,'Long'].values[0]

# Y COORDINATES
drzy=cp.loc[:,'Lat'].values[0]

# CRS SETUP - 4326 WGS
crs_={'init':'epsg:4326'}

# FORMAT THE GEOMETRY COLUMN - SET OF POINTS
geometry_ = [Point(x,y) for x,y in zip(df_potvrdeni['Long'],df_potvrdeni['Lat'])]

# FORMAT THE GEODATAFRAME ( DATA FRAME, CRS, GEOMETRY COLUMN)
geo_df=gpd.GeoDataFrame(df_potvrdeni, crs=crs_, geometry=geometry_)

# LOAD THE SHP FILE
gpdf=gpd.read_file('C:/Users/Josko/Desktop/my_projects/Covid_Cro/ne_10m_admin_0_countries.shp')

# PLOT
fig, ax = plt.subplots(figsize=(20, 18))
gpdf.plot(ax=ax)
geo_df.plot(ax=ax, color='red', markersize=10)
ax.annotate(t, xy=(drzx,drzy), xytext=(-45,40), arrowprops={'width':1,'color':'black','headwidth':5})
plt.show()
