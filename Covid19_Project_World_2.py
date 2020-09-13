# IMPORT LIBRARIES
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
import datetime
from bokeh.layouts import column, row

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
    print('Something went wrong. Name of the Country is wrong or it does not exist.')

##########################################################################################

# CONFIRMED

# X 
x_drzavni_potvrdeni=df_drzavni_potvrdeni.index[-30:].tolist()

# Y 
y_drzavni_potvrdeni=[]
for i in df_drzavni_potvrdeni.iloc[-30:].values:
    for j in i:
        y_drzavni_potvrdeni.append(j)

y_drzavni_potvrdeni2=[]
for i in df_drzavni_potvrdeni.iloc[-31:-1].values:
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

# TOOLS 
TOOLS="crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

# X TO DATETIME
x_drzavni_potvrdeni_dates=[]
for s in x_drzavni_potvrdeni: #'8/29/20'
    x_drzavni_potvrdeni_dates.append(datetime.datetime.strptime(s, '%m/%d/%y'))

# FIGURE, PLOT
p_potvrdeni=figure(plot_width=600,x_axis_type='datetime', tools=TOOLS) # X AXIS TYPE = DATETIME
p_potvrdeni.line(x=x_drzavni_potvrdeni_dates, y=ny, line_width=2, line_color='blue')
p_potvrdeni.circle(x=x_drzavni_potvrdeni_dates, y=ny, fill_color='white') 

##########################################################################################

# DEATHS

# X 
x_drzavni_umrli=df_drzavni_umrli.index[-30:].tolist()

# Y 
y_drzavni_umrli=[]
for i in df_drzavni_umrli.iloc[-30:].values:
    for j in i:
        y_drzavni_umrli.append(j)

y_drzavni_umrli2=[]
for i in df_drzavni_umrli.iloc[-31:-1].values:
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
    x_drzavni_umrli_dates.append(datetime.datetime.strptime(s, '%m/%d/%y'))
    
p_umrli=figure(plot_width=600,x_axis_type='datetime', tools=TOOLS)
p_umrli.circle(x=x_drzavni_umrli_dates, y=ny, size=10, color='red') 

##########################################################################################

# RECOVERED

# X 
x_drzavni_oporavljeni=df_drzavni_oporavljeni.index[-30:].tolist()

# Y 
y_drzavni_oporavljeni=[]
for i in df_drzavni_oporavljeni.iloc[-30:].values:
    for j in i:
        y_drzavni_oporavljeni.append(j)

y_drzavni_oporavljeni2=[]
for i in df_drzavni_oporavljeni.iloc[-31:-1].values:
    for j in i:
        y_drzavni_oporavljeni2.append(j)


# REVERSED 2 DEFINED LISTS        
yr=list(reversed(y_drzavni_oporavljeni))
yrc=list(reversed(y_drzavni_oporavljeni2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYAS
ny=yra-yrca
print(ny)

# TO LIST, REVERSED
ny=list(reversed(ny))

x_drzavni_oporavljeni_dates=[]
for s in x_drzavni_oporavljeni: #'8/29/20'
    x_drzavni_oporavljeni_dates.append(datetime.datetime.strptime(s, '%m/%d/%y'))
    
p_oporavljeni=figure(plot_width=600,x_axis_type='datetime', tools=TOOLS)
p_oporavljeni.line(x=x_drzavni_oporavljeni_dates, y=ny, line_color='green',line_width=2) 
p_oporavljeni.circle(x=x_drzavni_oporavljeni_dates, y=ny, fill_color='white') 

##########################################################################################

# ACTIVE CASES

# X 
x_drzavni_oporavljeni=df_drzavni_oporavljeni.index[-30:].tolist()

# Y CONFIRMED - DEATHS - RECOVERED
a=np.array(y_drzavni_potvrdeni)
b=np.array(y_drzavni_umrli)
c=np.array(y_drzavni_oporavljeni)
y_aktivni=a-b-c

x_drzavni_aktivni_dates=[]
for s in x_drzavni_oporavljeni: #'8/29/20'
    x_drzavni_aktivni_dates.append(datetime.datetime.strptime(s, '%m/%d/%y'))
    
p_aktivni=figure(plot_width=600,x_axis_type='datetime', tools=TOOLS)
p_aktivni.line(x=x_drzavni_aktivni_dates, y=y_aktivni, line_color='orange',line_width=2) 
p_aktivni.circle(x=x_drzavni_aktivni_dates, y=y_aktivni, fill_color='white') 

output_file('test.html')
layout=row(column(p_potvrdeni,p_oporavljeni),column(p_umrli,p_aktivni))
show(layout)


