# IMPORT LIBRARIES
import pandas as pd
import numpy as np
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from datetime import datetime
from bokeh.layouts import column, row
from pyproj import Proj, transform
from bokeh.tile_providers import get_provider, Vendors
from bokeh.models import HoverTool
import ipywidgets
from bokeh.io import push_notebook
from bokeh.models import Range1d
from bokeh.models.widgets import Panel, Tabs

# URL
url_potvrdeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_umrli='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_oporavljeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

# IMPORT DATA
try:
    df_potvrdeni=pd.read_csv(url_potvrdeni)
    df_umrli=pd.read_csv(url_umrli)
    df_oporavljeni=pd.read_csv(url_oporavljeni)

except:
    print('Something went wrong... URL problems')

# COLUMN Country/Region IS NOW INDEX

# CONFIRMED
df_grupirano_potvrdeni=df_potvrdeni.groupby('Country/Region').sum()
df_grupirano_potvrdeni_dates=df_grupirano_potvrdeni.iloc[:,2:]

# DEATHS
df_grupirano_umrli=df_umrli.groupby('Country/Region').sum()
df_grupirano_umrli_dates=df_grupirano_umrli.iloc[:,2:]

# RECOVERED
df_grupirano_oporavljeni=df_oporavljeni.groupby('Country/Region').sum()
df_grupirano_oporavljeni_dates=df_grupirano_oporavljeni.iloc[:,2:]

drzava=input('Input Country:  ')
drzava=drzava.lower()
drzava=drzava.title()
print('Your Country:  ' + drzava)

try:
    df_drzavni_potvrdeni=df_grupirano_potvrdeni_dates.loc[drzava].to_frame()
    df_drzavni_umrli=df_grupirano_umrli_dates.loc[drzava].to_frame()
    df_drzavni_oporavljeni=df_grupirano_oporavljeni_dates.loc[drzava].to_frame()

except:
    print('Došlo je do greške, ime države je neispravno ili ne postoji')

# CREATE VARIABLES TO CALCULATE DIFFERENCES FOR DAILY NUMBERS OF CASES (CONFIRMED, DEATHS, RECOVERED)
v1=df_grupirano_potvrdeni_dates.shape[1]
v2=df_grupirano_umrli_dates.shape[1]
v3=df_grupirano_oporavljeni_dates.shape[1]

v4=v1-1
v5=v2-1
v6=v3-1

##########################################################################################

# CONFIRMED

# X 
x_drzavni_potvrdeni=df_drzavni_potvrdeni.index[-v4:].tolist()

# Y 
y_drzavni_potvrdeni=[]
for i in df_drzavni_potvrdeni.iloc[-v4:].values:
    for j in i:
        y_drzavni_potvrdeni.append(j)

y_drzavni_potvrdeni2=[]
for i in df_drzavni_potvrdeni.iloc[-v1:-1].values:
    for j in i:
        y_drzavni_potvrdeni2.append(j)

