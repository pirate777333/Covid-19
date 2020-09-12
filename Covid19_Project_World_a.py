# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

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

# NEW CASES
df_grupirano_potvrdeni=df_potvrdeni.groupby('Country/Region').sum()
df_grupirano_potvrdeni_dates=df_grupirano_potvrdeni.iloc[:,2:]

# DEATHS
df_grupirano_umrli=df_umrli.groupby('Country/Region').sum()
df_grupirano_umrli_dates=df_grupirano_umrli.iloc[:,2:]

# RECOVERED
df_grupirano_oporavljeni=df_oporavljeni.groupby('Country/Region').sum()
df_grupirano_oporavljeni_dates=df_grupirano_oporavljeni.iloc[:,2:]

# INPUT COUNTRY
drzava=input('Input name of the Country:  ')
drzava=drzava.lower()
drzava=drzava.title()
print('Your Country:  ' + drzava)

try:
    df_drzavni_potvrdeni=df_grupirano_potvrdeni_dates.loc[drzava].to_frame()
    df_drzavni_umrli=df_grupirano_umrli_dates.loc[drzava].to_frame()
    df_drzavni_oporavljeni=df_grupirano_oporavljeni_dates.loc[drzava].to_frame()

except:
    print('Something went wrong. Name of the country is wrong or it does not exist.')

##########################################################################################

# NEW CASES

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

fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, figsize=(20,18))

ax[0,0].plot(x_drzavni_potvrdeni,ny, marker='.')
ax[0,0].set_xticklabels(x_drzavni_potvrdeni, rotation=0)
ax[0,0].set(title='Daily number of confirmed cases')
ax[0,0].annotate('Total number of\n'+'confirmed cases:\n'+str(y_drzavni_potvrdeni[-1]),
                 xy=('8/13/20',300),xytext=('8/13/20',300),fontsize=14, weight='bold')
ax[0,0].grid()

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

ax[0,1].scatter(x_drzavni_umrli,ny, marker='.', color='red')
ax[0,1].set_xticklabels(x_drzavni_umrli, rotation=90)
ax[0,1].yaxis.set_major_locator(MaxNLocator(integer=True))
ax[0,1].set(title='Daily number of deaths')
ax[0,1].annotate('Total number\n'+'of deaths:\n'+str(y_drzavni_umrli[-1]),
                 xy=('8/13/20',3),xytext=('8/13/20',3),fontsize=14, weight='bold')
ax[0,1].grid()

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

# TO LIST, REVERSED
ny=list(reversed(ny))

ax[1,0].plot(x_drzavni_oporavljeni,ny, marker='.', color='green')
ax[1,0].set_xticklabels(x_drzavni_oporavljeni, rotation=90)
ax[1,0].set(title='Daily number of recovered')
ax[1,0].annotate('Total number of\n'+'recovered:\n'+str(y_drzavni_oporavljeni[-1]),
                 xy=('8/13/20',200),xytext=('8/13/20',200),fontsize=14, weight='bold')
ax[1,0].grid()

##########################################################################################

# ACTIVE

# X 
x_drzavni_oporavljeni=df_drzavni_oporavljeni.index[-30:].tolist()

# Y CONFIRMED - DEATHS - RECOVERED
a=np.array(y_drzavni_potvrdeni)
b=np.array(y_drzavni_umrli)
c=np.array(y_drzavni_oporavljeni)
y=a-b-c

ax[1,1].plot(x_drzavni_oporavljeni,y, marker='.', color='orange')
ax[1,1].set_xticklabels(x_drzavni_oporavljeni, rotation=90)
ax[1,1].set(title='Daily number of active cases')
ax[1,1].grid()
plt.tight_layout()
plt.show()