# REVERSED 2 DEFINED LISTS        
yr=list(reversed(y_drzavni_potvrdeni))
yrc=list(reversed(y_drzavni_potvrdeni2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYAS
ny=yra-yrca

# TO LIST, REVERSED
ny=list(reversed(ny))

# X TO DATETIME
x_drzavni_potvrdeni_dates=[]
for s in x_drzavni_potvrdeni: #'8/29/20'
    x_drzavni_potvrdeni_dates.append(datetime.strptime(s, '%m/%d/%y'))

# CREATE SOURCE FOR FIGURE
source=ColumnDataSource(data={
    'x' : x_drzavni_potvrdeni_dates,
    'broj' : ny})
TOOLS="crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
p_potvrdeni=figure(plot_width=1800, plot_height=850,x_axis_type='datetime', tools=TOOLS,
                   title='Dnevne brojke novih slučajeva')
p_potvrdeni.background_fill_color="#fdffe3"
p_potvrdeni.grid.grid_line_color="white"
p_potvrdeni.xaxis.axis_label = 'Date'
p_potvrdeni.yaxis.axis_label = 'Broj novozaraženih'
p_potvrdeni.axis.axis_line_color = None

p_potvrdeni.line(x='x', y='broj', line_width=2, line_color='blue', source=source) # line_width=3
p_potvrdeni.circle(x='x', y='broj', size=5,color='blue', fill_color='white', source=source) # line_width=3

# HOVER TOOL, SPECIAL
p_potvrdeni.add_tools(HoverTool(
    tooltips=[
        ('datum', '@x{%m/%d/%y}'),
        ('broj', '@broj')],
    formatters={
        '@x':'datetime',
        'broj':'numeral'},
    mode='vline'))

##########################################################################################

# DEATHS

# X 
x_drzavni_umrli=df_drzavni_umrli.index[-v5:].tolist()

# Y 
y_drzavni_umrli=[]
for i in df_drzavni_umrli.iloc[-v5:].values:
    for j in i:
        y_drzavni_umrli.append(j)

y_drzavni_umrli2=[]
for i in df_drzavni_umrli.iloc[-v2:-1].values:
    for j in i:
        y_drzavni_umrli2.append(j)


# REVERSED 2 DEFINED LISTS       
yr=list(reversed(y_drzavni_umrli))
yrc=list(reversed(y_drzavni_umrli2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYAS
ny=yra-yrca

# TO LIST, REVERSED
ny=list(reversed(ny))

x_drzavni_umrli_dates=[]
for s in x_drzavni_umrli: #'8/29/20'
    x_drzavni_umrli_dates.append(datetime.strptime(s, '%m/%d/%y'))

source1=ColumnDataSource(data={
    'x' : x_drzavni_potvrdeni_dates,
    'broj' : ny})

p_umrli=figure(plot_width=1800, plot_height=850,x_axis_type='datetime', tools=TOOLS,
                   title='Dnevne brojke umrlih')
p_umrli.background_fill_color="#fdffe3"
p_umrli.grid.grid_line_color="white"
p_umrli.xaxis.axis_label = 'Date'
p_umrli.yaxis.axis_label = 'Broj umrlih'
p_umrli.axis.axis_line_color = None

p_umrli.circle(x='x', y='broj', size=5, fill_color='white' ,color='red', source=source1) # line_width=3

p_umrli.vbar(x='x', top='broj', color='red', width=0.5,source=source1)

p_umrli.add_tools(HoverTool(
    tooltips=[
        ('datum', '@x{%m/%d/%y}'),
        ('broj', '@broj')],
    formatters={
        '@x':'datetime',
        'broj':'numeral'},
    mode='vline'))

##########################################################################################

# RECOVERED

# X 
x_drzavni_oporavljeni=df_drzavni_oporavljeni.index[-v6:].tolist()

# Y 
y_drzavni_oporavljeni=[]
for i in df_drzavni_oporavljeni.iloc[-v6:].values:
    for j in i:
        y_drzavni_oporavljeni.append(j)

y_drzavni_oporavljeni2=[]
for i in df_drzavni_oporavljeni.iloc[-v3:-1].values:
    for j in i:
        y_drzavni_oporavljeni2.append(j)


# REVERSED 2 DEFINDED LISTS      
yr=list(reversed(y_drzavni_oporavljeni))
yrc=list(reversed(y_drzavni_oporavljeni2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYA
ny=yra-yrca

# TO LIST, REVERSED
ny=list(reversed(ny))

x_drzavni_oporavljeni_dates=[]
for s in x_drzavni_oporavljeni: #'8/29/20'
    x_drzavni_oporavljeni_dates.append(datetime.strptime(s, '%m/%d/%y'))

source2=ColumnDataSource(data={
    'x' : x_drzavni_oporavljeni_dates,
    'broj' : ny})

p_oporavljeni=figure(plot_width=1800, plot_height=850,x_axis_type='datetime', tools=TOOLS,
                   title='Dnevne brojke oporavljenih')
p_oporavljeni.background_fill_color="#fdffe3"
p_oporavljeni.grid.grid_line_color="white"
p_oporavljeni.xaxis.axis_label = 'Date'
p_oporavljeni.yaxis.axis_label = 'Broj oporavljenih'
p_oporavljeni.axis.axis_line_color = None

p_oporavljeni.line(x='x', y='broj', line_color='green',line_width=2, source=source2) # line_width=3
p_oporavljeni.circle(x='x', y='broj', size=5,color='green', fill_color='white', source=source2) # line_width=3

p_oporavljeni.add_tools(HoverTool(
    tooltips=[
        ('datum', '@x{%m/%d/%y}'),
        ('broj', '@broj')],
    formatters={
        '@x':'datetime',
        'broj':'numeral'},
    mode='vline'))


##########################################################################################

# ACTIVE

# X 
x_drzavni_oporavljeni=df_drzavni_oporavljeni.index[-v4:].tolist()

# Y CONFIRMED - DEATHS - RECOVERED
a=np.array(y_drzavni_potvrdeni)
b=np.array(y_drzavni_umrli)
c=np.array(y_drzavni_oporavljeni)
y_aktivni=a-b-c

x_drzavni_aktivni_dates=[]
for s in x_drzavni_oporavljeni: #'8/29/20'
    x_drzavni_aktivni_dates.append(datetime.strptime(s, '%m/%d/%y'))

source3=ColumnDataSource(data={
    'x' : x_drzavni_oporavljeni_dates,
    'broj' : y_aktivni})

p_aktivni=figure(plot_width=1800, plot_height=850,x_axis_type='datetime', tools=TOOLS,
                   title='Dnevne brojke aktivnih slučajeva')
p_aktivni.background_fill_color="#fdffe3"
p_aktivni.grid.grid_line_color="white"
p_aktivni.xaxis.axis_label = 'Date'
p_aktivni.yaxis.axis_label = 'Broj aktivnih slučajeva'
p_aktivni.axis.axis_line_color = None

p_aktivni.line(x='x', y='broj', line_color='orange',line_width=2, source=source3) # line_width=3
p_aktivni.circle(x='x', y='broj', size=5,color='orange', fill_color='white', source=source3) # line_width=3

p_aktivni.add_tools(HoverTool(
    tooltips=[
        ('datum', '@x{%m/%d/%y}'),
        ('broj', '@broj')],
    formatters={
        '@x':'datetime',
        'broj':'numeral'},
    mode='vline'))

# PANELS
first=Panel(child=row(p_potvrdeni), title='Potvrdeni')
second=Panel(child=row(p_umrli), title='Umrli')
third=Panel(child=row(p_oporavljeni), title='Oporavljeni')
fourth=Panel(child=row(p_aktivni), title='Aktivni')

# TABS, OUTPUT, SHOW IT
tabs=Tabs(tabs=[first, second,third, fourth])
output_file('tabbed_countries.html')

show(tabs)
